---
id: lab-myshkis-dynamical-systems-figures
title: "Паспорт визуализаций главы VIII Мышкиса"
aliases: ["Фигуры динамических систем"]
type: lab
status: canonical
publish: true
areas: [dynamical-systems, scientific-visualization]
concepts: [visual-prompt, source-verification, figure-provenance]
prerequisites: [apm-08-dynamical-systems]
ai_domains: [recurrent-models, neural-differential-equations, scientific-machine-learning]
source_refs:
  - id: myshkis-applied-mathematics-engineers-2006
    pages: "531-671"
    role: visual-source
level: advanced
created: 2026-07-17
updated: 2026-07-27
---

# Паспорт визуализаций главы VIII Мышкиса

## Общий стилевой контракт

Все шесть фигур создаются по составному промпту с неизменной первой частью:

> ICML-style scientific figure, clean academic vector infographic, white background, muted blue-gray palette with one accent color, minimal typography, precise arrows, thin lines, labeled panels, no photorealism, no 3D glossy rendering, no decorative background, conference-paper figure aesthetics, mathematically clean, visually balanced.

Дополнительный контракт: русские научные подписи; английский используется только для стандартных сокращений; математический механизм, понятный образ, перенос к ИИ и режим отказа разделены по панелям.

## Источниковая сверка

- с. 531–549: фундаментальная матрица, сопряжённая система, периодические коэффициенты и монодромия;
- с. 550–566: возмущения, осцилляции, метод ВКБ и точки поворота;
- с. 567–599: автономный поток, предельные множества, фазовые портреты и циклы;
- с. 600–617: устойчивость, первое приближение и функции Ляпунова;
- с. 618–628: механические и управляемые системы;
- с. 629–671: резонанс, автоколебания, релаксационные режимы, усреднение и дискретное время.

Формулы, номера печатных страниц и фазовые портреты проверены по визуальному рендеру исходного скана. Автоматически распознанный математический текст не использовался как источник.

## Фигуры и смысловые слои

### Обзор модуля

Файл: [dynamical-systems-module-insight-v1.png](80_assets/dynamical-systems/gpt-image-v1/dynamical-systems-module-insight-v1.webp)

Панели: линейный перенос и монодромия; фазовый поток и предельные режимы; функция Ляпунова; цикл и быстро-медленная динамика; перенос к моделям скрытого состояния.

Контрольная сумма SHA-256: `1BE21EA6551FA4D7CD20B2D5F867B766731C5930EC59EA5928C8DC64198B82E6`.

### Теорема Пуанкаре—Бендиксона

Файл: [poincare-bendixson-trapping-v1.png](80_assets/dynamical-systems/gpt-image-v1/poincare-bendixson-trapping-v1.webp)

Панели: плоская ловящая область; непересечение траекторий; поперечник и возвраты; кольцевой канал; трёхмерный режим отказа.

Контрольная сумма SHA-256: `E826F95513853D15590281A7776568FB5AFAC94A9253222CE0F9430F9A4C21E0`.

### Прямой метод Ляпунова

Файл: [lyapunov-energy-landscape-v1.png](80_assets/dynamical-systems/gpt-image-v1/lyapunov-energy-landscape-v1.webp)

Панели: вложенные подуровни; невозрастающая энергия; шарик в чаше; квадратичный сертификат; обучаемая энергия и поиск нарушений.

Контрольная сумма SHA-256: `6F235B90E980853C619DD0611185E70387560AB7566C420741B18DCF4B866432`.

### Мультипликаторы Флоке

Файл: [floquet-cycle-multipliers-v1.png](80_assets/dynamical-systems/gpt-image-v1/floquet-cycle-multipliers-v1.webp)

Панели: цикл и нейтральная фаза; поперечное сжатие; карта Пуанкаре; спектр монодромии; сохранение ритма в рекуррентной модели.

Контрольная сумма SHA-256: `68E82CA610DE3134F79DF9B5E5ADD7AB0B4C027F8B08181845A5C24E363CA1D2`.

### Метод усреднения

Файл: [averaging-slow-envelope-v1.png](80_assets/dynamical-systems/gpt-image-v1/averaging-slow-envelope-v1.webp)

Панели: быстрая несущая и медленная огибающая; малые изменения за период; усреднённая траектория; качели с малыми толчками; резонансный режим отказа.

Контрольная сумма SHA-256: `70FE1FF396ED6CE86A84B61B836F84A363DC561A533E68141874DD5C8581847F`.

### Мост к ИИ

Файл: [dynamical-systems-ai-bridge-v1.png](80_assets/dynamical-systems/gpt-image-v1/dynamical-systems-ai-bridge-v1.webp)

Панели: рекуррентная карта; непрерывная модель и решатель; равновесие и цикл; многомасштабное состояние; независимые проверки горизонта, шага, энергии и поперечного спектра.

Контрольная сумма SHA-256: `F9F5CCBBCA99D14FD72B2FE2CE3CAA0FA035E2DC62EBC18FCDC02DA46A8205EB`.

## Проверка качества

- У каждой новой страницы модуля, теоремы, метода и моста есть отдельная содержательная фигура.
- Каждая фигура включает строгий механизм, понятный перенос и хотя бы один режим отказа.
- Траектория, орбита и параметризованное решение визуально различаются.
- Нейтральная фаза цикла не смешивается с поперечной неустойчивостью.
- Термины и подписи русскоязычные, а растровые файлы версионированы.
