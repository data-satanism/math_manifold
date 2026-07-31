[CmdletBinding()]
param(
    [string]$WorkingDirectory = (Split-Path -Parent $PSScriptRoot),
    [string]$NodeExecutable = "",
    [ValidateRange(1, 64)]
    [int]$Concurrency = 1,
    [switch]$VerboseBuild
)

$ErrorActionPreference = "Stop"

function Get-NodeMajorVersion {
    param([string]$Executable)

    $version = & $Executable -p "process.versions.node"
    if ($LASTEXITCODE -ne 0 -or -not $version) {
        return -1
    }
    return [int](($version.Trim() -split '\.')[0])
}

$candidates = [System.Collections.Generic.List[string]]::new()
if ($NodeExecutable) {
    $candidates.Add($NodeExecutable)
}

$codexNode = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe"
if (Test-Path -LiteralPath $codexNode) {
    $candidates.Add($codexNode)
}

$nodeCommand = Get-Command node -ErrorAction SilentlyContinue
if ($nodeCommand) {
    $candidates.Add($nodeCommand.Source)
}

$selectedNode = $null
foreach ($candidate in $candidates | Select-Object -Unique) {
    if ((Test-Path -LiteralPath $candidate) -and (Get-NodeMajorVersion $candidate) -ge 22) {
        $selectedNode = (Resolve-Path -LiteralPath $candidate).Path
        break
    }
}

if (-not $selectedNode) {
    throw "Quartz 5 requires Node.js 22 or newer. Pass -NodeExecutable with an absolute path to node.exe."
}

$resolvedWorkingDirectory = (Resolve-Path -LiteralPath $WorkingDirectory).Path
$bootstrap = Join-Path $resolvedWorkingDirectory "quartz\bootstrap-cli.mjs"
if (-not (Test-Path -LiteralPath $bootstrap)) {
    throw "Quartz bootstrap was not found in $resolvedWorkingDirectory"
}

# Quartz and its plugin workers must resolve the same Node runtime. Without
# this override Windows may start an older node.exe through npm/npx and wait
# indefinitely before parsing Markdown.
$nodeDirectory = Split-Path -Parent $selectedNode
$env:PATH = "$nodeDirectory;$env:PATH"
$env:npm_node_execpath = $selectedNode

$arguments = @("quartz/bootstrap-cli.mjs", "build", "--concurrency=$Concurrency")
if ($VerboseBuild) {
    $arguments += "--verbose"
}

Write-Host "Quartz runtime: $selectedNode"
Push-Location $resolvedWorkingDirectory
try {
    & $selectedNode @arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Quartz build failed with exit code $LASTEXITCODE"
    }
}
finally {
    Pop-Location
}
