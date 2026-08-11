---
id: functional-analysis-theorems-gpt-image-v3
title: "Функциональный анализ: теоремные визуализации GPT.Image v3"
aliases: ["Визуальный пакет теорем функционального анализа v3"]
type: lab
status: canonical
publish: true
areas: [functional-analysis, scientific-visualization]
concepts: [visual-explanation, mathematical-geometry]
prerequisites: [visual-revision-roadmap-2026-07-31]
ai_domains: [scientific-communication]
source_refs:
  - id: boss-fa-2005
    pages: "36–37; 54–61; 90–92; 101–105; 112–122; 151–156; 164–165"
    role: primary
level: advanced
created: 2026-08-11
updated: 2026-08-12
---

# Функциональный анализ: теоремные визуализации GPT.Image v3

Пакет заменяет девять перегруженных иллюстраций v2. Принцип сжимающих отображений Банаха исключён из пакета: его фигура v8 уже соответствует новому визуальному контракту.

## Общий стиль

Во всех запросах используется неизменный префикс:

> ICML-style scientific figure, clean academic vector infographic, white background, muted blue-gray palette with one accent color, minimal typography, precise arrows, thin lines, labeled panels, no photorealism, no 3D glossy rendering, no decorative background, conference-paper figure aesthetics, mathematically clean, visually balanced.

Дополнение:

> Russian-first scientific labels; use English only for standard abbreviations. Clearly distinguish established result, analogy, research hypothesis, and failure mode. Mathematically motivated 3D coordinate surfaces, wireframes, spheres, shells, ellipsoids, manifolds, and potential fields are allowed and preferred when they reveal the abstraction. Use restrained flat vector shading and a clean scientific perspective; no glossy materials, cinematic rendering, or decorative depth.

## 1. Теорема Бэра о категориях

Use case: scientific-educational. Asset type: theorem insight figure for a Russian Math-for-AI course. Landscape 3:2. Exactly two main panels plus one thin failure strip. No paragraphs, no more than eight short labels, no English prose. Use the equivalent nowhere-dense formulation of the Baire category theorem. Main panel: a complete two-dimensional metric domain contains several different thin closed exceptional sets F₁,F₂,F₃,… drawn as curves, sparse filaments, and isolated fragments with empty interior, spread across the domain but never filling an open ball. Show a sequence of nested closed balls B₁⊃B₂⊃B₃ whose radii shrink geometrically; at step n the next ball avoids F_n. The balls converge to one orange point outside every F_n. Do not draw F_n as nested filled regions. Second compact panel marked «аналогия»: a parameter space crossed by thin exceptional surfaces E₁,E₂,E₃ and one orange configuration avoiding all of them; explicitly state that the analogy applies only when every exceptional set is nowhere dense. Failure strip: an incomplete space with the limiting point removed. Render only these labels, verbatim: «полное пространство», «нигде не плотные исключения», «вложенные шары избегают Fₙ», «общая точка вне всех Fₙ», «аналогия: избегаем все тонкие исключения», «только для нигде не плотных множеств», «неполнота: предел потерян». No Venn diagram, no filled sets labeled dense, no application claims, no filters, no household metaphor, no long formulas.

## 2. Принцип равномерной ограниченности

Use case: scientific-educational. Asset type: theorem insight figure for a Russian Math-for-AI course. Landscape 3:2. Exactly two main panels plus one thin failure strip. No paragraphs, no more than eight short labels, no English prose, no formulas. Main panel: a Banach-space unit ball with many directional rays. A family of linear operators has finite, direction-dependent pointwise bounds. Baire reveals one small interior ball on which all operators fit inside one common orange output ball; linear scaling transfers that local bound to every direction of the unit ball. Make this local-to-global mechanism visually dominant. Second compact panel marked «аналогия»: Jacobians of a model family; a finite sample of inputs does not certify a uniform bound, whereas a common operator-norm cap controls every direction. Failure strip: nonlinear local maps cannot be scaled globally by this theorem. Render only these labels, verbatim: «поточечная ограниченность», «общий локальный шар», «линейное масштабирование», «единая граница норм», «аналогия: нормы якобианов», «конечная проверка недостаточна», «граница: линейный случай». No gauges, dashboards, sensors, dense step sequence, or repeated Baire layers.

