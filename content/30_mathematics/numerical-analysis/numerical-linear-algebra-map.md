---
id: numerical-linear-algebra-map
title: "Методы численного анализа для ИИ"
aliases: ["Курс по Тыртышникову", "Численная линейная алгебра для ИИ", "Numerical analysis for AI"]
type: map
status: canonical
publish: true
areas: [numerical-analysis, numerical-linear-algebra, approximation-theory]
concepts: [matrix-norms, conditioning, singular-value-decomposition, spectral-perturbation, floating-point, matrix-factorizations, interpolation, chebyshev-polynomials, splines, minimax-approximation, quadrature, newton-method, optimization, krylov-subspace, gmres, conjugate-gradient, preconditioning, weak-solution, multigrid, toeplitz-matrix, hierarchical-matrix, wavelet]
prerequisites: [linear-algebra, mathematical-analysis]
ai_domains: [optimization, model-compression, mixed-precision, pca, representation-learning, spectral-diagnostics, surrogate-modeling, calibration, uncertainty-quantification, implicit-layers, gaussian-processes, second-order-methods, neural-operators, scientific-machine-learning, attention]
source_refs:
  - id: tyrtyshnikov-numerical-analysis
    pages: "3-278"
    role: primary
  - id: tyrtyshnikov-local-notes
    pages: "Главы 1–8; для глав 9–25 использован первичный PDF"
    role: intuition
level: advanced
created: 2026-07-13
updated: 2026-07-27
---

# Методы численного анализа для ИИ

## Главная идея

Численный алгоритм отвечает не только на вопрос «какова точная формула?», но и на три практических вопроса: насколько задача чувствительна к данным, какую близкую задачу фактически решила машина и какие представления сохраняют геометрию при конечной точности.

Курс строит единую цепочку:

$$
\text{геометрия нормы}
\longrightarrow \text{обусловленность задачи}
\longrightarrow \text{устойчивость алгоритма}
\longrightarrow \text{надёжность системы машинного обучения}.
$$

## Маршрут по двадцати пяти главам

1. [[30_mathematics/numerical-analysis/modules/01-spaces-and-norms|Пространства, нормы и усиление возмущений]].
2. [[30_mathematics/numerical-analysis/modules/02-unitary-matrices-and-svd|Скалярное произведение, унитарные матрицы и SVD]].
3. [[30_mathematics/numerical-analysis/modules/03-conditioning-and-matrix-series|Обусловленность, матричные ряды и простая итерация]].
4. [[30_mathematics/numerical-analysis/modules/04-spectral-localization-and-perturbation|Локализация спектра и возмущение собственных пар]].
5. [[30_mathematics/numerical-analysis/modules/05-spectral-distances-and-clusters|Спектральные расстояния, разделение и кластеры]].
6. [[30_mathematics/numerical-analysis/modules/06-floating-point-and-rounding-errors|Машинная арифметика и анализ ошибок]].
7. [[30_mathematics/numerical-analysis/modules/07-lu-cholesky-and-refinement|LU, выбор ведущего элемента, Холецкий и уточнение]].
8. [[30_mathematics/numerical-analysis/modules/08-qr-and-orthogonalization|QR, отражения, вращения и ортогонализация]].
9. [[30_mathematics/numerical-analysis/modules/10-power-and-subspace-iteration|Степенной метод, итерации подпространства и главные углы]].
10. [[30_mathematics/numerical-analysis/modules/11-qr-eigenvalue-algorithm|QR-алгоритм для задачи собственных значений]].
11. [[30_mathematics/numerical-analysis/modules/12-shifted-qr-and-svd|Сдвиги, неявный QR-алгоритм и вычисление SVD]].
12. [[30_mathematics/numerical-analysis/modules/13-interpolation-and-vandermonde|Интерполяция и матрица Вандермонда]].
13. [[30_mathematics/numerical-analysis/modules/14-chebyshev-convergence|Сходимость интерполяции и узлы Чебышёва]].
14. [[30_mathematics/numerical-analysis/modules/15-splines|Сплайны, гладкость и квазилокальность]].
15. [[30_mathematics/numerical-analysis/modules/16-best-approximation-and-orthogonal-polynomials|Наилучшее приближение и ортогональные многочлены]].
16. [[30_mathematics/numerical-analysis/modules/17-numerical-integration|Численное интегрирование и формулы Гаусса]].
17. [[30_mathematics/numerical-analysis/modules/18-nonlinear-equations-newton-secant|Нелинейные уравнения, Ньютон и секущие]].
18. [[30_mathematics/numerical-analysis/modules/19-unconstrained-optimization|Безусловная минимизация и глобализация шага]].
19. [[30_mathematics/numerical-analysis/modules/20-krylov-projection-methods|Проекционные и крыловские методы]].
20. [[30_mathematics/numerical-analysis/modules/21-gmres-convergence|Сходимость метода минимальных невязок]].
21. [[30_mathematics/numerical-analysis/modules/22-cg-ritz-preconditioning|Сопряжённые градиенты, числа Ритца и предобусловливание]].
22. [[30_mathematics/numerical-analysis/modules/23-operator-equations-fem-galerkin|Операторные уравнения, слабые решения и метод Галёркина]].
23. [[30_mathematics/numerical-analysis/modules/24-multigrid-subspace-corrections|Многосеточные методы и коррекции на подпространствах]].
24. [[30_mathematics/numerical-analysis/modules/25-structured-toeplitz-circulant|Теплицевы матрицы, циркулянты и быстрое преобразование Фурье]].
25. [[30_mathematics/numerical-analysis/modules/26-hierarchical-low-rank-wavelets|Многоуровневые матрицы, крестовая аппроксимация и вейвлеты]].

