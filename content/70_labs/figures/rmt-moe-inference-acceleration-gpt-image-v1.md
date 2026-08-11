---
id: lab-rmt-moe-inference-acceleration-gpt-image-v1
title: "Промпты визуализаций RMT для MoE-инференса, версия 1"
aliases: ["RMT MoE figures v1", "RMT MoE execution plan prompts"]
type: lab
status: canonical
publish: true
areas: [random-matrix-theory, scientific-visualization, gpu-systems]
concepts: [visual-prompt, expert-merging, dynamic-routing, grouped-gemm]
prerequisites: [bridge-rmt-moe-inference-acceleration]
ai_domains: [mixture-of-experts, inference-acceleration, model-compression]
source_refs:
  - id: rmt4ml-2022
    pages: "60-121"
    role: mathematical-background
  - id: megablocks-2023
    pages: "1-15"
    role: systems-baseline
level: advanced
created: 2026-08-06
updated: 2026-08-12
---

# Промпты визуализаций RMT для MoE-инференса, версия 1

## Постоянная часть

> ICML-style scientific figure, clean academic vector infographic, white background, muted blue-gray palette with one accent color, minimal typography, precise arrows, thin lines, labeled panels, no photorealism, no 3D glossy rendering, no decorative background, conference-paper figure aesthetics, mathematically clean, visually balanced.

> Russian-first scientific labels; use English only for standard abbreviations. Clearly distinguish established result, analogy, research hypothesis, and failure mode.

## Реестр

| Файл | representation_type | visual_primitives | analogy_family | novelty_check | failure_mode |
|---|---|---|---|---|---|
| `rmt-moe-execution-plan-v1.png` | intrinsic geometry + AI-native mechanism | спектральная плотность, кластеры экспертов, граф remap, GEMM-тайлы | none | вместо диагностического прибора показан переход от спектральной геометрии к плану исполнения | RMT-сжатие без сокращения active FLOPs |
| `rmt-moe-speedup-map-v1.png` | computational experiment + phase map | трёхосевая карта, Pareto-фронт, матрица абляций | none | доминирующий примитив отличается от pipeline первой фигуры | ложное ускорение из-за разных backend |
| `rmt-moe-layerwise-representations-v1.png` | intrinsic tensor geometry + comparison | слои MoE, тензор весов, функциональные отклики, матрицы Грама | none | вместо pipeline показаны две конкурирующие математические репрезентации | смешение обратимой развёртки с потерями проекции |
| `rmt-moe-remap-for-beginners-v1.png` | AI-native computational mechanism | таблица вероятностей, группы экспертов, токены, тайлы GEMM | none | используется пошаговая геометрия данных GPU без аппаратной метафоры | ложное отождествление двух порядков top-k и remap |
| `rmt-moe-representation-regimes-v1.png` | method-selection phase map + tensor geometry | четыре режима представления, RMT-ранги Tucker, карта применимости, переход к слоям | none | вместо ещё одного pipeline показаны независимые экспериментальные ветви и их границы | ложный вывод, что внутрислойная избыточность разрешает удаление слоя |

## Фигура 1. RMT-план исполнения MoE

> Landscape scientific bridge figure titled «RMT-план исполнения для MoE». Three connected panels. Panel A «Спектральная структура»: show a tensor stack of expert weight matrices unfolded into X with rows as experts, then an eigenvalue density with a muted blue-gray noise bulk and three orange separated spikes; arrows from stable spike directions to three expert clusters. Mark this panel «исследовательская гипотеза для обученного MoE», not an established theorem. Panel B «План исполнения»: show several token paths entering top-k expert nodes; apply a clear cluster remap c(e), then duplicate cluster IDs merge through a compact UniqueReduce node, with routing weights summed; show compact plan symbols c, r, b, δ without long formulas. Panel C «GPU-исполнение»: compact token-expert assignments feed aligned rectangular grouped GEMM tiles; visibly fewer active tiles and fewer memory arrows than in a faint original baseline. Include small measurable outputs «качество», «память», «FLOPs», «задержка». Solid arrows only for established tensor grouping and grouped GEMM; dashed orange arrows for the proposed RMT transfer. Bottom warning strip: «Сжатие параметров не равно ускорению без сокращения active FLOPs и накладных расходов маршрутизации». Russian labels except RMT, MoE, GPU, GEMM, top-k and FLOPs. No circuit-board decoration, no dashboard, no photorealistic chips. Use spectral particles, thin matrices, routing graph and flat GEMM tile geometry.

