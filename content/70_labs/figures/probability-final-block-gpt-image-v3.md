---
id: lab-probability-final-block-gpt-image-v3
title: "Промты GPT.Image: вероятность, главы 7–9, выпуск v3"
aliases: ["Probability figures v3", "Промты визуализаций вероятности 7–9"]
type: lab
status: canonical
publish: true
areas: [probability, scientific-visualization]
concepts: [visual-prompt, gaussian-width, chaining, matrix-deviation]
prerequisites: [probability-07-random-processes-gaussian-width, probability-08-chaining-empirical-processes, probability-09-matrix-deviations-sparse-recovery]
ai_domains: [statistical-learning, compressed-sensing, model-selection]
source_refs:
  - id: vershynin-hdp-2026
    pages: "195-299"
    role: primary
level: advanced
created: 2026-07-27
updated: 2026-08-12
---

# Промты GPT.Image: вероятность, главы 7–9, выпуск v3

## Неизменяемый префикс

> ICML-style scientific figure, clean academic vector infographic, white background, muted blue-gray palette with one accent color, minimal typography, precise arrows, thin lines, labeled panels, no photorealism, no 3D glossy rendering, no decorative background, conference-paper figure aesthetics, mathematically clean, visually balanced. Russian-first scientific labels; use English only for standard abbreviations. Clearly distinguish established result, analogy, research hypothesis, and failure mode.

## 1. Модуль 7

Файл: `probability-module-07-random-processes-gaussian-width-v3.png`.

A: процесс `X_t`, каноническая метрика приращений, супремум и гауссовская ширина `w(T)=E sup <g,t>`. B: один объект и его случайные тени; диаметр отделён от средней ширины. C: сфера, конечный каталог и разреженное множество имеют разные эффективные сложности; перенос к объёму измерений маркирован как установленный. Отказ: близость параметров не совпадает с близостью приращений.

## 2. Модуль 8

Файл: `probability-module-08-chaining-empirical-processes-v3.png`.

A: последовательность сетей `T_0,T_1,T_2`, цепочка приближений и сумма приращений. B: карта «страна → город → улица → дом». C: эмпирический процесс, фиксированный класс моделей и равномерный коридор. Отказ: класс расширяют после просмотра проверочных данных.

## 3. Модуль 9

Файл: `probability-module-09-matrix-deviations-sparse-recovery-v3.png`.

A: случайная матрица почти сохраняет длины на структурированном множестве `T`, цена `w(T)`. B: случайная плоскость проходит мимо узкого конуса альтернатив. C: разреженный сигнал и низкоранговая матрица, число измерений связано с эффективной сложностью. Отказ: неверная структура и анизотропный оператор.

## 4. Теорема Дадли

Файл: `dudley-integral-inequality-insight-v3.png`.

A: точные условия субгауссовских приращений и формула интеграла. B: цепочка сетей и телескопическая сумма. C: профиль `sqrt(log N(ε))`, площадь под кривой. D: неверная метрика и нецентрированный постоянный процесс.

## 5. VC-закон больших чисел

Файл: `vc-uniform-law-large-numbers-insight-v3.png`.

A: точная формула ожидаемого равномерного отклонения `≤ C sqrt(d/n)`. B: способность класса реализовать разметки на конечном наборе. C: фиксированный каталог гипотез и законный выбор после обучения. Отказ: класс всех конечных подмножеств запоминает выборку, эмпирическая доля 1, истинная 0.

## 6. Матричное отклонение

Файл: `matrix-deviation-inequality-insight-v3.png`.

A: независимые изотропные субгауссовские строки и точная ожидаемая граница через `K²γ(T)`. B: процесс `Z_x` и субгауссовские приращения. C: случайное измерение структурированного множества. Отказ: строки лежат только вдоль `e1`, направление `e2` полностью теряется.

## 7. Ширина и объём данных

Файл: `gaussian-width-sample-complexity-insight-v3.png`.

A: случайные тени сферы, конечного каталога и разреженного множества. B: понятная аналогия «средняя тень, не максимальный диаметр». C: локальное множество обновлений и ориентир `m ~ w(T)²`, установленное отделено от гипотезы. Отказ: глобальная ширина и адаптивная локализация.

## 8. Адаптивное обобщение

Файл: `empirical-processes-adaptive-generalization-insight-v3.png`.

A: равномерный коридор для заранее фиксированного класса. B: сертифицированный каталог режимов. C: дерево выбора архитектуры, порога и случайного запуска, журнал решений. Отказ: новая ветвь добавлена после просмотра теста.

## 9. Структурированное восстановление

Файл: `structured-recovery-low-rank-adaptation-insight-v3.png`.

A: условие `ker A ∩ D(K,x)={0}` и геометрия конуса. B: луч света и конус теней. C: разреженный вектор, низкоранговая матрица и локальная линейная аналогия LoRA; гипотеза помечена явно. Отказ: низкоранговое обновление лежит в почти невидимом направлении данных.