Исходный конспект об итерационных решателях не соответствует книжной главе 4 и сохранён как обзорная карта [[30_mathematics/numerical-analysis/modules/09-iterative-solvers-and-preconditioning|итерационных решателей и предобусловливания]]. Формальные утверждения ведут из неё к главам 19–21.

## Центральные результаты и методы

- [[30_mathematics/numerical-analysis/theorems/eckart-young-theorem|Теорема Эккарта—Янга]];
- [[30_mathematics/numerical-analysis/theorems/gershgorin-circles|Теорема о кругах Гершгорина]];
- [[30_mathematics/numerical-analysis/theorems/weyl-eigenvalue-perturbation|Теорема Вейля о возмущении собственных значений]];
- [[30_mathematics/numerical-analysis/theorems/wielandt-hoffman-theorem|Теорема Виландта—Хоффмана]];
- [[20_concepts/numerical-conditioning|Обусловленность численной задачи]];
- [[20_concepts/backward-stability|Обратная устойчивость алгоритма]];
- [[30_mathematics/numerical-analysis/methods/lu-factorization-with-pivoting|LU-разложение с выбором ведущего элемента]];
- [[30_mathematics/numerical-analysis/theorems/cholesky-factorization|Разложение Холецкого]];
- [[30_mathematics/numerical-analysis/methods/iterative-refinement|Итерационное уточнение]];
- [[30_mathematics/numerical-analysis/theorems/qr-factorization|Теорема о QR-разложении]];
- [[30_mathematics/numerical-analysis/methods/householder-and-givens|Отражения Хаусхолдера и вращения Гивенса]];
- [[30_mathematics/numerical-analysis/methods/modified-gram-schmidt|Модифицированная ортогонализация Грама—Шмидта]];
- [[30_mathematics/numerical-analysis/theorems/subspace-projector-distance|Расстояние между подпространствами через ортопроекторы]];
- [[30_mathematics/numerical-analysis/theorems/cs-decomposition|CS-разложение и главные углы]];
- [[30_mathematics/numerical-analysis/theorems/subspace-iteration-convergence|Сходимость итераций подпространства]];
- [[30_mathematics/numerical-analysis/theorems/qr-algorithm-convergence|Сходимость QR-алгоритма]];
- [[30_mathematics/numerical-analysis/theorems/rayleigh-shift-quadratic-convergence|Квадратичная сходимость со сдвигами Релея]];
- [[30_mathematics/numerical-analysis/theorems/hermitian-qr-cubic-convergence|Кубическая сходимость в эрмитовом случае]];
- [[30_mathematics/numerical-analysis/theorems/implicit-qr-uniqueness|Лемма о неявном QR-алгоритме]].
- [[30_mathematics/numerical-analysis/theorems/vandermonde-conditioning-lower-bound|Нижняя оценка обусловленности матрицы Вандермонда]];
- [[30_mathematics/numerical-analysis/theorems/lagrange-interpolation-remainder|Остаток интерполяции Лагранжа]];
- [[30_mathematics/numerical-analysis/theorems/faber-bernstein-divergence|Теорема Фабера—Бернштейна]];
- [[30_mathematics/numerical-analysis/theorems/chebyshev-interpolation-stability|Устойчивость интерполяции в узлах Чебышёва]];
- [[30_mathematics/numerical-analysis/theorems/bernstein-ellipse-interpolation|Интерполяция аналитических функций и эллипс Бернштейна]];
- [[30_mathematics/numerical-analysis/theorems/natural-spline-variational-principle|Вариационный принцип естественного сплайна]];
- [[30_mathematics/numerical-analysis/theorems/natural-spline-approximation|Оценки приближения сплайном]];
- [[30_mathematics/numerical-analysis/theorems/banded-inverse-decay|Убывание обратной ленточной матрицы]];
- [[30_mathematics/numerical-analysis/theorems/chebyshev-alternation|Теорема Чебышёва об альтернансе]];
- [[30_mathematics/numerical-analysis/theorems/monic-chebyshev-minimax|Минимаксное свойство многочлена Чебышёва]];
- [[30_mathematics/numerical-analysis/theorems/orthogonal-polynomial-interlacing|Перемежаемость корней ортогональных многочленов]];
- [[30_mathematics/numerical-analysis/theorems/gaussian-quadrature-optimality|Оптимальность квадратуры Гаусса]].
- [[30_mathematics/numerical-analysis/theorems/fixed-point-contraction|Теорема о сжимающем отображении]].
- [[30_mathematics/numerical-analysis/theorems/newton-local-quadratic-convergence|Локальная квадратичная сходимость Ньютона]].
- [[30_mathematics/numerical-analysis/theorems/strong-convexity-unique-minimizer|Сильная выпуклость и единственный минимум]].
- [[30_mathematics/numerical-analysis/theorems/global-line-search-gradient-convergence|Сходимость поиска шага]].
- [[30_mathematics/numerical-analysis/theorems/krylov-near-optimality|Почти оптимальность крыловской информации]].
- [[30_mathematics/numerical-analysis/theorems/gmres-minimal-residual|Характеристика минимальной невязки]].
- [[30_mathematics/numerical-analysis/theorems/gmres-polynomial-residual-bound|Полиномиальная оценка невязки]].
- [[30_mathematics/numerical-analysis/theorems/cg-a-norm-optimality|Оптимальность сопряжённых градиентов в энергетической норме]].
- [[30_mathematics/numerical-analysis/theorems/cg-chebyshev-convergence|Классическая оценка сопряжённых градиентов]].
- [[30_mathematics/numerical-analysis/theorems/ritz-superlinear-convergence|Числа Ритца и ускорение сходимости]].
- [[30_mathematics/numerical-analysis/theorems/projection-stability-convergence|Устойчивость и аппроксимация проекционного метода]].
- [[30_mathematics/numerical-analysis/theorems/coercive-form-existence|Существование слабого решения для коэрцитивной формы]].
- [[30_mathematics/numerical-analysis/theorems/fredholm-alternative-compact|Альтернатива Фредгольма]].
- [[30_mathematics/numerical-analysis/theorems/multigrid-v-cycle-convergence|Сеточно-независимая сходимость V-цикла]].
- [[30_mathematics/numerical-analysis/theorems/subspace-correction-condition-bound|Обусловленность коррекций на подпространствах]].
- [[30_mathematics/numerical-analysis/theorems/circulant-fourier-diagonalization|Диагонализация циркулянта преобразованием Фурье]].
- [[30_mathematics/numerical-analysis/theorems/toeplitz-circulant-spectral-clustering|Кластеризация спектра теплицевой системы]].
- [[30_mathematics/numerical-analysis/theorems/banded-inverse-quasiseparable|Семисепарабельность обратной ленточной матрицы]].
- [[30_mathematics/numerical-analysis/theorems/hierarchical-matrix-compressibility|Сжимаемость иерархической матрицы]].
- [[30_mathematics/numerical-analysis/theorems/cross-approximation-max-volume|Оценка крестовой аппроксимации]].

