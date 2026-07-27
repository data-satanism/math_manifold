---
id: frechet-derivative
title: "Производная Фреше"
aliases: ["Fréchet derivative", "Frechet derivative"]
type: concept
status: canonical
publish: true
areas: [functional-analysis, optimization]
concepts: [linearization, jacobian]
prerequisites: [bounded-operator, banach-space]
ai_domains: [autodiff, implicit-models, optimization]
source_refs:
  - id: boss-fa-2005
    pages: "157-164"
    role: primary
level: advanced
created: 2026-07-10
updated: 2026-07-27
---

# Производная Фреше

Отображение $F:X\to Y$ между банаховыми пространствами дифференцируемо по Фреше в $x$, если существует ограниченный линейный оператор $DF(x)$, такой что

$$
\frac{\|F(x+h)-F(x)-DF(x)h\|_Y}{\|h\|_X}\to0.
$$

Это равномерная по направлениям локальная линейзация. Производная Гато проверяет отдельные направления и без дополнительных условий слабее.

## Правило цепочки

Если $F$ и $G$ дифференцируемы по Фреше, то

$$
D(G\circ F)(x)=DG(F(x))\circ DF(x).
$$

Именно композиционная структура делает производную естественным языком автоматического дифференцирования.

## Неявная функция

Если $F(x_0,y_0)=0$, производная по $x$ непрерывно обратима и производная меняется непрерывно, то локально существует функция $x(y)$, причём

$$
Dx(y_0)=-D_xF(x_0,y_0)^{-1}D_yF(x_0,y_0).
$$

## Связь с AI

> [!info] established
> Неявное дифференцирование обучает модели, заданные уравнением, без разворачивания всех итераций. Главный риск — несуществующая или плохо обусловленная обратная производная.

См. [[20_concepts/fixed-point]], [[50_bridges/frechet-fixed-points]].

