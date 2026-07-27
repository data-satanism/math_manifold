---
id: thm-schauder-fixed-point
title: "Принцип неподвижной точки Шаудера"
aliases: ["Schauder fixed-point theorem"]
type: theorem
status: canonical
publish: true
areas: [functional-analysis, nonlinear-analysis]
concepts: [compactness, fixed-point, convexity]
prerequisites: [compactness, banach-space, brouwer-fixed-point]
ai_domains: [implicit-models, pde]
source_refs:
  - id: boss-fa-2005
    pages: "164-165"
    role: primary
level: advanced
created: 2026-07-10
updated: 2026-07-27
---

# Принцип неподвижной точки Шаудера

## Формулировка

Пусть $C$ — непустое замкнутое выпуклое подмножество банахова пространства, а $T:C\to C$ непрерывно и $T(C)$ относительно компактно. Тогда $T$ имеет неподвижную точку.

Эквивалентная частая форма: непрерывное отображение компактного выпуклого множества в себя имеет неподвижная точка.

## Идея доказательства

1. Компактное замыкание $K=\overline{T(C)}$ для каждого $\varepsilon>0$ покрывается конечным числом шаров с центрами $y_1,\ldots,y_m\in K$.
2. Строится непрерывная «почти проекция» $P_\varepsilon:K\to\operatorname{conv}\{y_1,\ldots,y_m\}$ с помощью нормированных весов, зависящих от расстояний до центров. Она удовлетворяет $\|P_\varepsilon y-y\|\lesssim\varepsilon$.
3. Конечномерное выпуклое множество $C_\varepsilon=\operatorname{conv}\{y_i\}$ компактно. Отображение $P_\varepsilon T:C_\varepsilon\to C_\varepsilon$ имеет неподвижную точку $x_\varepsilon$ по теореме Брауэра.
4. Тогда $\|x_\varepsilon-Tx_\varepsilon\|\lesssim\varepsilon$.
5. Для последовательности $\varepsilon_n\to0$ точки $Tx_{\varepsilon_n}$ лежат в относительно компактном множестве, поэтому имеют сходящуюся подпоследовательность. Близость $x_{\varepsilon_n}$ к $Tx_{\varepsilon_n}$ даёт тот же предел $x^*$.
6. Непрерывность $T$ приводит к $Tx^*=x^*$.

## Отличие от Банаха

Шаудер даёт существование, но не единственность и не сходимость итерации $x_{n+1}=Tx_n$. Компактность заменяет сжатие, но алгоритмическая цена высока.

## Связь с AI

> [!info] research-facing use
> Теорема применима к анализу существования нелинейных операторных моделей. Использовать её как обоснование конкретного решателя нельзя без отдельной схемы аппроксимации и устойчивости.

## Визуальная схема

![Научная схема с интуитивным образом и переносом в ИИ: schauder-fixed-point](80_assets/theorems/gpt-image-v2/schauder-fixed-point-insight.png)

> Схема выполнена в стиле научной векторной фигуры; акцентом отмечен ключевой переход утверждения.
