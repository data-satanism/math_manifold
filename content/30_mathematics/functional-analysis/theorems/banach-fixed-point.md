---
id: thm-banach-fixed-point
title: "Принцип сжимающих отображений Банаха"
aliases: ["Banach fixed-point theorem", "Contraction mapping theorem"]
type: theorem
status: canonical
publish: true
areas: [functional-analysis, dynamical-systems]
concepts: [fixed-point, contraction, completeness]
prerequisites: [complete-metric-space]
ai_domains: [implicit-models, numerical-analysis]
source_refs:
  - id: boss-fa-2005
    pages: "161-163"
    role: primary
level: intermediate
created: 2026-07-10
updated: 2026-07-27
---

# Принцип сжимающих отображений Банаха

## Формулировка

Пусть $(X,d)$ — непустое полное метрическое пространство и $T:X\to X$ — сжатие:

$$
d(Tx,Ty)\le qd(x,y),\qquad 0\le q<1.
$$

Тогда существует единственная неподвижная точка $x^*$, а итерации $x_{n+1}=Tx_n$ сходятся к ней из любой начальной точки. Более того,

$$
d(x_n,x^*)\le\frac{q^n}{1-q}d(x_1,x_0).
$$

## Доказательство

1. По сжатию $d(x_{n+1},x_n)\le q^nd(x_1,x_0)$.
2. Для $m>n$ треугольное неравенство даёт
   $$
   d(x_m,x_n)\le\sum_{k=n}^{m-1}q^kd(x_1,x_0)
   \le\frac{q^n}{1-q}d(x_1,x_0).
   $$
3. Правая часть стремится к нулю; $(x_n)$ фундаментальна.
4. По полноте $x_n\to x^*\in X$.
5. Сжатие непрерывно, поэтому $Tx^*=\lim Tx_n=\lim x_{n+1}=x^*$.
6. Если $y^*$ — другая неподвижная точка, то
   $$
   d(x^*,y^*)=d(Tx^*,Ty^*)\le qd(x^*,y^*),
   $$
   откуда расстояние равно нулю.

## Что ломается

- При $q=1$ возможны отсутствие неподвижная точка или неединственность.
- В неполном пространстве предел итераций может лежать вне $X$.
- Локальное сжатие гарантирует результат только внутри инвариантной окрестности.

## Связь с AI

> [!info] established
> DEQ и неявные слои используют решатели уравнения неподвижной точки. Оценка $q$ даёт скорость и устойчивость, но глобальное сжатие — сильное архитектурное ограничение.

## Визуальная схема

![Научная схема с интуитивным образом и переносом в ИИ: banach-fixed-point](80_assets/theorems/gpt-image-v2/banach-fixed-point-insight.png)

> Схема выполнена в стиле научной векторной фигуры; акцентом отмечен ключевой переход утверждения.
