---
id: lab-tensors-matrix-equations-prompts-v1
title: "Реестр запросов GPT.Image: тензоры и матричные уравнения"
aliases: ["Промты для тензоров и уравнений Сильвестра"]
type: lab
status: canonical
publish: true
areas: [tensor-analysis, matrix-analysis, visualization]
concepts: [scientific-figure, tensor-covariance, sylvester-equation, lyapunov-equation]
prerequisites: [apm-05-tensor-calculus, linear-algebra-07-matrix-equations]
ai_domains: [scientific-communication, geometric-deep-learning, implicit-layers]
source_refs:
  - id: myshkis-applied-mathematics-engineers-2006
    pages: "252-280"
    role: visual-grounding
  - id: boss-linear-algebra-2005
    pages: "140-146"
    role: visual-grounding
level: advanced
created: 2026-07-17
updated: 2026-07-27
---

# Реестр запросов GPT.Image: тензоры и матричные уравнения

## Неизменяемая стилевая часть

> ICML-style scientific figure, clean academic vector infographic, white background, muted blue-gray palette with one accent color, minimal typography, precise arrows, thin lines, labeled panels, no photorealism, no 3D glossy rendering, no decorative background, conference-paper figure aesthetics, mathematically clean, visually balanced.

## Содержательные части

### `tensor-calculus-coordinate-covariance-insight.png`

Четыре панели: один геометрический объект в декартовой и криволинейной системах; закон преобразования верхних и нижних индексов; ковариантное сравнение векторов на поверхности; одна молекула в двух локальных рамках и эквивариантный слой. Итоговый образ: «меняем описание, а не математический объект».

### `covariant-derivative-tensoriality-insight.png`

Четыре панели: постоянное поле в декартовых и полярных координатах; компенсация изменения компонент изменением базиса; коммутативная диаграмма двух координатных карт; перенос векторов соседей перед агрегацией на графе. Итоговый образ: связность отделяет реальное изменение от движения координат.

### `tensors-geometric-deep-learning-insight.png`

Четыре панели: карта и местность; точный эквивариантный контракт; энергия и силы повёрнутой молекулы; ошибки при смешении каналов, локальных рамок и псевдовекторов. Итоговый образ: эквивариантность — проверяемое равенство, а не дополнение данных.

### `matrix-equations-kronecker-lyapunov-insight.png`

Четыре панели: двустороннее действие $A$ и $B$ на матрицу; векторизация и кронекерова сумма; таблица попарных спектральных сумм; эллипсоиды функции Ляпунова и структурированный решатель в неявном слое. Итоговый образ: векторизация кодирует структуру, но не требует строить её явно.

### `sylvester-equation-uniqueness-insight.png`

Четыре панели: две независимые динамики; матрица сумм $\lambda_i+\mu_j$; доказательство через формы Шура и обратную подстановку; разделённые частоты против резонанса и чувствительности. Итоговый образ: единственность определяется отсутствием спектрального резонанса.

### `matrix-equations-control-learning-insight-v2.png`

Четыре панели: квадратичный сертификат устойчивости с оговоркой о ненормальном переходном росте; стационарная ковариация с точным различием $\Sigma\ge0$ и $\Sigma>0$; неявный слой и сопряжённая задача; кронекерово приближение кривизны и проверка остатка. Версия 2 исправляет условие строгой положительности ковариации.

## Проверка качества

- формулы сверяются с содержательной заметкой;
- русский текст проверяется на читаемость и отсутствие смешанных фраз;
- каждый рисунок содержит математическое ядро, понятный образ и перенос в ИИ;
- неточная версия не заменяется на месте: создаётся новый версионированный файл;
- статический рисунок остаётся читаемым на ширине мобильного экрана после увеличения.
