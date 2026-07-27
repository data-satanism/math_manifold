---
id: kernel-methods-map
title: "Ядерные методы в машинном обучении"
aliases: ["Курс по ядерным методам", "Обучение с положительно определёнными ядрами"]
type: map
status: canonical
publish: true
areas: [kernel-methods, functional-analysis, statistical-learning-theory]
concepts: [positive-definite-kernel, gram-matrix, reproducing-kernel, representer-theorem, support-vector-machine, margin, kernel-pca]
prerequisites: [hilbert-space, convex-optimization, probability-theory]
ai_domains: [kernels, support-vector-machines, representation-learning, structured-prediction, unsupervised-learning]
source_refs:
  - id: hofmann-scholkopf-smola-kernel-methods-2006
    pages: "1-53"
    role: primary
level: advanced
created: 2026-07-16
updated: 2026-07-27
---

# Ядерные методы в машинном обучении

## Главная цепочка

$$
k(x,x')
\longrightarrow K_{ij}
\longrightarrow \mathcal H_k
\longrightarrow \text{конечномерная выпуклая задача}
\longrightarrow \text{статистическая гарантия}.
$$

Курс расширяет [[50_bridges/hilbert-rkhs|существующий мост к RKHS]], а не повторяет его. Базовое гильбертово пространство и представление Рисса остаются едиными узлами. Новыми узлами становятся положительно и условно положительно определённые ядра, методы опорных векторов, оценки через отступ, средние Радемахера, экспоненциальные модели в RKHS, ядерный канонический корреляционный анализ и меры независимости.

## Маршрут источника

1. [[30_mathematics/kernel-methods/modules/01-positive-definite-kernels-rkhs|Положительно определённые ядра и воспроизводящие пространства]]: нелинейная задача как линейная задача в пространстве признаков.
2. [[20_concepts/positive-definite-kernel|Матрица Грама]], [[30_mathematics/kernel-methods/theorems/moore-aronszajn-rkhs-correspondence|соответствие Мура—Ароншайна]], [[30_mathematics/kernel-methods/theorems/representer-theorem-kernel-expansion|теорема о представителе]] и [[30_mathematics/kernel-methods/methods/kernel-construction-closure-rules|правила конструирования ядер]].
3. [[30_mathematics/kernel-methods/modules/02-support-vector-estimation|Методы опорных векторов]]: классификация с максимальным отступом, [[30_mathematics/kernel-methods/methods/one-class-svm-support-estimation|оценка носителя]], [[30_mathematics/kernel-methods/methods/epsilon-insensitive-kernel-regression|регрессия с нечувствительной зоной]] и [[30_mathematics/kernel-methods/theorems/structured-margin-loss-bound|структурное предсказание]].
4. [[30_mathematics/kernel-methods/modules/03-margin-uniform-convergence|Отступ, сложность класса и обобщение]]: [[30_mathematics/kernel-methods/theorems/rademacher-uniform-convergence|равномерная сходимость]], [[30_mathematics/kernel-methods/theorems/rkhs-rademacher-complexity|сложность шара RKHS]], [[30_mathematics/kernel-methods/theorems/surrogate-excess-risk-transfer|калибровка потерь]], [[30_mathematics/kernel-methods/theorems/margin-generalization-rate|скорость риска]] и [[20_concepts/tsybakov-noise-localization|локализация]].
5. [[30_mathematics/kernel-methods/modules/04-exponential-rkhs-statistical-models|Экспоненциальные статистические модели в RKHS]]: [[30_mathematics/kernel-methods/theorems/log-partition-moment-geometry|нормировка и моменты]], [[30_mathematics/kernel-methods/theorems/exponential-rkhs-density-universality|аппроксимационная плотность]], [[30_mathematics/kernel-methods/methods/conditional-exponential-rkhs-model|условные модели]], [[30_mathematics/kernel-methods/theorems/structured-soft-margin-duality|структурная двойственность]] и [[30_mathematics/kernel-methods/theorems/constraint-generation-epsilon-guarantee|добавление ограничений]].
6. [[30_mathematics/kernel-methods/modules/05-markov-networks-graph-compatible-kernels|Марковские сети и совместимые с графом ядра]]: [[30_mathematics/kernel-methods/theorems/hammersley-clifford-factorization|кликовая факторизация]], [[30_mathematics/kernel-methods/theorems/graph-compatible-kernel-decomposition|локальное разложение ядра]], [[30_mathematics/kernel-methods/theorems/clique-representer-sparse-expansion|кликовое представление]] и [[30_mathematics/kernel-methods/methods/graphical-kernel-probabilistic-inference|вероятностный вывод]].
7. [[30_mathematics/kernel-methods/modules/06-unsupervised-kernel-methods|Ядерные методы обучения без учителя]]: [[30_mathematics/kernel-methods/methods/kernel-pca-centered-gram|ядерный метод главных компонент]], [[30_mathematics/kernel-methods/methods/kernel-canonical-correlation|каноническая корреляция]], [[30_mathematics/kernel-methods/theorems/rkhs-cross-covariance-independence|HSIC]], [[30_mathematics/kernel-methods/theorems/kernel-mean-embedding-mmd|MMD]] и [[30_mathematics/kernel-methods/methods/kernel-dependency-estimation-preimage|оценивание структурированного выхода]].
8. Итоговая карта ограничений и вычислительной стоимости собрана в этом MOC и [[30_mathematics/kernel-methods/kernel-methods-source-map|постраничной карте источника]].

## Междисциплинарные связи

- [[30_mathematics/functional-analysis/modules/12-positive-operators|Положительность]] гарантирует допустимость матриц Грама.
- [[30_mathematics/numerical-analysis/modules/02-unitary-matrices-and-svd|Сингулярное разложение]] задаёт конечномерную механику ядерного метода главных компонент.
- [[30_mathematics/random-matrix-theory/random-matrix-theory-map|Теория случайных матриц]] описывает высокоразмерные спектральные и статистические эффекты ядерных матриц.
- [[50_bridges/hierarchical-matrices-kernel-attention|Иерархические матрицы]] и низкоранговые приближения дают вычислительный маршрут к большим выборкам.
- [[50_bridges/support-vector-margins-robust-ai|Отступы и опорные объекты]] связывают выпуклую геометрию с классификацией, мониторингом, регрессией и ранжированием.
- [[50_bridges/generalization-complexity-ai|Сложность класса]] связывает норму RKHS и случайные знаки с честным выбором моделей, проверкой утечки и границами переноса на обучаемые представления.
- [[50_bridges/log-partition-kernels-energy-models|Логарифмическая статистическая сумма]] связывает нормировку, остаток моментов и ковариационную кривизну с мягким максимальным преобразованием, условными случайными полями, энергетическими моделями и классификацией гауссовскими процессами.
- [[50_bridges/graphical-kernels-structured-inference|Графические ядра и структурный вывод]] связывают кликовую локальность, матрицу Грама, древесную ширину и точные алгоритмы разметки последовательностей.
- [[50_bridges/kernel-independence-representation-learning|Ядерные меры зависимости]] разделяют четыре задачи: нелинейную вариацию, согласование парных представлений, проверку независимости и сравнение распределений; это даёт маршрут к многомодальному обучению и мониторингу сдвига.

Карта покрытия: [[30_mathematics/kernel-methods/kernel-methods-source-map|все разделы обзора]]. Карточка источника: [[60_sources/hofmann-scholkopf-smola-kernel-methods|Hofmann, Schölkopf, Smola]].