## Мосты к ИИ

1. [[50_bridges/conditioning-optimization-geometry|Обусловленность и геометрия оптимизации]].
2. [[50_bridges/svd-pca-compression-lora|SVD, PCA, сжатие и LoRA]].
3. [[50_bridges/spectral-perturbation-rmt|Устойчивость спектра, метод главных компонент, векторные представления и теория случайных матриц]].
4. [[50_bridges/krylov-preconditioning-ml|Предобусловливание и крыловские методы в машинном обучении]].
5. [[50_bridges/backward-stability-mixed-precision|Обратная устойчивость и смешанная точность]].
6. [[50_bridges/qr-subspace-low-rank|QR и устойчивые подпространственные методы]].
7. [[50_bridges/principal-angles-representation-drift|Главные углы и дрейф пространств признаков]].
8. [[50_bridges/shifted-qr-spectral-diagnostics|Сдвинутый QR-алгоритм и спектральная диагностика моделей]].
9. [[50_bridges/interpolation-conditioning-surrogates|Интерполяция, обусловленность и суррогатные модели]].
10. [[50_bridges/chebyshev-minimax-neural-approximation|Минимакс и робастное приближение]].
11. [[50_bridges/splines-calibration-monotone-models|Сплайны, калибровка и монотонные модели]].
12. [[50_bridges/gaussian-quadrature-expectations|Квадратура Гаусса и оценка математических ожиданий]].
13. [[50_bridges/newton-implicit-equilibrium|Ньютон, неявные слои и равновесные модели]].
14. [[50_bridges/hessian-geometry-optimization|Гессиан и геометрия обучения модели]].
15. [[50_bridges/krylov-hessian-vector-products|Крыловские шаги второго порядка]].
16. [[50_bridges/iterative-solvers-gaussian-processes|Итерационные решатели для гауссовских процессов]].
17. [[50_bridges/preconditioning-ml-optimization|Предобусловливание и масштабирование параметров]].
18. [[50_bridges/galerkin-neural-operators|Галёркинские и обучаемые пространства]].
19. [[50_bridges/multigrid-multiscale-learning|Многосеточный метод и многоуровневые представления]].
20. [[50_bridges/fft-convolution-structured-layers|БПФ, свёрточные и спектральные слои]].
21. [[50_bridges/hierarchical-matrices-kernel-attention|Иерархические матрицы, ядра и внимание]].
22. [[50_bridges/wavelets-multiresolution-representations|Вейвлеты и многоразрешающие признаки]].

