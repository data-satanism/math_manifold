---
id: functional-analysis-bridges-gpt-image-v3
title: Реестр промтов для связок функционального анализа v3
aliases: ["Функциональный анализ — связующие иллюстрации v3"]
type: lab
status: canonical
publish: true
areas: [functional-analysis, scientific-visualization]
concepts: [metric, lp-spaces, reproducing-kernel, spectrum, convolution, operator-equation, frechet-derivative, cones-positive-operators]
prerequisites: [visual-revision-roadmap-2026-07-31]
ai_domains: [embeddings, statistical-learning, kernel-methods, model-compression, neural-operators, inverse-problems, equilibrium-models, graph-ml]
source_refs:
  - id: boss-fa-2005
    pages: "14–18; 25–67; 90–92; 112–181"
    role: primary
level: advanced
created: 2026-08-11
updated: 2026-08-12
---

# Реестр промтов для связок функционального анализа v3

## Общая характеристика стиля

Во всех запросах дословно использован следующий префикс:

> ICML-style scientific figure, clean academic vector infographic, white background, muted blue-gray palette with one accent color, minimal typography, precise arrows, thin lines, labeled panels, no photorealism, no 3D glossy rendering, no decorative background, conference-paper figure aesthetics, mathematically clean, visually balanced. Russian-first scientific labels; use English only for standard abbreviations. Clearly distinguish established result, analogy, research hypothesis, and failure mode. Mathematically motivated 3D coordinate surfaces, wireframes, spheres, shells, ellipsoids, manifolds, and potential fields are allowed and preferred when they reveal the abstraction. Use restrained flat vector shading and a clean scientific perspective; no glossy materials, cinematic rendering, or decorative depth.

## Нормы, метрики и геометрия представлений

```text
Use case: scientific-educational. Asset type: landscape insight figure for the bridge “Нормы и метрики → функции потерь и геометрия представлений”.
Create two main panels and one narrow warning strip, generous whitespace, very little text.
Panel A title exactly “Математическая структура”. Show the same displacement vector measured by three unit-ball geometries: diamond L1, circle L2, square L∞, then show a dual supporting hyperplane touching one ball. Short labels only: “один сдвиг”, “разная длина”, “двойственная норма”.
Panel B title exactly “ИИ: перенос и проверка”. Show a 2D embedding point cloud where changing the metric deforms neighborhoods and changes the nearest neighbor; beside it show an adversarial perturbation arrow constrained by a norm ball and a margin boundary. Label the checkable quantities “соседи”, “запас”, “чувствительность”.
Bottom warning strip title exactly “Граница переноса”. Show concentration of distances in high dimension as a thin spherical shell and warn with only the phrase “близости размываются”.
One coral-orange accent for the displacement and selected neighbor. No rulers, instruments, dashboards, icons, people, photorealism, long prose, legends, decorative background, or invented formulas.
```

## Мера, хвост распределения и статистический риск

```text
Use case: scientific-educational. Asset type: landscape insight figure for the bridge “Мера и Lp → статистический риск и устойчивые функции потерь”.
Create two main panels and one compact failure strip, with generous whitespace and only Russian labels except the standard abbreviation CVaR.
Panel A title exactly “Риск как интеграл”. Show a probability density with a broad typical region and a long rare-event tail. Below it show one increasing loss curve. At the bottom show the product of density and loss as the shaded contribution to expectation. Use only the short labels “масса”, “потеря”, “вклад в риск”, “редкие большие ошибки”. Do not compare L1, L2, or L∞ in this figure.
Panel B title exactly “ИИ: выборка и оценка”. Show a smooth population-risk curve with uncertainty band and a finite set of sampled error points concentrated in the typical region. Compare three clearly named curves: “обычное среднее”, “устойчивая оценка”, “CVaR”. Mark the checkable vertical gap as “разрыв риска”.
Bottom strip title exactly “Режим отказа”. Show the rare-event tail outside the sampled points, with the exact phrase “хвост не попал в выборку”, and an empirical-risk marker below the true-risk marker.
One burnt-orange accent only for the tail and missed events. No English parenthetical translations, no maps, cities, disasters, houses, dashboards, icons, long prose, 3D bowl, norm-ball comparisons, or unsupported theorem claims.
```

## RKHS, матрица Грама и гауссовский процесс

