---
id: mathematics-integration-map
title: "Интеграция математических направлений и ИИ"
aliases: ["Карта междисциплинарных связей", "Cross-domain mathematics map"]
type: map
status: canonical
publish: true
areas: [knowledge-engineering, applied-mathematics, functional-analysis, linear-algebra, numerical-analysis, kernel-methods, random-matrix-theory]
concepts: [knowledge-graph, mathematical-invariant, source-integration]
prerequisites: [content-integration-policy]
ai_domains: [scientific-machine-learning, kernels, representation-learning, optimization, neural-operators, graph-learning]
source_refs:
  - id: myshkis-applied-mathematics-engineers-2006
    pages: "11-671"
    role: primary
  - id: hofmann-scholkopf-smola-kernel-methods-2006
    pages: "1-53"
    role: primary
  - id: boss-linear-algebra-2005
    pages: "10-215"
    role: primary
level: advanced
created: 2026-07-16
updated: 2026-07-27
---

# Интеграция математических направлений и ИИ

## Зачем нужна эта карта

Новые источники не образуют три независимых курса. Они усиливают уже существующий граф: прикладная математика добавляет физические модели и вариационные механизмы, линейная алгебра уточняет конечномерные структуры, функциональный анализ даёт бесконечномерные основания, численный анализ превращает утверждения в алгоритмы, а теория случайных матриц описывает высокоразмерный режим.

## Основные линии переноса

| Сохраняемая структура | Источники и разделы | Существующий узел | Перенос в ИИ и машинное обучение |
|---|---|---|---|
| Внутреннее произведение и положительность | Босс; обзор ядерных методов | [[20_concepts/hilbert-space|Гильбертово пространство]], [[50_bridges/hilbert-rkhs|RKHS и ядра]] | допустимые ядра, матрицы Грама, гауссовские процессы |
| Спектр и инвариантные подпространства | Босс; Тыртышников; RMT | [[30_mathematics/functional-analysis/modules/10-spectral-theory|Спектральная теория]], [[50_bridges/operators-spectrum|операторы и спектр]] | PCA, устойчивость представлений, спектральная диагностика |
| Вариационный принцип | Мышкис; функциональный и численный анализ | [[30_mathematics/functional-analysis/modules/11-nonlinear-frechet|производная Фреше]], [[30_mathematics/numerical-analysis/modules/23-operator-equations-fem-galerkin|слабые решения и Галёркин]] | неявные слои, физически информированные модели, neural operators |
| Свёртка и преобразования | Мышкис; функциональный анализ | [[30_mathematics/functional-analysis/modules/08-distributions-convolution|обобщённые функции и свёртка]], [[50_bridges/fft-convolution-structured-layers|БПФ и свёрточные слои]] | CNN, спектральные слои, фильтрация временных рядов |
| Положительный конус и монотонность | Босс; функциональный анализ | [[30_mathematics/functional-analysis/modules/12-positive-operators|положительные операторы]] | марковские модели, монотонные сети, устойчивые динамические слои |
| Низкоранговая и ядерная структура | обзор ядерных методов; Тыртышников; RMT | [[50_bridges/hierarchical-matrices-kernel-attention|иерархические матрицы, ядра и внимание]] | приближения Нюстрёма, случайные признаки, быстрое внимание |
| Резольвента и интегральное уравнение | Мышкис; функциональный анализ; RMT | [[30_mathematics/functional-analysis/modules/09-operator-equations|операторные уравнения]], [[50_bridges/operator-equations|обратные задачи]] | регуляризация, операторное обучение, спектральные детерминированные эквиваленты |
| Отступ и сложность класса | обзор ядерных методов | [[30_mathematics/kernel-methods/modules/02-support-vector-estimation|методы опорных векторов]], [[30_mathematics/kernel-methods/modules/03-margin-uniform-convergence|равномерная сходимость]], [[50_bridges/generalization-complexity-ai|AI-мост]] | классификация, честный выбор моделей, диагностика представлений, оценки обобщения |
| Нормировка, моменты и ковариация | обзор ядерных методов, раздел 5.1 | [[30_mathematics/kernel-methods/theorems/log-partition-moment-geometry|логарифмическая статистическая сумма]], [[30_mathematics/kernel-methods/methods/conditional-exponential-rkhs-model|условная модель RKHS]], [[50_bridges/log-partition-kernels-energy-models|AI-мост]] | мягкое максимальное преобразование, условные случайные поля, энергетические модели, классификация гауссовскими процессами |
| Кликовая локальность и древесная ширина | обзор ядерных методов, раздел 5.2 | [[30_mathematics/kernel-methods/theorems/hammersley-clifford-factorization|факторизация]], [[30_mathematics/kernel-methods/theorems/graph-compatible-kernel-decomposition|графическое ядро]], [[50_bridges/graphical-kernels-structured-inference|AI-мост]] | разметка последовательностей, условные случайные поля, структурные методы опорных векторов, вероятностный вывод |
| Центрирование, перекрёстная ковариация и средние вложения | обзор ядерных методов, раздел 6; линейная алгебра; RMT | [[30_mathematics/kernel-methods/methods/kernel-pca-centered-gram|ядерный PCA]], [[30_mathematics/kernel-methods/theorems/rkhs-cross-covariance-independence|HSIC]], [[30_mathematics/kernel-methods/theorems/kernel-mean-embedding-mmd|MMD]], [[50_bridges/kernel-independence-representation-learning|AI-мост]] | согласование модальностей, диагностика представлений, двухвыборочные критерии, мониторинг сдвига |

## Очередь интеграции

1. [[30_mathematics/applied-mathematics/applied-mathematics-map|Прикладная математика для инженеров]]: новые области и физические интерпретации.
2. [[30_mathematics/kernel-methods/kernel-methods-map|Ядерные методы]]: усиление RKHS-моста до полноценного курса.
3. [[30_mathematics/linear-algebra/boss-linear-algebra-map|Линейная алгебра Босса]]: точечное дополнение существующей линейной и численной алгебры.

Решение по каждому пересекающемуся разделу хранится в `90_admin/content_overlap_registry.csv`. Правила выбора описаны в административной заметке `90_admin/content-integration-policy.md`.