## Фигура 2. Три независимые оси ускорения

> Landscape scientific figure titled «Когда сжатие MoE действительно ускоряет инференс». Use a clean three-axis phase map rather than a pipeline. Axes: «Память модели», «Активные FLOPs на токен», «Эффективность GPU». Plot five labeled method points connected as an experimental progression: «только merging», «remap + compact», «dynamic top-k», «общий низкоранговый базис», «смешанная точность». Show a muted Pareto surface from high memory/high latency to low memory/low latency, with one orange feasible frontier constrained by a horizontal quality-budget ribbon «потеря качества ≤ ε». On the right, a compact ablation matrix compares Original eager, RMT eager, Original fused, RMT fused and RMT kernel using checkmarks for equal backend comparisons. Add a small failure inset showing two bars: parameters decrease while latency stays flat because top-k and FFN width do not change. Mark system mechanisms as «установлено», and the RMT-selected operating points as «исследовательская гипотеза». Bottom warning: «Сравнивать только при одинаковых dtype, batch, sequence length и backend». Russian labels except RMT, MoE, GPU, FLOPs, top-k, FFN and dtype. No dashboard styling, no gauges, no decorative hardware; use mathematical phase geometry, Pareto curve and compact comparison matrix.

## Фигура 3. Послойные представления экспертов

> Landscape scientific bridge figure titled «Как представить экспертов каждого MoE-слоя». At the far left show a vertical transformer with four distinct MoE layers l=0,1,2,3; each layer has its own set of expert matrices and its own input distribution. Highlight l=0 with label «текущий пилот», and show a loop arrow over all layers labeled «полномодельный план: отдельно для каждого слоя». The center is split into two parallel branches. Upper branch «Точная развёртка весов»: stack W_gate, W_up and W_down for experts inside one layer, apply reversible reshape/vec into rows of X_l, and show a green equality badge «значения не потеряны; нормы Фробениуса сохранены». Then show the exact label «Матрица Грама весов» with K_l^(W)=X_l X_l^T/D_l. Lower branch «Текущий функциональный скетч»: inputs H_l pass through each expert f_l,e, outputs Y_l,e pass through random projection R to Z_l,e of shape N by p, then flatten each expert projection into exactly one row and stack the rows into A_l of shape E_l by (Np). Show G_l=A_l A_l^T/(Np). Label projection with orange badge «сжатие с потерями, проверять по seed, N, p». On the right both Gram matrices feed separate spectral plots and cluster maps c_l; add an optional dashed hybrid arrow «веса + функции + маршрутизация». Bottom failure strip: «Развёртка обратима; информация теряется при проекции, усечении ранга, объединении и квантовании». Mark exact reshape identities as «установлено» and the useful RMT clustering of trained MoE as «исследовательская гипотеза». Russian labels except RMT, MoE, SVD, W_gate, W_up, W_down, seed and standard formulas. Use tensor slabs, matrices, spectra and layer blocks; no household analogy and no decorative chips.

## Фигура 4. Переназначение экспертов для начинающих