```text
Use case: scientific-educational. Asset type: landscape insight figure for the bridge “Гильбертовы пространства → RKHS, ядра и гауссовские процессы”.
Create two main panels and a narrow failure strip, mathematically clean, minimal Russian labels.
Panel A title exactly “Математическая структура”. Show a smooth function surface in a Hilbert space, several kernel sections k_x as localized basis bumps, and an orthogonal decomposition into the span of training kernel sections plus a faint perpendicular component. The perpendicular component does not change sampled values but increases the norm. Labels: “оболочка ядер”, “ортогональная часть”, “минимальная норма”.
Panel B title exactly “ИИ: перенос и проверка”. Show nonlinear input points linked to a positive semidefinite Gram-matrix heatmap and then to a smooth posterior mean curve with a muted uncertainty band. Use labels “матрица Грама”, “среднее”, “неопределённость”, “проверка: K ⪰ 0”.
Bottom strip title exactly “Граница переноса”. Show an indefinite Gram matrix with one negative spectral direction and a torn Hilbert geometry; short label “отрицательное собственное значение”.
Use teal-green as the single accent. No coffee mugs, shadows, probes, physical analogies, dashboards, long equations, dense tables, English prose, or decorative 3D.
```

## Операторы, низкий ранг и спектральная диагностика

```text
Use case: scientific-educational. Asset type: landscape insight figure for the bridge “Операторы и спектр → PCA, SVD, LoRA и теория случайных матриц”.
Create three compact but spacious panels and one narrow failure strip. Every panel must show a different mathematical object and name it.
Panel A title exactly “Оператор”. Show a unit sphere transformed into an ellipsoid with singular axes; next to it show decreasing singular-value particles. Labels: “сингулярные направления”, “энергия”, “ранг r”.
Panel B title exactly “Низкий ранг”. Show a high-dimensional update represented as a thin rank-r plane crossing a smooth loss surface, with a projected update path and a small residual orthogonal to the plane. Labels: “LoRA”, “низкоранговая поправка”, “ошибка усечения”.
Panel C title exactly “Спектральная диагностика”. Show an RMT bulk density with a clear spectral edge and two separated outlier particles; connect the retained outliers to a low-rank data projection. Labels: “шумовой массив”, “край спектра”, “выбросы”.
Bottom strip title exactly “Режим отказа”. Show a nonnormal operator in the complex plane: eigenvalue dots appear stable but a large translucent pseudospectral contour bulges outward. Exact short label: “собственных значений недостаточно”.
Use violet as the single accent. No thermometers, barometers, speakers, sensors, diagnostic devices, dashboards, long prose, English sentences, or claim that LoRA optimality follows from spectral theory.
```

После генерации подпись `не нормальный оператор` заменена на `ненормальность` без изменения композиции.

## Свёртка, эквивариантность и обучение операторов

```text
Use case: scientific-educational. Asset type: landscape insight figure for the bridge “Обобщённые функции и свёртка → свёрточные сети и нейронные операторы”.
Create two main panels and a narrow failure strip, minimal Russian labels.
Panel A title exactly “Свёртка и симметрия”. Show a one-dimensional input field with a localized singular impulse, a smooth kernel sliding over it, and the resulting smoothed field. Beside it show the same input shifted and the output shifted by exactly the same amount, connected by a commuting-square diagram. Labels: “ядро”, “сдвиг входа”, “тот же сдвиг выхода”, “эквивариантность”.
Panel B title exactly “ИИ: оператор между полями”. Show a two-dimensional input field on a coarse grid, an operator arrow, and a smooth output field sampled on both coarse and fine grids. Emphasize that one learned operator acts across resolutions. Labels: “входное поле”, “оператор”, “выходное поле”, “проверка разрешения”.
Bottom strip title exactly “Режим отказа”. Show a translated feature approaching the boundary of a finite image; zero padding creates a false edge response. Exact label: “граница нарушает эквивариантность”.
Use cyan-teal as the single accent. No landscape scenery, scanners, sensors, sliding physical windows, photos, long formulas, architecture lists, English prose, or claim of exact equivariance with stride and padding.
```

После генерации `входное поле (1D)` и `zero padding` заменены на `одномерное входное поле` и `нулевое дополнение`.

## Операторные уравнения и регуляризация

```text
Use case: scientific-educational. Asset type: landscape insight figure for the bridge “Операторные уравнения → обратные задачи и регуляризация”.
Create two main panels and one narrow failure strip, using intrinsic geometry and minimal Russian labels.
Panel A title exactly “Неустойчивая обратимость”. Show a solution-space ellipsoid mapped by a compact forward operator into a very thin data-space ellipsoid with labeled singular directions. Add a small noise ball in data space whose inverse image becomes a long uncertainty tube along the smallest singular direction. Labels: “пространство решений”, “данные”, “малое σ”, “усиление шума”.
Panel B title exactly “ИИ: данные и априорная структура”. Show a blue data-consistency tube and an orange learned-prior manifold crossing it. The reconstruction is the intersection point. Nearby, show a classical regularization path approaching the same feasible region. Labels: “согласование с данными”, “априорная структура”, “регуляризованное решение”, “невязка”.
Bottom strip title exactly “Режим отказа”. Show a visually plausible point on the prior manifold but outside the data-consistency tube; exact label “правдоподобная галлюцинация”.
Use burnt orange as the single accent for the prior manifold and failure point. No cameras, blurred pictures, medical scans, sensors, solver dashboards, people, long prose, English labels, or assertion that a learned prior guarantees correctness.
```

