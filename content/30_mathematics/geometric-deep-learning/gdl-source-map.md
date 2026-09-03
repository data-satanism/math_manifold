---
id: gdl-source-map
title: "Карта источников: Геометрическое глубокое обучение"
aliases: ["Source map gdl"]
type: source
status: canonical
publish: true
areas: [differential-geometry, geometric-deep-learning, source-mapping]
concepts: [source-coverage, content-overlap]
prerequisites: [gdl-course-map]
ai_domains: [geometric-deep-learning, graph-ml, computer-vision, scientific-machine-learning]
source_refs:
  - id: gdl-protobook-2021
    pages: "PDF 1–160"
    role: primary
  - id: gdl-math-foundations-2025
    pages: "PDF 1–78"
    role: primary
  - id: deep-sets-2017
    pages: "PDF 1–29"
    role: primary
  - id: gin-2019
    pages: "PDF 1–17"
    role: primary
  - id: group-equivariant-cnn-2016
    pages: "PDF 1–12"
    role: primary
  - id: gauge-mesh-cnn-2021
    pages: "PDF 1–17"
    role: primary
  - id: equivariant-universal-approximation-2018
    pages: "PDF 1–64"
    role: primary
level: research
created: 2026-08-12
updated: 2026-09-03
---

# Карта источников: Геометрическое глубокое обучение

| № | Источник и страницы | Целевой модуль | Статус |
|---:|---|---|---|
| 1 | gdl-protobook-2021, PDF 9–33; gdl-math-foundations-2025, PDF 1–3 | [[30_mathematics/geometric-deep-learning/modules/gdl-01-high-dimensional-priors|Проклятие размерности и геометрические априорные ограничения]] | canonical |
| 2 | gdl-math-foundations-2025, PDF 10–19; gdl-protobook-2021, PDF 13–23 | [[30_mathematics/geometric-deep-learning/modules/gdl-02-groups-actions-symmetry|Группы, действия и симметрии данных]] | canonical |
| 3 | gdl-protobook-2021, PDF 16–23; gdl-math-foundations-2025, PDF 10–16 | [[30_mathematics/geometric-deep-learning/modules/gdl-03-orbits-stabilizers-quotients|Орбиты, стабилизаторы и фактор-пространства]] | canonical |
| 4 | gdl-protobook-2021, PDF 16–21; equivariant-universal-approximation-2018, PDF 2–18 | [[30_mathematics/geometric-deep-learning/modules/gdl-04-representations-invariance-equivariance|Представления, инвариантность и эквивариантность]] | canonical |
| 5 | group-equivariant-cnn-2016, PDF 4–10; gdl-protobook-2021, PDF 44–48, 73–81 | [[30_mathematics/geometric-deep-learning/modules/gdl-05-equivariant-operators-convolution|Эквивариантные операторы и групповая свёртка]] | canonical |
| 6 | gdl-math-foundations-2025, PDF 37–49; gdl-protobook-2021, PDF 48–60 | [[30_mathematics/geometric-deep-learning/modules/gdl-06-smooth-manifolds-tangent-bundles|Гладкие многообразия, касательные пространства и расслоения]] | canonical |
| 7 | gdl-protobook-2021, PDF 48–60; gdl-math-foundations-2025, PDF 41–49 | [[30_mathematics/geometric-deep-learning/modules/gdl-07-riemannian-metric-geodesics|Риманова метрика, геодезические и экспоненциальная карта]] | canonical |
| 8 | gdl-protobook-2021, PDF 60–65, 90–93; gauge-mesh-cnn-2021, PDF 2–10 | [[30_mathematics/geometric-deep-learning/modules/gdl-08-connections-gauges|Связности, параллельный перенос и калибровки]] | canonical |
| 9 | gdl-protobook-2021, PDF 35–39, 81–87; gdl-math-foundations-2025, PDF 55–76 | [[30_mathematics/geometric-deep-learning/modules/gdl-09-graphs-laplacian-spectra|Графы, лапласиан и спектральные сигналы]] | canonical |
| 10 | gin-2019, PDF 2–17; gdl-protobook-2021, PDF 81–90 | [[30_mathematics/geometric-deep-learning/modules/gdl-10-message-passing-expressivity|Передача сообщений, выразительность и предел 1-WL]] | canonical |
| 11 | gdl-protobook-2021, PDF 39–44, 72–81; group-equivariant-cnn-2016, PDF 1–6 | [[30_mathematics/geometric-deep-learning/modules/gdl-11-grids-cnn-equivariance|Решётки и CNN как трансляционно-эквивариантные модели]] | canonical |
| 12 | gdl-protobook-2021, PDF 44–72, 78–93; gauge-mesh-cnn-2021, PDF 2–13 | [[30_mathematics/geometric-deep-learning/modules/gdl-12-homogeneous-spaces-geometric-graphs|Однородные пространства и геометрические графы]] | canonical |
| 13 | gdl-protobook-2021, PDF 31–33, 106–118; gdl-math-foundations-2025, PDF 1–3, 65–76 | [[30_mathematics/geometric-deep-learning/modules/gdl-13-architecture-design-protocol|Единый протокол проектирования геометрической архитектуры]] | canonical |

