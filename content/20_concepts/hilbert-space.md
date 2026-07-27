---
id: hilbert-space
title: "Гильбертово пространство"
aliases: ["Hilbert space"]
type: concept
status: canonical
publish: true
areas: [functional-analysis, geometry]
concepts: [inner-product, orthogonality, projection]
prerequisites: [banach-space]
ai_domains: [kernels, gaussian-processes, signal-processing]
source_refs:
  - id: boss-fa-2005
    pages: "37-39, 112-122"
    role: primary
level: intermediate
created: 2026-07-10
updated: 2026-07-27
---

# Гильбертово пространство

Гильбертово пространство — полное пространство со скалярным произведением. Норма определяется как $\|x\|=\sqrt{\langle x,x\rangle}$, поэтому вместе с длиной появляются углы, ортогональность и проекции.

## Геометрический смысл

Если $M$ — замкнутое линейное подпространство $H$, то каждый $x\in H$ единственным образом раскладывается как

$$
x=P_Mx+(x-P_Mx),\qquad x-P_Mx\perp M.
$$

Это бесконечномерная версия метода наименьших квадратов. Ортонормированный базис позволяет разложить $x=\sum_k\langle x,e_k\rangle e_k$, а равенство Парсеваля переводит норму в энергию коэффициентов.

## Граница применимости

Не всякая банахова норма задаётся скалярным произведением. Критерий — тождество параллелограмма:

$$
\|x+y\|^2+\|x-y\|^2=2\|x\|^2+2\|y\|^2.
$$

$L^p$ при $p\ne2$ обычно не гильбертово.

## Связь с AI

> [!info] established
> Метод наименьших квадратов, признаки Фурье, ядерные методы и гауссовские процессы используют гильбертову геометрию. RKHS делает вычислимым скалярное произведение в пространстве функций через ядерный трюк.

См. [[30_mathematics/functional-analysis/theorems/riesz-representation]], [[50_bridges/hilbert-rkhs]], [[20_concepts/adjoint-operator]].

