---
id: lie-groups-differential-geometry-map
title: "Группы Ли, теория представлений и дифференциальная геометрия"
aliases: ["Карта курса по геометрии симметрий"]
type: map
status: canonical
publish: true
areas: ["differential-geometry", "lie-theory", "representation-theory"]
concepts: ["smooth-manifold", "lie-group", "representation", "riemannian-geometry", "equivariance"]
prerequisites: ["topology-map", "linear-algebra-map", "harmonic-analysis-wavelets-map"]
ai_domains: ["geometric-deep-learning", "equivariant-learning", "scientific-machine-learning"]
source_refs:
  - id: knapp-stokes-whitney-2021
    pages: "1–79"
    role: primary
  - id: gallier-riemannian-manifolds-2011
    pages: "7–91"
    role: primary
  - id: kirillov-introduction-lie-groups-2008
    pages: "13–68"
    role: primary
  - id: vogan-frobenius-theorem-2020
    pages: "1–6"
    role: primary
  - id: gdl-protobook-2021
    pages: "13–118"
    role: bridge
  - id: gdl-math-foundations-2025
    pages: "37–78"
    role: bridge
level: research
created: 2026-08-31
updated: 2026-09-03
---
# Группы Ли, теория представлений и дифференциальная геометрия

## Назначение курса

Курс строит строгий фундамент под опубликованным маршрутом геометрического глубокого обучения. Он идёт от локальной геометрии многообразий к непрерывным симметриям, неприводимым представлениям, гармоническому анализу на компактных группах и проверяемому проектированию эквивариантной архитектуры.

## Маршрут из 12 модулей

1. [[30_mathematics/lie-groups-differential-geometry/modules/lg-01-smooth-manifolds-atlases|Гладкие многообразия, карты и подмногообразия]]
2. [[30_mathematics/lie-groups-differential-geometry/modules/lg-02-tangent-cotangent-differential|Касательные и кокасательные пространства, дифференциал и расслоения]]
3. [[30_mathematics/lie-groups-differential-geometry/modules/lg-03-vector-fields-flows-bracket|Векторные поля, потоки, скобка Ли и интегрируемость]]
4. [[30_mathematics/lie-groups-differential-geometry/modules/lg-04-differential-forms-stokes|Дифференциальные формы, внешний дифференциал и теорема Стокса]]
5. [[30_mathematics/lie-groups-differential-geometry/modules/lg-05-riemannian-metrics-connections|Риманова метрика, связность и параллельный перенос]]
6. [[30_mathematics/lie-groups-differential-geometry/modules/lg-06-geodesics-exponential-curvature|Геодезические, экспоненциальное отображение и кривизна]]
7. [[30_mathematics/lie-groups-differential-geometry/modules/lg-07-lie-groups-algebras|Группы Ли, алгебры Ли и инфинитезимальные симметрии]]
8. [[30_mathematics/lie-groups-differential-geometry/modules/lg-08-exponential-adjoint-bch|Экспонента, присоединённое действие и формула Бейкера—Кэмпбелла—Хаусдорфа]]
9. [[30_mathematics/lie-groups-differential-geometry/modules/lg-09-representations-schur-reducibility|Представления, неприводимость, лемма Шура и полная приводимость]]
10. [[30_mathematics/lie-groups-differential-geometry/modules/lg-10-haar-peter-weyl|Мера Хаара, ортогональность характеров и теорема Петера—Вейля]]
11. [[30_mathematics/lie-groups-differential-geometry/modules/lg-11-homogeneous-spaces-bundles-gauges|Однородные пространства, факторизация, расслоения и калибровки]]
12. [[30_mathematics/lie-groups-differential-geometry/modules/lg-12-equivariant-architecture-protocol|От симметрии и геометрии к эквивариантной архитектуре]]

## Новые самостоятельные теоремы

- [[30_mathematics/lie-groups-differential-geometry/theorems/regular-value-submanifold-theorem|Теорема о регулярном значении и подмногообразии уровня]]
- [[30_mathematics/lie-groups-differential-geometry/theorems/frobenius-integrability-theorem|Теорема Фробениуса об интегрируемости распределения]]
- [[30_mathematics/lie-groups-differential-geometry/theorems/levi-civita-existence-uniqueness|Теорема Леви—Чивиты о метрической связности]]
- [[30_mathematics/lie-groups-differential-geometry/theorems/geodesic-local-minimizing-theorem|Локальная минимальность геодезических в нормальной окрестности]]
- [[30_mathematics/lie-groups-differential-geometry/theorems/lie-homomorphism-differential-exponential|Дифференциал гомоморфизма групп Ли и согласование экспонент]]
- [[30_mathematics/lie-groups-differential-geometry/theorems/baker-campbell-hausdorff-local-theorem|Локальная формула Бейкера—Кэмпбелла—Хаусдорфа]]
- [[30_mathematics/lie-groups-differential-geometry/theorems/schur-lemma-complex-representations|Лемма Шура для комплексных неприводимых представлений]]
- [[30_mathematics/lie-groups-differential-geometry/theorems/compact-representation-complete-reducibility|Полная приводимость конечномерных представлений компактной группы]]
- [[30_mathematics/lie-groups-differential-geometry/theorems/haar-measure-compact-groups|Существование и единственность нормированной меры Хаара на компактной группе]]
- [[30_mathematics/lie-groups-differential-geometry/theorems/peter-weyl-compact-groups|Теорема Петера—Вейля для компактных групп]]
- [[30_mathematics/lie-groups-differential-geometry/theorems/lie-quotient-manifold-theorem|Теорема о гладкой структуре фактор-пространства $G/H$]]

## Переиспользованные узлы без дублирования

- [[30_mathematics/applied-mathematics/theorems/stokes-theorem|Теорема Стокса]].
- [[30_mathematics/applied-mathematics/theorems/covariant-derivative-tensoriality|Тензорность ковариантной производной]].
- [[30_mathematics/geometric-deep-learning/theorems/gdl-equivariant-composition|Композиция эквивариантных отображений]].

## Явные связи

- [[30_mathematics/geometric-deep-learning/gdl-map|Геометрическое глубокое обучение]] получает классические предпосылки.
- [[30_mathematics/harmonic-analysis-wavelets/harmonic-analysis-wavelets-map|Гармонический анализ]] продолжается теоремой Петера—Вейля.
- [[30_mathematics/topology/topology-map|Топология]] поставляет фактор-пространства, компактность и накрытия.
- [[50_bridges/lie-symmetry-geometry-ai|Симметрия и геометрия → эквивариантные архитектуры]] фиксирует границы переноса.

## Лабораторный маршрут

- [[70_labs/lie-groups-differential-geometry/lie-geometry-labs|Четыре воспроизводимых эксперимента]].

## Статус

Материалы утверждены владельцем 3 сентября 2026 года и включены в публичный выпуск со статусом `canonical` и `publish: true`.