После генерации подпись `Tikhonov` заменена на `регуляризация Тихонова`.

## Производная Фреше и неявный слой

```text
Use case: scientific-educational. Asset type: landscape insight figure for the bridge “Производная Фреше и неподвижные точки → автоматическое дифференцирование и неявные слои”.
Create two main panels and one compact failure strip, minimal Russian labels.
Panel A title exactly “Многообразие неподвижных точек”. Show a two-dimensional state plane with trajectories of the iteration z_{k+1}=F(z_k;θ) converging to one fixed point labeled exactly “z* = F(z*; θ)”. Extend this point into a smooth curve z*(θ) over a parameter axis and draw a tangent arrow labeled “чувствительность”. Include the exact short condition “I − D_zF обратим”.
Panel B title exactly “ИИ: неявный слой”. Show input x selecting an equilibrium on the curve. Label the forward diagnostic exactly “невязка ‖z − F(z,x)‖”. Show an adjoint solve with the simple formula “(I − D_zF)ᵀ λ = g_z” and an arrow to “градиент”. Add the label “проверить отдельно”.
Bottom strip title exactly “Режим отказа”. Show a point with small residual “‖z − F(z,x)‖ ≈ 0” but an almost vertical tangent and large inverse sensitivity. Exact phrase “малая невязка, большой градиент”.
Use magenta-purple as the single accent. No residual equation F(z,θ)=0 anywhere. No thermostats, gauges, repeated dials, dashboards, long prose, English labels, or claim that forward convergence alone guarantees stable gradients.
```

После генерации подпись `adjoint solve` заменена на `сопряжённая система`.

## Положительные операторы и монотонные модели

```text
Use case: scientific-educational. Asset type: landscape insight figure for the bridge “Положительные операторы → марковские процессы, Перрон—Фробениус и монотонные модели”.
Create three simple panels and a narrow failure strip, with minimal Russian labels.
Panel A title exactly “Конус и порядок”. Show a clean three-dimensional convex cone K inducing the order x ≤ y, and a positive linear map T sending the cone strictly inside itself. Labels: “допустимые направления”, “T(K) внутри K”, “порядок сохранён”.
Panel B title exactly “Диффузия на графе”. Show a graph with a nonnegative color field evolving over three time steps toward a stationary positive mode; below it show a probability-simplex trajectory converging to an interior fixed point. Labels: “масса сохранена”, “стационарная мода”, “спектральный зазор”.
Panel C title exactly “ИИ: монотонная модель”. Show a smooth prediction surface increasing along one declared feature direction, with comparable input points x ≤ y connected to outputs f(x) ≤ f(y). Label the check “нарушение порядка = 0”.
Bottom strip title exactly “Режим отказа”. Split into two tiny cases: a periodic two-cycle that never converges, and one negative edge weight that sends a vector outside the cone. Labels: “периодичность” and “отрицательный вес”.
Use green as the single accent. No scales, traffic, instruments, dashboards, checklists, long prose, English labels, or claim that nonnegativity alone guarantees convergence or global monotonicity.
```

После генерации условие спектрального зазора исправлено с `0 < λ₂ < 1` на `|λ₂| < 1`.

## Разнообразие представлений

| Страница | Представление | Главные примитивы | Режим отказа |
|---|---|---|---|
| нормы и метрики | внутренняя геометрия | единичные шары, опорная гиперплоскость, сферическая оболочка | концентрация расстояний |
| мера и риск | вычислительный эксперимент | плотность, хвост, вклад в интеграл, выборочные точки | хвост не наблюдался |
| RKHS | внутренняя геометрия | ядерные сечения, ортогональное разложение, матрица Грама | отрицательное собственное значение |
| операторы и спектр | геометрия ИИ | эллипсоид, поверхность потерь, спектральный массив | псевдоспектральное усиление |
| свёртка | геометрия ИИ | коммутирующая диаграмма, поля на двух сетках | краевой эффект |
| обратная задача | внутренняя геометрия | тонкий эллипсоид, труба согласованности, априорное многообразие | галлюцинация вне данных |
| неявный слой | внутренняя геометрия | поле итераций, многообразие неподвижных точек, касательная | большая чувствительность |
| положительные операторы | геометрия ИИ | конус, графовая мода, симплекс, монотонная поверхность | периодичность и выход из конуса |
