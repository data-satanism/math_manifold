---
id: math-ai-home
title: "Math for AI — карта знаний"
aliases: ["Главная карта", "MathAI Knowledge"]
type: map
status: canonical
publish: true
areas: [mathematics, artificial-intelligence]
concepts: [abstraction, representation, operator, optimization]
prerequisites: []
ai_domains: [llm, computer-vision, time-series, model-compression, graph-ml, industrial-ai]
source_refs: []
level: foundation
created: 2026-07-10
updated: 2026-07-27
description: "Два входа в единую систему: через математические абстракции и через задачи AI."
tags: [map, math-for-ai]
---

# Math for AI — карта знаний

Эта база устроена не как полка с независимыми учебниками. Её основной объект — **математическая абстракция**, которая проявляется в нескольких областях и получает вычислительную реализацию в AI.

## Два входа

### От математики к приложениям

- [[10_maps/functional-analysis|Функциональный анализ]]
- [[30_mathematics/numerical-analysis/numerical-linear-algebra-map|Численный анализ и численная линейная алгебра]]
- [[30_mathematics/linear-algebra/boss-linear-algebra-map|Линейная алгебра: интеграционный маршрут по Боссу]]
- [[30_mathematics/random-matrix-theory/random-matrix-theory-map|Теория случайных матриц для машинного обучения]]
- [[30_mathematics/numerical-analysis/modules/19-unconstrained-optimization|Численная оптимизация]]

### От AI-задачи к математике

- Функции потерь и геометрия представлений → [[50_bridges/metrics-losses|Нормы и метрики]].
- Ядра и гауссовские процессы → [[50_bridges/hilbert-rkhs|Гильбертовы пространства и RKHS]].
- PCA, LoRA и спектральное отсечение → [[50_bridges/operators-spectrum|Операторы и спектр]].
- CNN и нейронные операторы → [[50_bridges/distributions-convolution|Обобщённые функции и свёртка]].
- Неявные слои и DEQ → [[50_bridges/frechet-fixed-points|Производная Фреше и неподвижные точки]].

## Как читать

1. Начните с карты области.
2. Перейдите к модулю курса, если нужен связный маршрут.
3. Откройте заметку о понятии, если нужен переиспользуемый объект.
4. В заметке о теореме проверяйте точные условия и доказательство.
5. В связующей заметке отделяйте строгий перенос от инженерной аналогии.

> [!note] Редакционный статус
> Публичная версия содержит только материалы со статусом `canonical`, явно одобренные владельцем. Новые расширения RMT и линейной алгебры проходят отдельное ревью и появятся здесь только после следующего утверждения.
