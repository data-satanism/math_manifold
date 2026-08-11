---
id: ai-domain-scientific-industrial-ai
title: "Научный и промышленный ИИ: математическая карта"
aliases: ["Математика Scientific ML", "Scientific and industrial AI map"]
type: map
status: canonical
publish: true
areas: [artificial-intelligence, scientific-machine-learning, industrial-ai, knowledge-navigation]
concepts: [operator-equations, invariants, inverse-problems, numerical-stability]
prerequisites: [mathematics-integration-map]
ai_domains: [scientific-machine-learning, industrial-ai, neural-operators, control]
source_refs: []
level: advanced
created: 2026-07-27
updated: 2026-08-12
description: "Маршрут от физических законов и операторных уравнений к проверяемым научным системам машинного обучения."
---

# Научный и промышленный ИИ: математическая карта

## 1. Закон до модели

- [[50_bridges/field-invariants-physics-informed-models|Инварианты полей и физически информированные модели]] отделяет закон сохранения от штрафа в функции потерь.
- [[50_bridges/variational-principles-energy-models|Вариационные принципы и энергетические модели]] показывает, когда решение характеризуется минимумом функционала.
- [[30_mathematics/applied-mathematics/modules/06-calculus-of-variations|Вариационное исчисление]] даёт строгую основу.

## 2. Операторная постановка

- [[50_bridges/operator-equations|Операторные уравнения и обратные задачи]].
- [[50_bridges/integral-equations-attention-neural-operators|Интегральные уравнения и нейронные операторы]].
- [[50_bridges/galerkin-neural-operators|Метод Галёркина и нейронные операторы]].

**Установленный результат:** устойчивость дискретизации можно анализировать через аппроксимацию, согласованность и устойчивость.
**Аналогия:** обучаемый оператор можно рассматривать как адаптивное пространство приближения.
**Граница:** малая ошибка на сетке не доказывает сходимость при смене разрешения или геометрии.

## 3. Управление и динамика

- [[50_bridges/matrix-equations-control-learning|Матричные уравнения, управление и обучение]].
- [[50_bridges/laplace-state-space-learning|Преобразование Лапласа и модели пространства состояний]].
- [[50_bridges/dynamical-systems-recurrent-models|Динамические системы и рекуррентные модели]].

## 4. Численная проверяемость

- [[50_bridges/backward-stability-mixed-precision|Обратная устойчивость]].
- [[50_bridges/preconditioning-ml-optimization|Предобусловливание и оптимизация]].
- [[50_bridges/multigrid-multiscale-learning|Многосеточные методы и многомасштабное обучение]].
- [[50_bridges/gaussian-quadrature-expectations|Квадратуры и математические ожидания]].

## Минимальный протокол верификации

1. Записать пространство входов и выходов оператора.
2. Указать физические размерности и инварианты.
3. Отделить ошибку данных, аппроксимации, оптимизации и вычисления.
4. Проверить остаток уравнения и устойчивость к смене сетки.
5. Проверить экстраполяцию только в явно заданном диапазоне параметров.

## Режимы отказа

- неверная размерность или масштаб переменных;
- неидентифицируемая обратная задача;
- нарушение закона сохранения вне обучающей сетки;
- хорошая средняя ошибка при недопустимом локальном остатке;
- численная неустойчивость, маскируемая качеством на одной выборке.
