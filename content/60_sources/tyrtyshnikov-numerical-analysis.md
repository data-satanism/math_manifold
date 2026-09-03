---
id: source-tyrtyshnikov-numerical-analysis
title: "Тыртышников — Методы численного анализа"
aliases: ["Методы численного анализа Тыртышникова", "Курс Тыртышникова"]
type: source
status: canonical
publish: true
areas: [numerical-analysis, numerical-linear-algebra, approximation-theory]
concepts: [matrix-norm, conditioning, singular-value-decomposition, spectral-perturbation, floating-point, matrix-factorizations, subspace-iteration, qr-algorithm, interpolation, chebyshev-polynomials, splines, orthogonal-polynomials, quadrature, newton-method, optimization, krylov-subspace, gmres, conjugate-gradient, preconditioning, galerkin-method, multigrid, toeplitz-matrix, hierarchical-matrix, wavelet]
prerequisites: [linear-algebra, mathematical-analysis]
ai_domains: [optimization, model-compression, mixed-precision, representation-learning, spectral-diagnostics, surrogate-modeling, calibration, uncertainty-quantification, implicit-layers, gaussian-processes, second-order-methods, neural-operators, scientific-machine-learning, attention]
source_refs:
  - id: tyrtyshnikov-numerical-analysis
    pages: "3-278"
    role: primary
level: advanced
created: 2026-07-13
updated: 2026-09-03
---

# Тыртышников — Методы численного анализа

## Роль в курсе

Книга Е. Е. Тыртышникова служит первичным математическим источником для курса [[30_mathematics/numerical-analysis/numerical-linear-algebra-map|«Методы численного анализа для ИИ»]]. Текущее покрытие включает все главы 1–25: от норм, устойчивости и матричных разложений до аппроксимации, нелинейных и крыловских методов, операторных уравнений, многосеточных схем, структурированных матриц и вейвлетов.

Локальные конспекты глав 1–8 используются как источник интуиций и авторского голоса. Главы 9–25 восстановлены непосредственно по первичному PDF. Формулировки, условия теорем, границы разделов и номера страниц проверяются по визуальным рендерам книги. Локальный конспект с именем «Глава 4» используется только как источник интуиций для книжных глав 19–21.

## Паспорт локальной копии

- объём: 290 PDF-страниц;
- SHA-256: `FDB4EC127213BF8C49F72F2A9D7623D637C0D0EE9922B453A11F4598FF0876AD`;
- исходный файл скопирован без перемещения и изменения;
- технический текстовый слой некорректно кодирует часть кириллицы, поэтому формулы и номера результатов сверяются по визуальному рендеру страниц;
- для печатных страниц рассматриваемого издания физическая PDF-страница имеет смещение `+8`.

## Правила использования

1. PDF и извлечённый текст остаются в `_private` и не экспортируются.
2. Автоматическое извлечение используется только для навигации и чернового поиска.
3. Ни одна формула не становится `canonical` без визуальной сверки с соответствующей страницей.
4. В публичный репозиторий могут попасть только собственные объяснения, собственные иллюстрации и библиографическая карточка после утверждения пользователем.
5. Новые страницы глав 9–25 остаются в `review`, поскольку их математические формулировки требуют пользовательской проверки до `canonical`.

## Покрытие

Точное соответствие всех 254 подразделов глав 1–25 и целевых заметок хранится в [[30_mathematics/numerical-analysis/tyrtyshnikov-source-map|карте источника]]. Контрольные суммы исходных локальных файлов зафиксированы в административном снимке источников.
