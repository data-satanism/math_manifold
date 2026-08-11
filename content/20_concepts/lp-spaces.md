---
id: lp-spaces
title: "Пространства Lp"
aliases: ["Lp spaces", "L^p"]
type: concept
status: canonical
publish: true
areas: [functional-analysis, measure-theory]
concepts: [measure, norm, equivalence-class]
prerequisites: [lebesgue-integral]
ai_domains: [statistical-learning, robust-optimization]
source_refs:
  - id: boss-fa-2005
    pages: "52-65"
    role: primary
level: intermediate
created: 2026-07-10
updated: 2026-07-27
---

# Пространства $L^p$

Для $1\le p<\infty$

$$
L^p(\Omega)=\left\{f : \int_\Omega |f|^p\,d\mu<\infty\right\}/\sim,
\qquad \|f\|_p=\left(\int |f|^p d\mu\right)^{1/p},
$$

где $f\sim g$, если они равны почти всюду. Для $p=\infty$ используется существенный супремум.

## Почему это классы эквивалентности

Интеграл не замечает изменений на множестве меры ноль. Поэтому точечное значение функции в $L^p$ вообще не определено без выбора представителя. Это важно: операция вычисления значения $f\mapsto f(x_0)$ не является корректным функционалом на всём $L^p$.

## Геометрия

- $L^1$ чувствительно к массе ошибок и связано с устойчивой функцией потерь.
- $L^2$ — гильбертово пространство, допускает ортогональность.
- $L^\infty$ контролирует худшее существенное отклонение.
- При конечной мере включения между $L^p$ зависят от направления показателей и константы меры; на бесконечной мере простого общего включения нет.

## Связь с ИИ

> [!info] established
> Популяционный риск — интеграл функции потерь по распределению данных. Выбор $p$ меняет тип контроля: среднеквадратический, средний абсолютный или наихудшего случая.

См. [[20_concepts/convergence-modes]], [[50_bridges/lp-risk]].
