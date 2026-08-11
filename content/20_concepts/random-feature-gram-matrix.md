---
id: random-feature-gram-matrix
title: "Матрица Грама случайных признаков"
aliases: ["Random feature Gram matrix", "Грамова матрица случайного слоя"]
type: concept
status: canonical
publish: true
areas: [random-matrix-theory, random-features, kernel-methods]
concepts: [effective-kernel, deterministic-equivalent, random-feature-map]
prerequisites: [positive-definite-kernel, deterministic-equivalent]
ai_domains: [random-features, regression, neural-networks, kernels]
source_refs:
  - id: rmt4ml-2022
    pages: "299-317"
    role: primary
  - id: louart2018randomnn
    pages: "1-53"
    role: primary
level: advanced
created: 2026-07-30
updated: 2026-08-12
---

# Матрица Грама случайных признаков

## Определение

Для данных $X=[x_1,\ldots,x_n]\in\mathbb R^{p\times n}$, случайных весов $W\in\mathbb R^{N\times p}$ и активации $\sigma$ определим

$$
\Sigma=\sigma(WX)\in\mathbb R^{N\times n},
\qquad
G=\frac1n\Sigma^T\Sigma.
$$

Элемент $G_{ij}$ измеряет сходство объектов после одного случайного нелинейного слоя.

## Два предела

При $N\to\infty$ и фиксированных $n,p$ закон больших чисел приводит к ядру

$$
K_{ij}=\mathbb E_w[\sigma(w^Tx_i)\sigma(w^Tx_j)].
$$

В пропорциональном режиме $n,p,N\to\infty$ случайность конечного числа признаков остаётся первого порядка. Тогда требуется RMT-эквивалент резольвенты $G$, а эффективное ядро зависит от отношения $N/n$ и регуляризации.

## Геометрический смысл

Матрица Грама не хранит координаты признаков по отдельности. Она хранит все попарные скалярные произведения и тем самым определяет геометрию выборки в случайном признаковом пространстве.

## Вычислительная форма

Для гребневой регрессии вычисляют

$$
(G+\gamma I)^{-1},
$$

а детерминированный эквивалент заменяет многократную генерацию $W$ фиксированной точкой для эффективного ядра.

## Перенос в ИИ

**Установлено.** Теория описывает однослойные сети со случайными замороженными весами в совместном пределе размерностей.

**Аналогия.** Каждый случайный нейрон — отдельный датчик; матрица Грама объединяет их измерения в устойчивую карту сходства.

**Граница переноса.** После обучения $W$ или добавления глубины независимость датчиков исчезает, и исходная теорема больше не применима напрямую.

## Источники

- [[60_sources/rmt4ml-couillet-liao|RMT4ML]], стр. 299–317.
- [[60_sources/louart-liao-couillet-random-neural-networks|Louart, Liao, Couillet]], стр. 1–53.
