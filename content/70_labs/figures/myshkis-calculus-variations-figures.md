---
id: lab-myshkis-calculus-variations-figures
title: "Паспорт визуализаций главы VI Мышкиса"
aliases: ["Фигуры вариационного исчисления"]
type: lab
status: canonical
publish: true
areas: [calculus-of-variations, scientific-visualization]
concepts: [visual-prompt, source-verification, figure-provenance]
prerequisites: [apm-06-calculus-of-variations]
ai_domains: [scientific-machine-learning]
source_refs:
  - id: myshkis-applied-mathematics-engineers-2006
    pages: "281-418"
    role: visual-source
level: advanced
created: 2026-07-17
updated: 2026-07-27
---

# Паспорт визуализаций главы VI Мышкиса

## Общий стилевой контракт

Все пять фигур созданы по составному промпту с неизменной первой частью:

> ICML-style scientific figure, clean academic vector infographic, white background, muted blue-gray palette with one accent color, minimal typography, precise arrows, thin lines, labeled panels, no photorealism, no 3D glossy rendering, no decorative background, conference-paper figure aesthetics, mathematically clean, visually balanced.

Дополнительный контракт: русские научные подписи; английский используется только для стандартных сокращений; установленные результаты, аналогии, исследовательские гипотезы и режимы отказа визуально разделены.

## Источниковая сверка

- с. 288–305: допустимые вариации, первая вариация и вывод уравнения Эйлера;
- с. 324–336: вторая вариация, условия Лежандра и Якоби, геометрия сопряжённых точек;
- с. 350–361: канонические переменные, однопараметрические группы и теорема Нётер;
- с. 370–383: действие, уравнения поля и законы сохранения;
- с. 392–418: методы Ритца, Бубнова—Галёркина, Канторовича и Эйлера.

Формулы, номера печатных страниц и геометрия сопряжённых точек проверены по визуальному рендеру исходного скана. Автоматически распознанный текст не использовался как математический источник.

## Фигуры и смысловые слои

### Обзор модуля

Файл: [calculus-of-variations-module-insight-v1.png](80_assets/calculus-of-variations/gpt-image-v1/calculus-of-variations-module-insight-v1.png)

Панели: пространство функций и функционал; первая и вторая вариации; переход к уравнению и прямому методу; перенос к энергетической модели с независимыми проверками.

Контрольная сумма SHA-256: `DAB93DE86428C1A0568EAAA13CA74D12DAA6A33A0D5B936849DE467A42E84BE0`.

### Уравнение Эйлера—Лагранжа

Файл: [euler-lagrange-local-balance-v1.png](80_assets/calculus-of-variations/gpt-image-v1/euler-lagrange-local-balance-v1.png)

Панели: локализованная вариация; интегрирование по частям; фундаментальная лемма как локальный баланс; перенос к вычислению дифференциальной невязки и два режима отказа.

Контрольная сумма SHA-256: `07CF19A2DBD9A00E84B8CE7F1FC5154895BDB22AA26A29E36CA0A99721EDD556`.

### Вторая вариация и сопряжённые точки

Файл: [second-variation-jacobi-insight-v1.png](80_assets/calculus-of-variations/gpt-image-v1/second-variation-jacobi-insight-v1.png)

Панели: квадратичная форма; веер экстремалей и первая сопряжённая точка; безопасный и небезопасный интервалы; аналогия с потерей устойчивости и границы гессианной диагностики.

Контрольная сумма SHA-256: `8EA021446EE217B7B17FCE88B5312A80A3DD2DBCA62ECB51460EC02BAE83A0B7`.

### Теорема Нётер

Файл: [noether-symmetry-conservation-v1.png](80_assets/calculus-of-variations/gpt-image-v1/noether-symmetry-conservation-v1.png)

Панели: однопараметрическое преобразование; вариационное тождество; энергия, импульс и момент импульса; архитектурная симметрия, контроль дрейфа и исследовательская гипотеза.

Контрольная сумма SHA-256: `D7DF10BD40E40BED00ABE99926DFFC032858F92743577B1EF12BF70C746F5143`.

### Мост к моделям ИИ

Файл: [variational-principles-ai-bridge-v1.png](80_assets/calculus-of-variations/gpt-image-v1/variational-principles-ai-bridge-v1.png)

Панели: полный математический контракт; энергетическое предсказание, неявный слой и нейронный оператор; мембрана как понятный образ; валидационный протокол и режимы отказа. Первая версия была отклонена из-за смешанного заголовка; текущая версия содержит русскую подпись «Три вычислительные схемы».

Контрольная сумма SHA-256: `109EADA7EB5E1F6E141A85CACD11672781F07D868EE97D86D4041855A5FA4659`.

## Проверка качества

- У каждой новой страницы модуля, теоремы и моста есть отдельная содержательная фигура.
- Каждая фигура включает математический механизм, понятный образ или пример, перенос к ИИ и режим отказа.
- Термины и подписи русскоязычные; стандартные сокращения раскрываются в тексте заметок.
- Растровые файлы версионированы и не перезаписывают предыдущие семейства изображений.

