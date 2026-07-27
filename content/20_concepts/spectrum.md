---
id: spectrum
title: "Спектр оператора"
aliases: ["Spectrum", "Спектральный радиус"]
type: concept
status: canonical
publish: true
areas: [functional-analysis, spectral-theory]
concepts: [resolvent, eigenvalue, spectral-radius]
prerequisites: [bounded-operator]
ai_domains: [model-compression, graph-ml, optimization]
source_refs:
  - id: boss-fa-2005
    pages: "144-156"
    role: primary
level: advanced
created: 2026-07-10
updated: 2026-07-27
---

# Спектр оператора

Для ограниченного оператора $A$ на комплексном банаховом пространстве спектр

$$
\sigma(A)=\{\lambda\in\mathbb C: A-\lambda I\text{ не имеет ограниченной обратной}\}.
$$

Собственные значения входят в спектр, но не исчерпывают его. У оператора умножения $(Af)(t)=tf(t)$ на $L^2[0,1]$ спектр равен $[0,1]$, хотя собственных значений может не быть.

## Резольвента и радиус

Резольвента $R(\lambda,A)=(A-\lambda I)^{-1}$ описывает чувствительность обратной задачи. Спектральный радиус

$$
r(A)=\sup_{\lambda\in\sigma(A)}|\lambda|=\lim_{n\to\infty}\|A^n\|^{1/n}.
$$

Для не-нормального оператора большая резольвента может возникать далеко от спектра; одного спектра недостаточно для переходной динамики.

## Компактный случай

Ненулевая часть спектра компактного оператора состоит из собственных значений конечной кратности, которые могут накапливаться только у нуля. Для самосопряжённого компактного оператора получается ортонормальное разложение.

## Связь с AI

> [!info] established with caveat
> Спектр матриц весов, матрицы Гессе и ядерных матриц используется для сжатия и диагностики. Перенос спектральной интуиции на нелинейную сеть требует указать конкретный линейный оператор: якобиан, матрицу Гессе, ковариацию или отображение внимания.

См. [[50_bridges/operators-spectrum]], [[30_mathematics/functional-analysis/theorems/spectral-compact-selfadjoint]].

