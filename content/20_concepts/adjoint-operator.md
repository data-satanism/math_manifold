---
id: adjoint-operator
title: "Сопряжённый оператор"
aliases: ["Adjoint operator", "Сопряжение"]
type: concept
status: canonical
publish: true
areas: [functional-analysis, linear-algebra]
concepts: [duality, inner-product]
prerequisites: [bounded-operator, hilbert-space]
ai_domains: [autodiff, inverse-problems, signal-processing]
source_refs:
  - id: boss-fa-2005
    pages: "92-96, 119-122"
    role: primary
  - id: myshkis-applied-mathematics-engineers-2006
    pages: "186-194"
    role: supporting
  - id: boss-linear-algebra-2005
    pages: "94-97"
    role: supporting
level: advanced
created: 2026-07-10
updated: 2026-07-27
---

# Сопряжённый оператор

Для $A:X\to Y$ банахов сопряжённый оператор $A^*:Y^*\to X^*$ задаётся правилом

$$
(A^*f)(x)=f(Ax).
$$

В гильбертовых пространствах после представления Рисса это превращается в знакомое равенство

$$
\langle Ax,y\rangle_Y=\langle x,A^*y\rangle_X.
$$

## Почему это больше транспонирования

Для матрицы в евклидовом базисе $A^*$ — сопряжённое транспонирование. Для дифференциального оператора сопряжение связано с интегрированием по частям и граничными условиями. Изменение внутреннего произведения меняет формулу сопряжённого оператора.

## Самосопряжённость

Оператор $A=A^*$ имеет действительный спектр. Компактный самосопряжённый оператор допускает ортонормальное спектральное разложение — бесконечномерный аналог симметричной матрицы.

В конечномерном случае есть полезный механизм разложения: если $L$ инвариантно относительно самосопряжённого $A$, то $L^\perp$ также инвариантно, поскольку $\langle Ax,y\rangle=\langle x,Ay\rangle=0$ для $x\in L^\perp$, $y\in L$. Этот шаг связывает конечномерную геометрию Мышкиса с общей спектральной теорией, не создавая второго определения сопряжения.

## Связь с ИИ

> [!info] established
> Обратное автоматическое дифференцирование распространяет ковекторы через обратное протягивание, то есть через операцию, родственную сопряжению производной. Формула зависит от выбранных спариваний и не всегда равна простому транспонированию матрицы.

См. [[30_mathematics/functional-analysis/theorems/riesz-representation]], [[30_mathematics/functional-analysis/theorems/spectral-compact-selfadjoint]], [[30_mathematics/linear-algebra/modules/04-quadratic-forms-canonical-structure]], [[50_bridges/frechet-fixed-points]].
