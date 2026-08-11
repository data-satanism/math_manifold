---
id: kernel-methods-source-map
title: "Карта источника: обзор ядерных методов"
aliases: ["Карта обзора ядерных методов", "Карта Хофмана, Шёлькопфа и Смолы"]
type: map
status: canonical
publish: true
areas: [kernel-methods, source-mapping]
concepts: [source-integration, duplicate-control]
prerequisites: [content-integration-policy]
ai_domains: [kernels, support-vector-machines, unsupervised-learning]
source_refs:
  - id: hofmann-scholkopf-smola-kernel-methods-2006
    pages: "1-53"
    role: primary
level: advanced
created: 2026-07-16
updated: 2026-07-27
---

# Карта источника: обзор ядерных методов

Номера ниже относятся к PDF-страницам локального файла. Обзор часто отсылает доказательства к первичным работам; такие утверждения не переходят в `canonical` без дополнительного источника.

| Раздел | Название | PDF-страницы | Интеграция |
|---|---|---:|---|
| 1 | Introduction | 2 | дополнено: [[50_bridges/hilbert-rkhs]] и [[30_mathematics/kernel-methods/modules/01-positive-definite-kernels-rkhs]] |
| 2.1 | An Introductory Example | 3 | включено в модуль 1: геометрия классификатора в пространстве признаков |
| 2.2 | Positive Definite Kernels | 4–14 | интегрировано: [[20_concepts/positive-definite-kernel]], [[30_mathematics/kernel-methods/theorems/moore-aronszajn-rkhs-correspondence]], [[30_mathematics/kernel-methods/methods/kernel-construction-closure-rules]] |
| 2.3 | Kernel Function Classes | 15–19 | интегрировано: [[30_mathematics/kernel-methods/theorems/representer-theorem-kernel-expansion]] и сокращённые разложения в модуле 1 |
| 3.1 | Support Vector Classification | 20–21 | интегрировано: [[30_mathematics/kernel-methods/modules/02-support-vector-estimation]], [[30_mathematics/kernel-methods/theorems/svm-duality-nu-bounds]] |
| 3.2 | Estimating the Support of a Density | 22 | интегрировано: [[30_mathematics/kernel-methods/methods/one-class-svm-support-estimation]] |
| 3.3 | Regression Estimation | 23 | интегрировано: [[30_mathematics/kernel-methods/methods/epsilon-insensitive-kernel-regression]] |
| 3.4 | Multicategory Classification, Ranking and Ordinal Regression | 24 | интегрировано: [[30_mathematics/kernel-methods/theorems/structured-margin-loss-bound]] |
| 3.5 | Applications of SVM Algorithms | 25 | интегрировано: примеры и диагностика в [[50_bridges/support-vector-margins-robust-ai|связь с ИИе]] |
| 4.1 | Margins and Empirical Risk | 26–27 | интегрировано: [[30_mathematics/kernel-methods/modules/03-margin-uniform-convergence]] |
| 4.2 | Uniform Convergence and Rademacher Averages | 27–28 | интегрировано: [[30_mathematics/kernel-methods/theorems/rademacher-uniform-convergence]], [[30_mathematics/kernel-methods/theorems/rkhs-rademacher-complexity]] |
| 4.3 | Upper Bounds and Convex Functions | 28 | интегрировано: [[30_mathematics/kernel-methods/theorems/surrogate-excess-risk-transfer]] |
| 4.4 | Rates of Convergence | 28 | интегрировано: [[30_mathematics/kernel-methods/theorems/margin-generalization-rate]] |
| 4.5 | Localization and Noise Conditions | 29 | интегрировано: [[20_concepts/tsybakov-noise-localization]] |
| 5.1.1 | Exponential Models | 29–30 | интегрировано: [[30_mathematics/kernel-methods/theorems/log-partition-moment-geometry]] и раздел 1 модуля [[30_mathematics/kernel-methods/modules/04-exponential-rkhs-statistical-models]] |
| 5.1.2 | Exponential RKHS Models | 30 | интегрировано: [[30_mathematics/kernel-methods/theorems/exponential-rkhs-density-universality]]; область применимости предложения 14 помечена для сверки |
| 5.1.3 | Conditional Exponential Models | 31 | интегрировано: [[30_mathematics/kernel-methods/methods/conditional-exponential-rkhs-model]] |
| 5.1.4 | Risk Functions for Model Fitting | 31–32 | интегрировано в [[30_mathematics/kernel-methods/methods/conditional-exponential-rkhs-model]]; вероятностная и отступная цели разделены |
| 5.1.5 | Generalized Representer Theorem and Dual Soft-Margin Formulation | 32–33 | существующая [[30_mathematics/kernel-methods/theorems/representer-theorem-kernel-expansion]] дополнена следствием 15; новая специфическая двойственность: [[30_mathematics/kernel-methods/theorems/structured-soft-margin-duality]] |
| 5.1.6 | Sparse Approximation | 33–34 | интегрировано: [[30_mathematics/kernel-methods/theorems/constraint-generation-epsilon-guarantee]] |
| 5.1.7 | Generalized Gaussian Processes Classification | 34–35 | интегрировано в [[30_mathematics/kernel-methods/methods/conditional-exponential-rkhs-model]] с явным различием апостериорной моды и байесовского интегрирования |
| 5.2.1 | Markov Networks and Factorization Theorem | 36 | интегрировано: [[30_mathematics/kernel-methods/theorems/hammersley-clifford-factorization]] и раздел 1 модуля [[30_mathematics/kernel-methods/modules/05-markov-networks-graph-compatible-kernels]] |
| 5.2.2 | Kernel Decomposition over Markov Networks | 36–37 | интегрировано: [[30_mathematics/kernel-methods/theorems/graph-compatible-kernel-decomposition]]; общая RKHS не дублируется |
| 5.2.3 | Clique-based Sparse Approximation | 37–38 | интегрировано: [[30_mathematics/kernel-methods/theorems/clique-representer-sparse-expansion]] как следствие общей теоремы о представителе |
| 5.2.4 | Probabilistic Inference | 38 | интегрировано: [[30_mathematics/kernel-methods/methods/graphical-kernel-probabilistic-inference]] и [[50_bridges/graphical-kernels-structured-inference]] |
| 6 | Kernel Methods for Unsupervised Learning | 38 | интегрировано: [[30_mathematics/kernel-methods/modules/06-unsupervised-kernel-methods]] |
| 6.1 | Kernel Principal Component Analysis | 39 | интегрировано: [[30_mathematics/kernel-methods/methods/kernel-pca-centered-gram]]; линейный PCA переиспользован через [[50_bridges/svd-pca-compression-lora]] |
| 6.2 | Canonical Correlation and Measures of Independence | 40 | интегрировано: [[30_mathematics/kernel-methods/methods/kernel-canonical-correlation]] с явной регуляризацией |
| 6.3 | Measures of Independence | 40–41 | интегрировано: [[30_mathematics/kernel-methods/theorems/rkhs-cross-covariance-independence]] и [[30_mathematics/kernel-methods/theorems/kernel-mean-embedding-mmd]]; HSIC и MMD разведены по постановкам |
| 6.4 | Kernel Dependency Estimation | 41 | интегрировано: [[30_mathematics/kernel-methods/methods/kernel-dependency-estimation-preimage]] |
| 7 | Conclusion | 41 | интегрировано в [[30_mathematics/kernel-methods/kernel-methods-map]] и [[50_bridges/kernel-independence-representation-learning]] без отдельного повторяющего узла |

Все подразделы 5.1, 5.2 и 6 имеют отдельное место в карте, даже когда несколько соседних подразделов объединены одной концептуальной заметкой. Библиография на последующих страницах используется для восстановления полных доказательств.
