---
id: lab-margin-generalization-figures
title: "Паспорт визуализаций обобщения и сложности класса"
aliases: ["Фигуры средних Радемахера и отступа"]
type: lab
status: canonical
publish: true
areas: [kernel-methods, statistical-learning-theory, scientific-visualization]
concepts: [visual-prompt, figure-provenance, source-verification]
prerequisites: [km-03-margin-uniform-convergence]
ai_domains: [generalization, model-selection, representation-learning, uncertainty-estimation]
source_refs:
  - id: hofmann-scholkopf-smola-kernel-methods-2006
    pages: "26-29"
    role: visual-source
level: advanced
created: 2026-07-20
updated: 2026-07-27
---

# Паспорт визуализаций обобщения и сложности класса

## Стилевой контракт

Все семь фигур созданы встроенной моделью генерации изображений с неизменным префиксом:

> ICML-style scientific figure, clean academic vector infographic, white background, muted blue-gray palette with one accent color, minimal typography, precise arrows, thin lines, labeled panels, no photorealism, no 3D glossy rendering, no decorative background, conference-paper figure aesthetics, mathematically clean, visually balanced.

Дополнение:

> Russian-first scientific labels; use English only for standard abbreviations. Clearly distinguish established result, analogy, research hypothesis, and failure mode.

## Фигуры и содержательные промпты

### Обзор модуля

Файл: [margin-uniform-convergence-module-v2.png](80_assets/kernel-methods/gpt-image-v2/margin-uniform-convergence-module-v2.webp)

Промпт: показать цепочку «отступ → суррогатная потеря → случайные знаки → равномерная оценка → риск»; аналогию с калибровкой чувствительного измерительного прибора; применение к выбору ядра и замороженному представлению; режимы отказа при утечке проверки и сдвиге распределения.

Контрольная сумма SHA-256: `939b3deeed7169fed1098df4f7a7d469636917f818be9f6564bda877ded5119c`.

### Равномерная сходимость

Файл: [rademacher-uniform-convergence-v2.png](80_assets/kernel-methods/gpt-image-v2/rademacher-uniform-convergence-v2.webp)

Промпт: показать призрачную выборку, симметризацию случайными знаками и концентрационную поправку; аналогию с испытательным шумом; проверку класса моделей; контрпример адаптивного выбора функции после просмотра данных.

Контрольная сумма SHA-256: `c7f2240f5df6b471124be693649fc1afb888c7a2db7846b1406076ba176ac444`.

### Шар RKHS

Файл: [rkhs-rademacher-complexity-v2.png](80_assets/kernel-methods/gpt-image-v2/rkhs-rademacher-complexity-v2.webp)

Промпт: показать результирующий вектор случайно подписанных признаков, двойственность нормы и исчезновение смешанных членов; аналогию с перетягиванием каната; диагональ ядра как радиус; режим отказа при неограниченном $k(x,x)$ и обучаемом ядре.

Контрольная сумма SHA-256: `86828a381712049423adeed5f73ccf10329d26d2d735120e0aa9c78f74251af8`.

### Перенос суррогатного риска

Файл: [surrogate-excess-risk-transfer-v2.png](80_assets/kernel-methods/gpt-image-v2/surrogate-excess-risk-transfer-v2.webp)

Промпт: показать условный риск при фиксированном $\eta$, калибровочную функцию и перенос избытка; аналогию с непрерывной шкалой предупреждения; применение к выбору функции потерь; контрпример постоянной выпуклой мажоранты.

Контрольная сумма SHA-256: `300c128ac1d371b9365a13c14dc38f4c5854a83896ad9d2725b02777845b5fe5`.

### Итоговая скорость

Файл: [margin-generalization-rate-v2.png](80_assets/kernel-methods/gpt-image-v2/margin-generalization-rate-v2.webp)

Промпт: показать телескопическое разложение на аппроксимационную и статистическую ошибки, член радиус–отступ; аналогию с двумя частями бюджета маршрута; применение к выбору модели; отказ при настройке по той же проверочной выборке.

Контрольная сумма SHA-256: `2bb927953f84edc2defab82507d9f2d3f0c1b8b94fa86eb15215829846494f4a`.

### Условие Цыбакова

Файл: [tsybakov-noise-localization-v2.png](80_assets/kernel-methods/gpt-image-v2/tsybakov-noise-localization-v2.webp)

Промпт: показать массу около уровня $\eta=1/2$, степенное шумовое условие и локализацию; аналогию с туманной береговой линией; диагностику неопределённости и активной разметки; отказ при некалиброванной уверенности.

Контрольная сумма SHA-256: `835e7fbdcf758bf945055683e77adbfe04976c6263475bf143aaee5eb5901bfd`.

### Мост к ИИ

Файл: [generalization-complexity-ai-v2.png](80_assets/kernel-methods/gpt-image-v2/generalization-complexity-ai-v2.webp)

Промпт: показать сохраняемую цепочку «фиксированный класс → чувствительность к случайным знакам → граница риска»; калибровочный стенд; строгий случай фиксированного представления и условный случай обучаемого; проверки утечки, сдвига и подгруппового риска.

Контрольная сумма SHA-256: `5d3f1124e40626cb3a5689109420f95a7084a1f4ec162b7f63e6e99050ac67d4`.

## Источниковая сверка

- PDF-с. 26: постановка через отступ, эмпирический риск и регуляризацию.
- PDF-с. 27: формулы (85)–(87), ограниченные разности и симметризация.
- PDF-с. 28: сложность шара RKHS, принцип сжатия, формулы (88)–(89).
- PDF-с. 29: условие Цыбакова и связь типа Бернштейна, формулы (90)–(91).

Все номера формул и границы разделов проверены по рендеру исходного PDF. Текст внутри изображений является объяснительным слоем; авторитетные формулировки находятся в Markdown-заметках.
