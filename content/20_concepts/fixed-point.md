---
id: fixed-point
title: "Неподвижная точка"
aliases: ["Fixed point"]
type: concept
status: canonical
publish: true
areas: [functional-analysis, dynamical-systems]
concepts: [iteration, contraction]
prerequisites: [completeness]
ai_domains: [implicit-models, equilibrium-models, optimization]
source_refs:
  - id: boss-fa-2005
    pages: "161-165, 178-180"
    role: primary
level: intermediate
created: 2026-07-10
updated: 2026-07-27
---

# Неподвижная точка

Неподвижная точка отображения $T:X\to X$ удовлетворяет $T(x^*)=x^*$. Многие уравнения переписываются именно так, но существование, единственность и вычислимость — разные вопросы.

## Три режима

1. **Сжатие:** $d(Tx,Ty)\le qd(x,y)$, $q<1$. В полном пространстве существует единственная точка, а итерация сходится геометрически.
2. **Компактность:** непрерывное компактное отображение замкнутого выпуклого множества в себя имеет неподвижную точку по Шаудеру. Единственность и алгоритмическая сходимость не следуют.
3. **Порядок:** монотонные отображения полных решёток имеют экстремальные неподвижная точкаs по Биркгофу—Тарскому.

## Диагностика

Перед запуском итерации нужно различать:

- теорему существования;
- условие единственности;
- локальную/глобальную сходимость;
- скорость и численную устойчивость.

## Связь с AI

> [!info] established
> Модель глубокого равновесия задаёт скрытое состояние как $z^*=F_\theta(z^*,x)$. Контроль константы Липшица помогает существованию и решению, но слишком сильное сжатие может ограничить выразительность.

См. [[30_mathematics/functional-analysis/theorems/banach-fixed-point]], [[30_mathematics/functional-analysis/theorems/schauder-fixed-point]], [[50_bridges/frechet-fixed-points]].