## Полное покрытие подразделов

| Источник | Глава и все входящие подразделы | Страницы | Решение или целевые модули |
|---|---|---:|---|
| gdl-protobook-2021 | 1. Введение | PDF 8 | gdl-01-high-dimensional-priors |
| gdl-protobook-2021 | 2. Обучение в высокой размерности: 2.1 регулярность функций; 2.2 проклятие размерности | PDF 9–12 | gdl-01-high-dimensional-priors |
| gdl-protobook-2021 | 3. Геометрические априорные ограничения: 3.1 симметрии, представления и инвариантность; 3.2 изоморфизмы и автоморфизмы; 3.3 устойчивость к деформациям; 3.4 разделение масштабов; 3.5 общий проектный шаблон | PDF 13–33 | gdl-02-groups-actions-symmetry;gdl-04-representations-invariance-equivariance;gdl-13-architecture-design-protocol |
| gdl-protobook-2021 | 4. Геометрические домены: 4.1 графы и множества; 4.2 решётки; 4.3 группы и однородные пространства; 4.4 геодезические и многообразия; 4.5 калибровки и расслоения; 4.6 геометрические графы и сетки | PDF 34–71 | gdl-06-smooth-manifolds-tangent-bundles;gdl-08-connections-gauges;gdl-09-graphs-laplacian-spectra;gdl-12-homogeneous-spaces-geometric-graphs |
| gdl-protobook-2021 | 5. Модели GDL: 5.1 CNN; 5.2 G-CNN; 5.3 GNN; 5.4 Deep Sets, трансформеры и латентные графы; 5.5 эквивариантная передача сообщений; 5.6 внутренняя CNN на сетке; 5.7 RNN; 5.8 LSTM | PDF 72–105 | gdl-05-equivariant-operators-convolution;gdl-10-message-passing-expressivity;gdl-11-grids-cnn-equivariance;gdl-12-homogeneous-spaces-geometric-graphs |
| gdl-protobook-2021 | 6. Задачи и приложения | PDF 106–117 | gdl-13-architecture-design-protocol |
| gdl-protobook-2021 | 7. Исторический обзор | PDF 118–160 | reference-only |
| gdl-math-foundations-2025 | 1. Алгебраические структуры: 1.1 множества и отображения; 1.2 группы; 1.3 векторные пространства | PDF 4–19 | gdl-02-groups-actions-symmetry;gdl-04-representations-invariance-equivariance |
| gdl-math-foundations-2025 | 2. Геометрические и аналитические структуры: 2.1 нормы; 2.2 метрики; 2.3 скалярные произведения | PDF 20–25 | reference-only |
| gdl-math-foundations-2025 | 3. Векторный анализ: 3.1 гладкость; 3.2 скалярные и векторные поля; 3.3 производные; 3.4 интегралы; 3.5 дивергенция; 3.6 лапласиан; 3.7 градиентный спуск | PDF 26–36 | reference-only |
| gdl-math-foundations-2025 | 4. Топология и дифференциальная геометрия: 4.1 топология; 4.2 эквивалентности; 4.3 многообразия; 4.4 гипотеза многообразия | PDF 37–50 | gdl-06-smooth-manifolds-tangent-bundles;gdl-07-riemannian-metric-geodesics |
| gdl-math-foundations-2025 | 5. Функциональный анализ: 5.1 банаховы; 5.2 гильбертовы пространства; 5.3 операторы и функционалы | PDF 51–54 | reference-only |
| gdl-math-foundations-2025 | 6. Спектральная теория: 6.1 собственные функции; 6.2 анализ Фурье | PDF 55–64 | gdl-09-graphs-laplacian-spectra |
| gdl-math-foundations-2025 | 7. Теория графов: 7.1 определения; 7.2 группы и графы; 7.3 векторные поля на графах | PDF 65–78 | gdl-09-graphs-laplacian-spectra;gdl-10-message-passing-expressivity |
| deep-sets-2017 | 1–5. Введение; перестановочная инвариантность и эквивариантность; архитектура функций на множествах Deep Sets; приложения; выводы. Приложения A–I: доказательства, инвариантная и эквивариантная модели и эксперименты | PDF 1–29 | gdl-03-orbits-stabilizers-quotients;gdl-10-message-passing-expressivity |
| gin-2019 | 1–8. Введение; предварительные сведения; теоретическая схема; GIN; менее выразительные агрегаторы; связанные работы; эксперименты; выводы. Приложения A–I: доказательства лемм и теорем | PDF 1–17 | gdl-10-message-passing-expressivity |
| group-equivariant-cnn-2016 | 1–8. Введение; CNN; связанные работы; математическая схема; p4/p4m-свёртки; реализация; эксперименты; обсуждение | PDF 1–12 | gdl-05-equivariant-operators-convolution;gdl-11-grids-cnn-equivariance |
| gauge-mesh-cnn-2021 | 1–6. Введение; калибровки на сетках; калибровочно-эквивариантная свёртка; параллельный перенос и передача сообщений; эксперименты; обсуждение и приложения | PDF 1–17 | gdl-08-connections-gauges;gdl-12-homogeneous-spaces-geometric-graphs |
| equivariant-universal-approximation-2018 | 1. Введение: мотивация, связанные работы, вклад | PDF 2–6 | gdl-04-representations-invariance-equivariance |
| equivariant-universal-approximation-2018 | 2. Компактные группы: симметризация; полиномиальные инварианты; поляризация; симметрическая группа | PDF 6–18 | gdl-04-representations-invariance-equivariance |
| equivariant-universal-approximation-2018 | 3. Трансляции: конечные абелевы группы; непрерывные сигналы; агрегирование | PDF 18–32 | gdl-05-equivariant-operators-convolution;gdl-11-grids-cnn-equivariance |
| equivariant-universal-approximation-2018 | 4. Свёрточные сети с сохранением зарядов: поточечная эквивариантность; дифференцирование; дискретные операторы; SO(2)-модули; основная теорема | PDF 32–56 | gdl-12-homogeneous-spaces-geometric-graphs |
| equivariant-universal-approximation-2018 | 5. Обсуждение и приложение A | PDF 56–64 | reference-only |

## Правило покрытия

Каждый указанный диапазон проверяется в исходном PDF. Если соседние подразделы объединены, их границы остаются видимыми в этой таблице и в `source_refs` модуля. Совпадающее содержание расширяет существующий узел или получает ссылку `reference-only`; отдельное определение-дубликат не создаётся.
