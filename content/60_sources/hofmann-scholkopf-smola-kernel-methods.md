---
id: source-hofmann-scholkopf-smola-kernel-methods
title: "Hofmann, Schölkopf, Smola — Обзор ядерных методов в машинном обучении"
aliases: ["A Review of Kernel Methods in Machine Learning", "Обзор ядерных методов"]
type: source
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

# Обзор ядерных методов в машинном обучении

## Роль источника

Работа Томаса Хофмана, Бернхарда Шёлькопфа и Александра Смолы связывает положительно определённые ядра, воспроизводящие ядерные гильбертовы пространства, выпуклую оптимизацию и статистические гарантии. Для портала она служит первичным источником по алгоритмическому маршруту «ядро → матрица Грама → конечномерная оптимизация → обобщающая способность».

## Паспорт файла

- исходный файл: `Kernel_methods_in_machine_learning.pdf`;
- объём: 53 PDF-страницы;
- SHA-256: `953DD6286CF35C7E36929F170833A3FD4F17970030D516B3D7C626363CAC5DF1`;
- текстовый слой доступен;
- математические обозначения после извлечения могут искажаться, поэтому формулы сверяются с рендером PDF;
- обзор не содержит полных доказательств для части результатов, поэтому для теорем используются указанные авторами первичные работы и учебники.

## Структура

Источник охватывает положительно определённые ядра и их классы, методы опорных векторов, оценку риска через отступ, статистические модели в RKHS и нелинейные методы без учителя. Точная карта разделов хранится в [[30_mathematics/kernel-methods/kernel-methods-source-map|карте источника]].

## Правило интеграции

Определение гильбертова пространства и теорема Рисса остаются в курсе функционального анализа. Специфическая для ядер часть интегрирована в [[30_mathematics/kernel-methods/modules/01-positive-definite-kernels-rkhs|первый модуль]] через единые узлы [[20_concepts/positive-definite-kernel|положительно определённого ядра]], [[30_mathematics/kernel-methods/theorems/moore-aronszajn-rkhs-correspondence|соответствия Мура—Ароншайна]], [[30_mathematics/kernel-methods/theorems/representer-theorem-kernel-expansion|теоремы о представителе]] и [[30_mathematics/kernel-methods/methods/kernel-construction-closure-rules|правил конструирования]]. Раздел выпуклого оценивания интегрирован в [[30_mathematics/kernel-methods/modules/02-support-vector-estimation|модуль методов опорных векторов]] с отдельными узлами двойственности, оценки носителя, регрессии и структурного отступа. Раздел обобщения интегрирован в [[30_mathematics/kernel-methods/modules/03-margin-uniform-convergence|третий модуль]] через единые узлы [[30_mathematics/kernel-methods/theorems/rademacher-uniform-convergence|равномерной сходимости]], [[30_mathematics/kernel-methods/theorems/rkhs-rademacher-complexity|сложности шара RKHS]], [[30_mathematics/kernel-methods/theorems/surrogate-excess-risk-transfer|калибровочного переноса]], [[30_mathematics/kernel-methods/theorems/margin-generalization-rate|скорости риска]] и [[20_concepts/tsybakov-noise-localization|локализации]]. Подраздел 5.1 интегрирован в [[30_mathematics/kernel-methods/modules/04-exponential-rkhs-statistical-models|четвёртый модуль]] через [[30_mathematics/kernel-methods/theorems/log-partition-moment-geometry|геометрию нормировки]], [[30_mathematics/kernel-methods/theorems/exponential-rkhs-density-universality|плотность экспоненциального класса]], [[30_mathematics/kernel-methods/methods/conditional-exponential-rkhs-model|условные модели]], [[30_mathematics/kernel-methods/theorems/structured-soft-margin-duality|структурную двойственность]] и [[30_mathematics/kernel-methods/theorems/constraint-generation-epsilon-guarantee|метод рабочего множества]]. Формулировка предложения 14 оставлена в `review`: напечатанное доказательство использует $\log p$ и требует дополнительной проверки случая плотностей с нулями. Подраздел 5.2 интегрирован в [[30_mathematics/kernel-methods/modules/05-markov-networks-graph-compatible-kernels|пятый модуль]] через [[30_mathematics/kernel-methods/theorems/hammersley-clifford-factorization|теорему факторизации]], [[30_mathematics/kernel-methods/theorems/graph-compatible-kernel-decomposition|разложение ядра]], [[30_mathematics/kernel-methods/theorems/clique-representer-sparse-expansion|кликовое представление]] и [[30_mathematics/kernel-methods/methods/graphical-kernel-probabilistic-inference|метод вывода]]. Раздел 6 интегрирован в [[30_mathematics/kernel-methods/modules/06-unsupervised-kernel-methods|шестой модуль]] через [[30_mathematics/kernel-methods/methods/kernel-pca-centered-gram|ядерный PCA]], [[30_mathematics/kernel-methods/methods/kernel-canonical-correlation|регуляризованную KCCA]], [[30_mathematics/kernel-methods/theorems/rkhs-cross-covariance-independence|операторный критерий независимости]], [[30_mathematics/kernel-methods/theorems/kernel-mean-embedding-mmd|средние вложения]] и [[30_mathematics/kernel-methods/methods/kernel-dependency-estimation-preimage|задачу прообраза]]. Обычный PCA не дублируется, а переиспользуется через [[50_bridges/svd-pca-compression-lora|существующий спектральный мост]].
