---
id: thm-uniform-boundedness
title: "Принцип равномерной ограниченности"
aliases: ["Banach-Steinhaus theorem", "Uniform boundedness principle"]
type: theorem
status: canonical
publish: true
areas: [functional-analysis]
concepts: [operator-family, pointwise-boundedness]
prerequisites: [banach-space, thm-baire-category]
ai_domains: [stability, numerical-analysis]
source_refs:
  - id: boss-fa-2005
    pages: "101-102"
    role: primary
level: advanced
created: 2026-07-10
updated: 2026-07-27
---

# Принцип равномерной ограниченности

## Формулировка

Пусть $X$ — банахово пространство, $Y$ — нормированное, а $\mathcal F\subset\mathcal L(X,Y)$. Если для каждого фиксированного $x\in X$

$$
\sup_{T\in\mathcal F}\|Tx\|<\infty,
$$

то нормы операторов ограничены равномерно:

$$
\sup_{T\in\mathcal F}\|T\|<\infty.
$$

## Доказательство

1. Определим замкнутые множества
   $$
   E_n=\{x\in X : \sup_{T\in\mathcal F}\|Tx\|\le n\}.
   $$
   Они замкнуты как пересечения прообразов замкнутых шаров.
2. Поточечная ограниченность означает $X=\cup_{n\ge1}E_n$.
3. По [[30_mathematics/functional-analysis/theorems/baire-category|теореме Бэра]] некоторое $E_N$ содержит шар $B(x_0,r)$.
4. Если $\|h\|<r$, то $x_0+h$ и $x_0$ лежат в $E_N$, поэтому
   $$
   \|Th\|\le\|T(x_0+h)\|+\|Tx_0\|\le2N.
   $$
5. Масштабируя $h=(r/2)u$ для $\|u\|\le1$, получаем $\|Tu\|\le4N/r$ для всех $T$. Значит, $\sup_T\|T\|\le4N/r$.

## Контрапозиция

Если нормы операторов неограничены, существует один $x$, на котором значения $\|Tx\|$ неограничены. «Плохое направление» не обязано быть очевидным и может зависеть от всего семейства.

## Связь с AI

> [!info] analogy with rigorous core
> Поточечная устойчивость каждого отдельного входа не даёт равномерной устойчивости без контроля операторных норм. Для нелинейных моделей нужно отдельно перейти к семейству производных или локальных линейзаций.

## Визуальная схема

![Научная схема с интуитивным образом и переносом в ИИ: uniform-boundedness](80_assets/theorems/gpt-image-v2/uniform-boundedness-insight.png)

> Схема выполнена в стиле научной векторной фигуры; акцентом отмечен ключевой переход утверждения.