## Как читать

Читателю, знакомому с линейной алгеброй и математическим анализом, лучше идти по главам последовательно. Для прикладного маршрута можно начать с сингулярного разложения и обусловленности, затем перейти к устойчивым матричным алгоритмам. Главы 17–21 образуют цепочку «Ньютон → глобализация → крыловская проекция → предобусловливание», а главы 22–25 — цепочку «слабая форма → коррекция по масштабам → структура сдвига → иерархическое сжатие».

Интерактивные маршруты: [[70_labs/interactive/nonlinear-optimization-krylov-widgets|Ньютон, оптимизация и крыловские методы]]; [[70_labs/interactive/operator-multigrid-structured-widgets|операторные, многосеточные и структурированные методы]].

Каждая формальная связь с ИИ помечается как установленный результат, аналогия или исследовательская гипотеза. Утверждения из первой категории применяются только при явно выписанных предпосылках.

## Источник и границы текущего блока

- [[60_sources/tyrtyshnikov-numerical-analysis|Карточка первичного источника]].
- [[30_mathematics/numerical-analysis/tyrtyshnikov-source-map|Карта покрытия всех подразделов 1.1–25.9]].

Все страницы имеют статус `review`. Перевести их в `canonical` и разрешить публикацию может только пользователь после ручной сверки.
