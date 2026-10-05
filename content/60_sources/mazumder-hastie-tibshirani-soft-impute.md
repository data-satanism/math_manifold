---
id: source-mazumder-hastie-tibshirani-soft-impute
title: "Mazumder–Hastie–Tibshirani: спектральная регуляризация и SOFT-IMPUTE"
aliases: ["SOFT-IMPUTE", "Spectral Regularization Algorithms for Learning Large Incomplete Matrices"]
type: source
status: canonical
publish: true
areas: [big-data-algorithms, low-rank-methods, optimization]
concepts: [matrix-completion, nuclear-norm, singular-value-decomposition]
prerequisites: [nla-02-unitary-matrices-and-svd]
ai_domains: [matrix-factorization, recommender-systems]
source_refs:
  - id: mazumder-hastie-tibshirani-soft-impute-2010
    pages: "PDF 5–7; печатные с. 2291–2293; Lemma 1, Algorithm 1, Lemma 2"
    role: primary
level: advanced
created: 2026-10-02
updated: 2026-10-02
---

# Mazumder–Hastie–Tibshirani: спектральная регуляризация и SOFT-IMPUTE

Rahul Mazumder, Trevor Hastie, Robert Tibshirani. *Spectral Regularization Algorithms for Learning Large Incomplete Matrices*. JMLR 11(80), 2287–2322, 2010. [Официальная карточка и PDF](https://jmlr.org/papers/v11/mazumder10a.html).

Проверенный PDF содержит 36 физических страниц. SHA-256 приватной копии закрытом архиве: `86e08b09025411e0e287c5699812caa3158e2f8901bc1d2f036584061a2816dd`. Физическая PDF-страница 5 соответствует печатной странице 2291.

На PDF 5–7 визуально проверены Lemma 1, Algorithm 1 и Lemma 2: мягкое пороговое преобразование сингулярных чисел, итеративное заполнение текущими предсказаниями и уменьшение регуляризованной цели. [[30_mathematics/big-data-algorithms/modules/bda-05-matrix-completion|Пятый модуль]] использует эту опору и выписывает собственный вывод шага для квадратичной ошибки на наблюдаемых элементах с ядерным штрафом.

Мягкое пороговое преобразование не следует отождествлять с жёстким усечением до заданного ранга. Уменьшение обучающей цели не доказывает точного заполнения неизвестных элементов или статистического качества рекомендаций. Измерения скорости из статьи относятся к её реализации и экспериментальным условиям; они не являются измерениями нынешней лаборатории.
