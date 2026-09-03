---
id: lab-support-vector-estimation-figures
title: "Паспорт визуализаций методов опорных векторов"
aliases: ["Фигуры отступа и опорных объектов"]
type: lab
status: canonical
publish: true
areas: [kernel-methods, scientific-visualization]
concepts: [visual-prompt, figure-provenance, source-verification]
prerequisites: [km-02-support-vector-estimation]
ai_domains: [classification, anomaly-detection, regression, structured-prediction]
source_refs:
  - id: hofmann-scholkopf-smola-kernel-methods-2006
    pages: "20-25"
    role: visual-source
level: advanced
created: 2026-07-20
updated: 2026-07-27
---

# Паспорт визуализаций методов опорных векторов

## Стилевой контракт

Все шесть фигур создаются по неизменной первой части промпта:

> ICML-style scientific figure, clean academic vector infographic, white background, muted blue-gray palette with one accent color, minimal typography, precise arrows, thin lines, labeled panels, no photorealism, no 3D glossy rendering, no decorative background, conference-paper figure aesthetics, mathematically clean, visually balanced.

Дополнение: русские научные подписи; английский только для стандартных сокращений; разделены строгий механизм, понятный образ, перенос к ИИ и режим отказа.

## Фигуры

### Обзор модуля

Файл: [support-vector-estimation-module-v1.png](80_assets/kernel-methods/gpt-image-v1/support-vector-estimation-module-v1.webp)

Слои: единая геометрия отступа; четыре задачи оценивания; двойственная цена; диагностический маршрут.

Контрольная сумма SHA-256: `61ef7fbcd3641daed47e9ca6ee0884747f2ca23a63ca189168e49c79e03cefd7`.

### Двойственность и параметр ν

Файл: [svm-duality-nu-bounds-v1.png](80_assets/kernel-methods/gpt-image-v1/svm-duality-nu-bounds-v1.webp)

Слои: прямая и двойственная задачи; активные ограничения; бюджет двойственной массы; границы ошибок и числа опорных объектов.

Контрольная сумма SHA-256: `2c7db5b18f501e90defbdd3aa081fe072195227a3176987a1e5dbd3afb282e3b`.

### Структурный отступ

Файл: [structured-margin-loss-bound-v1.png](80_assets/kernel-methods/gpt-image-v1/structured-margin-loss-bound-v1.webp)

Слои: прикладная потеря в ограничении; доказательство верхней оценки; резерв маршрута; неточный поиск конкурента.

Контрольная сумма SHA-256: `18e58902f974b83429e2b028e4c883a35613faf5baa3be93cbe8ff6ab3eef8fa`.

### Оценка носителя

Файл: [one-class-svm-support-estimation-v1.png](80_assets/kernel-methods/gpt-image-v1/one-class-svm-support-estimation-v1.webp)

Слои: отделение от начала; множество уровня; охраняемая территория; дрейф штатного режима.

Контрольная сумма SHA-256: `e3f01727ef29325332570978d82f783ea7cf8fb38486ce59d897631ecbdc0b7f`.

### Регрессионная трубка

Файл: [epsilon-insensitive-regression-v1.png](80_assets/kernel-methods/gpt-image-v1/epsilon-insensitive-regression-v1.webp)

Слои: нечувствительная потеря; опорные точки; допуск прибора; меняющийся шум.

Контрольная сумма SHA-256: `0e3197cc642644a2fd904ae800157fb934eb6650fce16c8a345ce9d5a11b2e14`.

### Мост к задачам ИИ

Файл: [support-vector-margins-robust-ai-v1.png](80_assets/kernel-methods/gpt-image-v1/support-vector-margins-robust-ai-v1.webp)

Слои: ограничение, норма и двойственная цена; страховой резерв; четыре механизма ИИ; проверки границ переноса.

Контрольная сумма SHA-256: `f94ed018c2fee5344166c2220d437725a4276ef43001f4665d61cd54606ec9fc`.

## Источниковая сверка

- с. 20–21: жёсткий и мягкий отступ, двойственная задача и условия оптимальности;
- с. 21–22: $\nu$-вариант и оценки числа ошибок и опорных объектов;
- с. 22–23: оценка носителя и регрессия с нечувствительной зоной;
- с. 24–25: многоклассовые, ранговые и структурные ограничения.

Формулы (70)–(84) и границы страниц проверены по визуальному рендеру исходного PDF.