> Landscape beginner-friendly scientific figure titled «Как переназначение экспертов исполняется на GPU». Use one worked example with four original experts and three groups. Panel A «Исходный роутер»: one token vector h enters a matrix multiplication and produces four logits z1,z2,z3,z4 and four probability bars p1,p2,p3,p4. Panel B «Группы»: show C1={e1,e3}, C2={e2}, C3={e4}; use matching colors and show grouped logits with the short formula z-tilde_c=logsumexp over the group, then probability bars where p-tilde_1=p1+p3, p-tilde_2=p2, p-tilde_3=p4. Label «масса вероятности сохранена». Panel C «Что делает GPU для пакета токенов»: show five numbered tensor operations as a clean data-flow: 1 matrix multiplication H W_gate^T, 2 grouped logsumexp, 3 top-k groups, 4 sort/compact token assignments by group, 5 grouped GEMM and weighted sum. Beneath it separate a blue box «реализовано сейчас: операции PyTorch, без собственного CUDA-ядра» and a dashed orange box «следующий этап: объединённое ядро Triton для шагов 2-4». Add a small comparison inset: «текущий путь: группы, затем top-k» versus «исследовательская альтернатива: top-k, затем переназначение», with a not-equal sign. In the legend use exactly «MoE — смесь экспертов», «RMT — теория случайных матриц», «top-k — выбор k лучших», and «GEMM — матричное умножение». Bottom warning: «Порядок операций влияет на выбранные группы; сравнивать отдельной абляцией». Russian labels except RMT, MoE, GPU, PyTorch, CUDA, Triton, top-k, logsumexp, GEMM and formulas. No hardware chip illustration; show tensors, tables, arrows and aligned GEMM tiles. Ensure large readable labels for a reader unfamiliar with CUDA.

## `rmt-moe-representation-regimes-v1.png`

> Create a landscape ICML-style scientific figure titled exactly «Четыре режима представления экспертов MoE». White background, clean academic vector infographic, muted blue-gray palette with green for information-preserving steps and orange for lossy or research-dependent steps, thin precise arrows, minimal Russian typography, no photorealism, no decorative hardware, no glossy 3D. Start at left with one MoE layer l containing E_l expert weight tensors and label «анализировать каждый слой отдельно». Split into four parallel labeled branches. A «Матрица Грама весов, без данных»: reversible mode-0 unfold X_l∈R^{E_l×D}, then small K_l^(W)=X_l X_l^T/D; green badge «дёшево, значения сохранены», orange boundary «веса близки не всегда функции близки». B «Функциональный скетч, калибровка без меток»: H_l flows through experts f_l,e, random projection R, rows A_l∈R^{E_l×Np}, then G_l=A_l A_l^T/(Np); badge «видит поведение», boundary «зависит от корпуса, N, p, seed». C «Гибридная геометрия»: three small matrices labeled «веса», «функции», «маршрутизация» combine as K_l(α)=α_W K_W+α_F K_F+α_R K_R; badge «лучшее покрытие», boundary «нужна настройка масштабов и α». D «HOSVD/Tucker + RMT»: show a multiway weight tensor, randomized mode sketches Y_m=W_(m)Ω_m, factor matrices Q_m, compact Tucker core and ranks (r_E,r_in,r_out); RMT spectral plots choose ranks at separated spikes. Mark «перспективная исследовательская гипотеза» and boundary «дороже; RMT null model must be validated». Beneath the four branches place a compact applicability matrix with rows «данных нет», «есть неразмеченная калибровка», «важна структура осей», «ограничены память/время» and columns matching A-D, using check marks and half-filled circles rather than prose. Add a bottom panel «Следующий масштаб: целые слои» showing progression «неравномерный бюджет → condensation → MoE Layer Drop → Block Drop». Put a prominent not-equal formula «избыточность экспертов внутри слоя ≠ избыточность всего слоя» and a gate requiring both «малое остаточное влияние I_l» and «малая уникальная спектральная энергия» before layer removal. Label established linear-algebra identities as «установлено» and RMT-guided Tucker ranks and layer pruning as «исследовательская гипотеза». Ensure every formula and dimension is exact and legible. Russian labels except RMT, MoE, HOSVD, Tucker, SVD, seed and standard formulas.
