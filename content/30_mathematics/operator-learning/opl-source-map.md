---
id: opl-source-map
title: "Карта источников: Уравнения в частных производных, обратные задачи и операторное обучение"
aliases: ["Source map opl"]
type: source
status: canonical
publish: true
areas: [partial-differential-equations, inverse-problems, operator-learning, source-mapping]
concepts: [source-coverage, content-overlap]
prerequisites: [opl-course-map]
ai_domains: [scientific-machine-learning, neural-operators, inverse-problems]
source_refs:
  - id: neural-operator-2021
    pages: "PDF 1–97"
    role: primary
  - id: fourier-neural-operator-2021
    pages: "PDF 1–16"
    role: primary
  - id: deeponet-2019
    pages: "PDF 1–22"
    role: primary
level: research
created: 2026-08-12
updated: 2026-08-12
---

# Карта источников: Уравнения в частных производных, обратные задачи и операторное обучение

| № | Источник и страницы | Целевой модуль | Статус |
|---:|---|---|---|
| 1 | neural-operator-2021, PDF 1–9, 30–35 | [[30_mathematics/operator-learning/modules/opl-01-pde-solution-operators|Уравнения в частных производных и операторы решений]] | canonical |
| 2 | neural-operator-2021, PDF 6–12, 47–53 | [[30_mathematics/operator-learning/modules/opl-02-weak-variational-formulations|Слабые и вариационные постановки]] | canonical |
| 3 | neural-operator-2021, PDF 30–35, 40–45; fourier-neural-operator-2021, PDF 8–10 | [[30_mathematics/operator-learning/modules/opl-03-inverse-problems-regularization|Обратные задачи и регуляризация]] | canonical |
| 4 | deeponet-2019, PDF 1–5, 18–21; neural-operator-2021, PDF 24–27 | [[30_mathematics/operator-learning/modules/opl-04-deeponet-branch-trunk|DeepONet и разложение branch–trunk]] | canonical |
| 5 | fourier-neural-operator-2021, PDF 3–10, 13–15; neural-operator-2021, PDF 21–24, 38–44 | [[30_mathematics/operator-learning/modules/opl-05-fourier-neural-operator|Фурье-нейронный оператор и спектральные ядра]] | canonical |
| 6 | neural-operator-2021, PDF 8–24, 47–53 | [[30_mathematics/operator-learning/modules/opl-06-discretization-invariance|Инвариантность к дискретизации и сходимость сеток]] | canonical |
| 7 | neural-operator-2021, PDF 30–35, 45–53 | [[30_mathematics/operator-learning/modules/opl-07-losses-sobolev-physics|Нормы ошибок, соболевские потери и физические ограничения]] | canonical |
| 8 | neural-operator-2021, PDF 35–46, 53–59; fourier-neural-operator-2021, PDF 6–10 | [[30_mathematics/operator-learning/modules/opl-08-validation-generalization|Валидация операторов и перенос между физическими режимами]] | canonical |

## Полное покрытие подразделов

| Источник | Глава и все входящие подразделы | Страницы | Решение или целевые модули |
|---|---|---:|---|
| neural-operator-2021 | Введение: подход, контекст | PDF 1–6 | opl-01-pde-solution-operators |
| neural-operator-2021 | Learning operators: parametric PDE, постановка, дискретизация | PDF 6–9 | opl-01-pde-solution-operators;opl-06-discretization-invariance |
| neural-operator-2021 | Нейронные операторы: параметризация и вычисление; GNO, LNO, MGNO, FNO | PDF 9–24 | opl-04-deeponet-branch-trunk;opl-05-fourier-neural-operator |
| neural-operator-2021 | Связь с DeepONet и Transformers | PDF 24–30 | opl-04-deeponet-branch-trunk |
| neural-operator-2021 | Тестовые задачи: Poisson, Darcy, Burgers, Navier–Stokes, inverse problem, spectra, loss criteria | PDF 30–35 | opl-01-pde-solution-operators;opl-03-inverse-problems-regularization;opl-07-losses-sobolev-physics |
| neural-operator-2021 | Численные результаты: Poisson, Darcy/Burgers, Navier–Stokes, super-resolution, spectral analysis, boundary conditions, inverse problem, comparison | PDF 35–47 | opl-05-fourier-neural-operator;opl-08-validation-generalization |
| neural-operator-2021 | Теория аппроксимации: neural operators, discretization invariance, approximation theorems | PDF 47–53 | opl-02-weak-variational-formulations;opl-06-discretization-invariance |
| neural-operator-2021 | Обзор литературы, выводы и направления | PDF 53–59 | opl-08-validation-generalization |
| neural-operator-2021 | Приложения и дополнительные результаты | PDF 60–97 | reference-only |
| fourier-neural-operator-2021 | 1–3. Введение; learning operators; neural operator | PDF 1–5 | opl-01-pde-solution-operators |
| fourier-neural-operator-2021 | 4. Fourier Neural Operator | PDF 5–6 | opl-05-fourier-neural-operator |
| fourier-neural-operator-2021 | 5. Эксперименты: Burgers, Darcy, Navier–Stokes, super-resolution, Bayesian inverse problem | PDF 6–10 | opl-03-inverse-problems-regularization;opl-05-fourier-neural-operator;opl-08-validation-generalization |
| fourier-neural-operator-2021 | 6. Обсуждение и выводы | PDF 9–13 | opl-08-validation-generalization |
| fourier-neural-operator-2021 | A. Нотация, spectral analysis, data generation и дополнительные результаты | PDF 13–16 | opl-05-fourier-neural-operator |
| deeponet-2019 | 1. Введение и operator universal approximation | PDF 1–4 | opl-04-deeponet-branch-trunk |
| deeponet-2019 | 2. Методология: DeepONet и генерация данных | PDF 4–5 | opl-04-deeponet-branch-trunk |
| deeponet-2019 | 3. Число сенсоров | PDF 5–6 | opl-04-deeponet-branch-trunk |
| deeponet-2019 | 4. Эксперименты: линейная/нелинейная динамика, маятник, diffusion–reaction | PDF 6–15 | opl-04-deeponet-branch-trunk |
| deeponet-2019 | 5–6. Выводы и благодарности | PDF 15–18 | reference-only |
| deeponet-2019 | A–C. Теорема операторной аппроксимации, число сенсоров, Gaussian random field | PDF 18–22 | opl-04-deeponet-branch-trunk |

## Правило покрытия

Каждый указанный диапазон проверяется в исходном PDF. Если соседние подразделы объединены, их границы остаются видимыми в этой таблице и в `source_refs` модуля. Совпадающее содержание расширяет существующий узел или получает ссылку `reference-only`; отдельное определение-дубликат не создаётся.