## 3. Теорема об открытом отображении

Use case: scientific-educational. Asset type: theorem insight figure for a Russian Math-for-AI course. Landscape 3:2. Exactly two main panels plus one thin failure strip. No paragraphs, no more than eight short labels, no English prose, and no equations. Main panel: a bounded surjective linear operator maps a unit ball in Banach space X to a distorted blue-gray region in Banach space Y that visibly contains one orange ball around zero. Within the same panel, show only three shrinking residual arrows that sum to a preimage, as a restrained geometric cue. Second compact panel marked «установленный результат»: an inverse problem where a small ball of output perturbations has controlled preimages, conveying bounded inverse stability. Failure strip: a dense but nonclosed range and a nonsurjective range each contain no output ball. Render only these labels, verbatim: «ограниченный сюръективный оператор», «образ единичного шара», «внутренний шар», «последовательные поправки», «устойчивый обратный оператор», «нет сюръективности — нет шара». No pipelines, funnels, doors, research-hypothesis panel, household metaphor, or proof text.

## 4. Теорема о замкнутом графике

Use case: scientific-educational. Asset type: theorem insight figure. Landscape 3:2. Main geometry in the product space X×Y: a thin blue-gray graph surface of a linear operator. Two sequences of paired points (x_n, T x_n) approach a limit point; because the graph is closed, the limit remains on the surface and equals (x, T x). Show the projection from the graph to X and its bounded inverse as a secondary geometric cue. Compact AI panel: a differential or PDE operator with its correct Sobolev domain; convergent inputs and outputs preserve the operator relation. Mark «установленный результат». Failure strip: differentiation treated as an everywhere-defined map on L²; the domain boundary is missing, so the theorem cannot be invoked. Required labels: «замкнутый график», «предел остаётся на графике», «полный домен», «ограниченный оператор», «область определения оператора», «не весь L²». No road or bridge metaphor, no 3D spectacle, no long proof text.

## 5. Теорема Хана—Банаха

Use case: scientific-educational. Asset type: theorem insight figure. Landscape 3:2. Main two-thirds: a lower-dimensional subspace M embedded in X. A linear functional is shown by parallel level hyperplanes on M; extend those level hyperplanes coherently through all of X while they remain below a translucent convex sublinear envelope p. Emphasize preservation of norm and orientation, not an interval-calibration analogy. Add a compact separation inset: a convex cloud and an external point separated by one supporting hyperplane. Compact AI transfer: a linear margin classifier uses the same separation geometry only for convexly separable representations; mark «установленная связь через теоремы разделения». Failure strip: overlapping nonconvex classes are not made separable by Hahn–Banach alone. Required labels: «подпространство M», «продолжение на X», «норма сохранена», «опорная гиперплоскость», «линейный зазор», «нелинейная неразделимость». No ruler, calibration scale, gauge, or claim that arbitrary data become separable.

## 6. Теорема Рисса о представлении функционала

Use case: scientific-educational. Asset type: theorem insight figure. Landscape 3:2. Main geometry: a Hilbert space with parallel level hyperplanes of a continuous linear functional. A unique orange vector y is orthogonal to every level hyperplane and converts the covector into the inner-product rule f(x)=⟨x,y⟩; show norm equality by matching the length of y to the steepness of the levels, without extra formulas. Compact AI panel: in an RKHS, an evaluation functional has a vector representative k_x, and a Hilbert gradient is a vector direction. Mark «установленный результат». Failure strip: in a general Banach space a covector has no canonical vector representative without an additional duality map. Required labels: «уровни функционала», «единственный представитель y», «скалярное произведение», «равенство норм», «RKHS: представитель k_x», «банахово пространство: нет канонического вектора». No microphone, receiver, sensor, or measurement-device metaphor.

## 7. Теорема Лебега о мажорируемой сходимости

