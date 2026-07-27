---
id: galerkin-finite-elements-method
title: "Метод Галёркина и конечных элементов"
aliases: ["Галёркинская дискретизация", "МКЭ"]
type: method
status: canonical
publish: true
areas: [numerical-analysis, partial-differential-equations]
concepts: [weak-form, trial-space, test-space, finite-elements, residual-orthogonality]
prerequisites: [nla-23-operator-equations-fem-galerkin]
ai_domains: [neural-operators, scientific-machine-learning]
source_refs:
  - id: tyrtyshnikov-numerical-analysis
    pages: "227-231"
    role: primary
level: advanced
created: 2026-07-15
updated: 2026-07-27
---

# Метод Галёркина и конечных элементов

## Идея

Выбрать конечномерное пространство $V_h\subset V$ и найти $u_h\in V_h$ из условия

$$
a(u_h,v_h)=\ell(v_h)\qquad\forall v_h\in V_h.
$$

Невязка ортогональна тестовому пространству, а локальный базис превращает задачу в разреженную систему.

## Алгоритм

1. Вывести слабую форму и встроить существенные граничные условия в $V$.
2. Построить сетку и локальные базисные функции $\varphi_j$.
3. Собрать матрицу $K_{ij}=a(\varphi_j,\varphi_i)$ и вектор $b_i=\ell(\varphi_i)$.
4. Решить $K\alpha=b$.
5. Восстановить $u_h=\sum_j\alpha_j\varphi_j$.
6. Проверить невязку и устойчивость, затем уточнить сетку.

## Режимы отказа

- неверная слабая форма меняет знак или граничные члены;
- плохая сетка ухудшает аппроксимацию и обусловленность;
- несогласованные пробное и тестовое пространства создают неустойчивость;
- малая алгебраическая невязка не равна малой дискретизационной ошибке.

## Перенос в ИИ

**Аналогия.** Обучаемая система может предлагать базис, сетку или начальное приближение, но галёркинская проверка должна оставаться вычислимой независимо.

## Визуализация

![Слабая форма и проекция на локальный базис конечных элементов](80_assets/numerical-analysis/gpt-image-v5/nla-ch22-operator-galerkin-insight.png)

## Источник

[[60_sources/tyrtyshnikov-numerical-analysis|Тыртышников]], §22.1–22.5, стр. 227–231.

