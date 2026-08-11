---
id: ai-domain-graph-machine-learning
title: "Графовое машинное обучение: математическая карта"
aliases: ["Математика графового обучения", "Graph machine learning map"]
type: map
status: canonical
publish: true
areas: [artificial-intelligence, graph-machine-learning, knowledge-navigation]
concepts: [graph-spectrum, positive-operators, kernels, community-detection]
prerequisites: [mathematics-integration-map]
ai_domains: [graph-ml, structured-prediction, representation-learning]
source_refs: []
level: advanced
created: 2026-07-27
updated: 2026-08-12
description: "Маршрут от матриц графа и положительных операторов к GNN и обнаружению сообществ."
---

# Графовое машинное обучение: математическая карта

## 1. Граф как оператор

Матрица смежности, лапласиан и матрица переходов действуют на сигналы в вершинах. Поэтому отправная точка — не визуальное изображение графа, а оператор и его инвариантные подпространства.

- [[50_bridges/operators-spectrum|Операторы и спектр]].
- [[30_mathematics/linear-algebra/modules/09-positive-stochastic-matrices|Положительные и стохастические матрицы]].
- [[30_mathematics/linear-algebra/theorems/perron-frobenius-theorem|Теорема Перрона—Фробениуса]].

## 2. Агрегирование сообщений

- [[50_bridges/positive-operators|Положительные операторы и монотонные модели]] объясняют сохранение конуса и стационарное направление.
- [[50_bridges/graphical-kernels-structured-inference|Графические ядра и структурный вывод]] связывают локальную факторизацию с глобальным предсказанием.
- [[50_bridges/linear-programming-structured-prediction|Линейное программирование и структурное предсказание]] показывает роль выпуклой релаксации.

## 3. Сигнал против шумового спектра

- [[30_mathematics/random-matrix-theory/modules/07-graph-spectra-community-detection|Спектры графов и обнаружение сообществ]].
- [[30_mathematics/random-matrix-theory/theorems/dense-sbm-spectral-transition|Спектральный переход в плотной стохастической блочной модели]].
- [[50_bridges/rmt-spectral-diagnostics|RMT и спектральная диагностика]].

**Установленный результат:** в заданной случайной модели существует порог отделения информативного собственного направления.
**Граница:** порог нельзя без проверки переносить на произвольный реальный граф с зависимыми рёбрами и тяжёлыми степенями.

## 4. Масштабирование вычислений

- [[50_bridges/krylov-hessian-vector-products|Подпространства Крылова]] дают матрично-свободную спектральную обработку.
- [[50_bridges/hierarchical-matrices-kernel-attention|Иерархические и ядровые приближения]] уменьшают стоимость глобальных взаимодействий.

## Контрольные вопросы

1. Какая матрица графа соответствует задаче и какой мерой она самосопряжённа?
2. Как отделяется информативный выброс от шумового спектра?
3. Не приводит ли повторное усреднение к вырождению представлений?
4. Какие свойства графа нарушают модель независимых рёбер?