Use case: scientific-educational. Asset type: theorem insight figure. Landscape 3:2. Use a reproducible-looking function plot. Main panel: several curves f_n converge pointwise to f while all remain between ±g; use a translucent blue-gray envelope and show the absolute area |f_n−f| shrinking to zero. Beside it, a clear counterexample spike n·1_(0,1/n): width shrinks while orange area stays constant, demonstrating why pointwise convergence alone is insufficient. Compact AI panel: limits of population risk or expected gradients may pass through expectation only under domination or uniform integrability; mark «установленный результат». Required labels: «общая интегрируемая мажоранта», «поточечная сходимость», «L¹-разность исчезает», «масса не должна убегать», «ожидание и предел», «без мажоранты: площадь сохраняется». Keep axes and curves mathematically clean; no random numerical ticks, no long formulas, no decorative objects.

## 8. Принцип неподвижной точки Шаудера

Use case: scientific-educational. Asset type: theorem insight figure for a Russian Math-for-AI course. Landscape 3:2. Exactly two main panels plus one thin failure strip. No paragraphs, no more than eight short labels, no English prose. Main panel: a closed convex set C inside a Banach space X, mapped continuously into itself. Show T(C) as a smaller relatively compact curved set, covered by a finite ε-net of blue points; their translucent convex hull contains approximate fixed points x_ε whose short residual arrows shrink toward one orange limit x*=T(x*). Second compact panel: an implicit neural operator with an equilibrium; mark «исследовательская гипотеза» and emphasize «существование, не алгоритм». Failure strip: a noncompact image creates a sequence drifting away without a convergent subsequence. Render only these labels, verbatim: «банахово пространство X», «замкнутое выпуклое множество C», «T(C) относительно компактно», «конечная ε-сеть», «предел x*=T(x*)», «существование, не алгоритм», «нет компактности — возможен уход». No word Banach, no contraction spiral, target icon, carousel, conveyor, or invented convergence rate.

## 9. Спектральная теорема для компактного самосопряжённого оператора

Use case: scientific-educational. Asset type: theorem insight figure. Landscape 3:2. Main two-thirds: an orthogonal field of eigen-directions in Hilbert space coupled to a one-dimensional spectral particle plot. Real eigenvalues are discrete, ordered by magnitude, and accumulate only at zero; an orange low-rank subspace keeps the leading modes while the blue-gray tail fades. Compact AI panel: covariance operator or kernel PCA; project data onto leading eigenfunctions and show retained energy versus discarded tail. Mark «установленный результат». Failure strip with two minimal cases: noncompact self-adjoint operator may have continuous spectral bands; compact non-self-adjoint operator may lack an orthonormal eigenbasis. Required labels: «ортогональные собственные моды», «действительный спектр», «λ_k → 0», «низкоранговое усечение», «сохранённая энергия», «непрерывный спектр / нет ортонормального базиса». No signal mixer, orchestra, audio waveform, SVD block poster, or long equations.

## Проверка разнообразия

| № | Представление | Главные примитивы | Семейство аналогии | Режим отказа |
|---:|---|---|---|---|
| 1 | intrinsic-geometry | плотные слои, вложенные шары, проколотый предел | none | неполнота |
| 2 | intrinsic-geometry | единичный шар, направления, локальный и глобальный радиусы | none | нелинейность или неполнота |
| 3 | intrinsic-geometry | деформированный образ шара, внутренний шар, поправки | none | несюръективность |
| 4 | intrinsic-geometry | граф в произведении пространств, сходящиеся пары | none | неверный домен |
| 5 | intrinsic-geometry | подпространство, уровни функционала, опорная гиперплоскость | none | неразделимые классы |
| 6 | intrinsic-geometry | уровни функционала, ортогональный представитель, RKHS | none | отсутствие канонической идентификации |
| 7 | computational-experiment | функции, мажоранта, площадь, концентрирующийся пик | none | уход массы |
| 8 | intrinsic-geometry | компактное выпуклое тело, ε-сеть, приближённые точки | none | отсутствие компактности |
| 9 | intrinsic-geometry | ортогональные моды, спектральные частицы, хвост | none | непрерывный или ненормальный спектр |

Доминирующие примитивы соседних фигур различаются; бытовые аналогии отсутствуют; восемь из девяти фигур основаны на внутренней математической геометрии.
