---
id: lab-myshkis-integral-equations-figures
title: "Паспорт визуализаций главы VII Мышкиса"
aliases: ["Фигуры интегральных уравнений"]
type: lab
status: canonical
publish: true
areas: [integral-equations, scientific-visualization]
concepts: [visual-prompt, source-verification, figure-provenance]
prerequisites: [apm-07-integral-equations]
ai_domains: [neural-operators, attention, scientific-machine-learning]
source_refs:
  - id: myshkis-applied-mathematics-engineers-2006
    pages: "419-530"
    role: visual-source
level: advanced
created: 2026-07-17
updated: 2026-07-27
---

# Паспорт визуализаций главы VII Мышкиса

## Общий стилевой контракт

Все пять фигур создаются по составному промпту с неизменной первой частью:

> ICML-style scientific figure, clean academic vector infographic, white background, muted blue-gray palette with one accent color, minimal typography, precise arrows, thin lines, labeled panels, no photorealism, no 3D glossy rendering, no decorative background, conference-paper figure aesthetics, mathematically clean, visually balanced.

Дополнительный контракт: русские научные подписи; английский используется только для стандартных сокращений; математический механизм, понятный образ, перенос к ИИ и режим отказа разделены по панелям.

## Источниковая сверка

- с. 419–423: классы интегральных уравнений и ядра Гильберта—Шмидта;
- с. 424–433: точная редукция вырожденного ядра;
- с. 457–471: симметрия, собственные функции и спектральное разложение;
- с. 472–495: уравнения Вольтерры, первого рода и разностные ядра;
- с. 496–505: главное значение и формулы Сохоцкого—Племеля;
- с. 514–530: нелинейные уравнения, конечномерная редукция и неподвижные точки.

Формулы и границы печатных страниц проверены по визуальному рендеру исходного скана. Автоматически распознанный математический текст не использовался как источник.

## Фигуры и смысловые слои

### Обзор модуля

Файл: [integral-equations-module-insight-v1.png](80_assets/integral-equations/gpt-image-v1/integral-equations-module-insight-v1.webp)

Панели: поле влияний и классы уравнений; физические образы причинности и сглаживания; конечномерная и спектральная редукции; перенос к операторным слоям и независимые проверки.

Контрольная сумма SHA-256: `B632ACC155831FDAB600C539C48D7CFCEE6B786BE99F6ACB75F41198788A035C`.

### Вырожденное ядро

Файл: [degenerate-kernel-reduction-v1.png](80_assets/integral-equations/gpt-image-v1/degenerate-kernel-reduction-v1.webp)

Панели: разделённое ядро; сбор конечного числа моментов; малая линейная система; восстановление поля; аналогия с латентным операторным слоем и резонансный режим отказа.

Контрольная сумма SHA-256: `003695F3EEF445CABF95F0DB60FD84B1B838D649380BC287D9139659B4A2AD01`.

### Симметричное ядро

Файл: [symmetric-kernel-spectrum-v1.png](80_assets/integral-equations/gpt-image-v1/symmetric-kernel-spectrum-v1.webp)

Панели: взаимное ядро; независимые собственные моды; мембрана как понятный образ; спектральное усечение; потеря ортогональной картины при нарушении симметрии.

Контрольная сумма SHA-256: `733365175E64DAA732E045C32EFD87A6C2DC9DD49E4C2BE25E66D301CF3C7192`.

### Формулы Сохоцкого—Племеля

Файл: [sokhotski-plemelj-jump-v1.png](80_assets/integral-equations/gpt-image-v1/sokhotski-plemelj-jump-v1.webp)

Панели: два подхода к контуру; общее главное значение и половинные скачки; мембрана между средами; компенсационная квадратура и режим отказа.

Контрольная сумма SHA-256: `B01AADE188BB01A95686CFF48135D2007F1CF9D7C910AF603D46A28C0BB358D1`.

### Мост к ИИ

Файл: [integral-equations-ai-bridge-v1.png](80_assets/integral-equations/gpt-image-v1/integral-equations-ai-bridge-v1.webp)

Панели: поле датчиков; внимание, латентные моменты, нейронный оператор и равновесный слой; тесты меры, сетки, ранга, спектра и невязки.

Контрольная сумма SHA-256: `934467AB984B72BB2F06DC2BB90BC0AE2D53CB9C35EAEB75EAEC9A1DBB6043CD`.

## Проверка качества

- У каждой новой страницы модуля, теоремы и моста есть отдельная содержательная фигура.
- Каждая фигура включает строгий механизм и перенос математической идеи на понятный образ.
- Перенос к ИИ отделён от установленного результата и сопровождается режимом отказа.
- Термины и подписи русскоязычные; формулы сведены к коротким, проверяемым выражениям.
- Растровые файлы версионированы и не перезаписывают предыдущие семейства изображений.
