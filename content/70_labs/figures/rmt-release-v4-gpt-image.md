---
id: lab-rmt-release-v4-gpt-image
title: "Промты GPT.Image для релиза RMT 2.0, версия 4"
aliases: ["RMT GPT.Image v4", "Визуальный пакет RMT 2.0"]
type: lab
status: canonical
publish: true
areas: [random-matrix-theory, scientific-visualization]
concepts: [visual-prompt, spectral-edge-outlier, deterministic-equivalent, spiked-random-matrix-model]
prerequisites: [rmt-release-2-map]
ai_domains: [scientific-communication, spectral-diagnostics, kernels, graph-ml]
source_refs:
  - id: rmt4ml-2022
    pages: "44-410"
    role: primary
level: advanced
created: 2026-07-30
updated: 2026-08-12
---

# Промты GPT.Image для релиза RMT 2.0, версия 4

## Постоянная часть

> ICML-style scientific figure, clean academic vector infographic, white background, muted blue-gray palette with one accent color, minimal typography, precise arrows, thin lines, labeled panels, no photorealism, no 3D glossy rendering, no decorative background, conference-paper figure aesthetics, mathematically clean, visually balanced.

> Russian-first scientific labels; use English only for standard abbreviations. Clearly distinguish established result, analogy, research hypothesis, and failure mode.

## Содержательные части

| Файл | Математическая идея | Понятный образ | Перенос и граница |
|---|---|---|---|
| `rmt-module-01-high-dimensional-spectra-v4.png` | двойная асимптотика, шумовой массив, выброс | хор и уровень фонового шума | выбор нулевой модели; нельзя смешивать операторы |
| `rmt-module-02-resolvents-v4.png` | ESD → резольвента → фиксированная точка | спектральный сканер с шириной полосы | детерминированный эквивалент; не операторно-нормовая сходимость |
| `rmt-module-03-covariance-inference-v4.png` | высокоразмерное смещение и поправка | калибровка измерительного прибора | дрейф ковариаций; зависимость выборок нарушает вывод |
| `rmt-module-04-random-kernels-v4.png` | концентрация расстояний и локальное разложение ядра | настройка усилителя около рабочей точки | спектральная кластеризация; неверный масштаб уничтожает сигнал |
| `rmt-module-05-random-networks-v4.png` | случайные признаки, матрица Грама, обусловленность и двойной спуск | радиоприёмник около критической настройки | контролируемая модель случайных признаков; не глубокая обучаемая сеть |
| `rmt-module-06-convex-classifiers-v4.png` | выпуклая цель, регуляризация и макроскопические параметры | многомерный рельеф и приборная панель | ошибка классификации при модельных предпосылках; асимптотический прогноз не равен точной гарантии |
| `rmt-module-07-graph-spectra-v4.png` | шумовой диапазон, отдельное значение и согласование сообществ | согласованный групповой ритм над радиошумом | плотная SBM; хабы и разреженность меняют режим |
| `rmt-module-08-universality-v4.png` | концентрация и совпадение наблюдаемой величины | разные материалы с одним макрозаконом | моментный суррогат; не равенство распределений |
| `empirical-spectral-distribution-v4.png` | список собственных значений превращается в меру | общая гистограмма результатов экзамена | спектральная сводка; конечные сигнальные значения имеют исчезающий вес |
| `resolvent-stieltjes-v4.png` | комплексный зонд и сглаженная плотность | спектральный сканер с регулируемой шириной луча | сглаженная диагностика; малое сглаживание неустойчиво |
| `marchenko-pastur-law-v4.png` | прямоугольная выборка превращает шум в асимметричную плотность | оркестр без солиста | шумовой эталон PCA; неоднородная ковариация меняет закон |
| `spiked-covariance-transition-v4.png` | порог по силе сигнала, отделение и согласование | солист в хоре | PCA установлено для шипованной модели; ранг обученной сети — гипотеза |
| `wigner-semicircle-law-insight-v4.png` | симметричный шум и полукруг | случайные колебания на экране осциллографа | эталон для ансамбля Вигнера; обученные веса — только аналогия |
| `rmt-spectral-diagnostics-v4.png` | оператор → нулевая модель → край → устойчивость | медицинская диагностика по нескольким анализам | проверяемый протокол; спектр не является автоматическим вердиктом |

## Обязательные ограничения

- только русские обычные слова; допустимы сокращения RMT, PCA, ML и математические символы;
- не использовать слова `bulk`, `outlier`, `attention rank selection`, `softmax`;
- четыре визуальные функции: математическая идея, понятный образ, перенос в ИИ, режим отказа;
- не копировать фигуры из монографии; композиция и пиктограммы создаются заново;
- подписи внутри изображения не являются математическим источником истины.

## Ручная приёмка

Каждый принятый файл проверен визуально после генерации. Версии с перепутанными законами, неверными осями, неполными формулами или английскими подписями отбракованы и не скопированы в `80_assets/random-matrix-theory/gpt-image-v4`.
