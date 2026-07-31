@echo off
setlocal

set "WORKDIR=%~1"
if "%WORKDIR%"=="" set "WORKDIR=%~dp0.."
if not "%~1"=="" shift

set "NODE_EXE=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe"
if not exist "%NODE_EXE%" (
  for /f "delims=" %%I in ('where node 2^>nul') do if not defined NODE_FALLBACK set "NODE_FALLBACK=%%I"
  set "NODE_EXE=%NODE_FALLBACK%"
)

if not exist "%NODE_EXE%" (
  echo Node.js was not found. Quartz 5 requires Node.js 22 or newer.
  exit /b 1
)

set "VERSION_FILE=%TEMP%\quartz-node-major-%RANDOM%.txt"
"%NODE_EXE%" -p "process.versions.node.split('.')[0]" > "%VERSION_FILE%"
if errorlevel 1 (
  del /q "%VERSION_FILE%" 2>nul
  echo Could not determine the Node.js version.
  exit /b 1
)
set /p NODE_MAJOR=<"%VERSION_FILE%"
del /q "%VERSION_FILE%" 2>nul
if not defined NODE_MAJOR (
  echo Could not determine the Node.js version.
  exit /b 1
)
if %NODE_MAJOR% LSS 22 (
  echo Quartz 5 requires Node.js 22 or newer. Found major version %NODE_MAJOR%.
  exit /b 1
)

for %%I in ("%NODE_EXE%") do set "NODE_DIR=%%~dpI"
set "PATH=%NODE_DIR%;%PATH%"
set "npm_node_execpath=%NODE_EXE%"

echo Quartz runtime: %NODE_EXE%
pushd "%WORKDIR%"
if errorlevel 1 exit /b 1

"%NODE_EXE%" quartz\bootstrap-cli.mjs build --concurrency=1
set "EXIT_CODE=%ERRORLEVEL%"

popd
exit /b %EXIT_CODE%
