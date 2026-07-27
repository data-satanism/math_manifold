---
id: rmt-chapters-02-08-v3-figures
title: "Промты визуализаций RMT: модули 02–08, версия 3"
aliases: ["RMT chapters 02-08 visual prompts v3"]
type: lab
status: canonical
publish: true
areas: [random-matrix-theory, visualization]
concepts: [deterministic-equivalent, covariance-distance, random-kernel-matrix, random-feature-gram-matrix, generalized-linear-classifier, stochastic-block-model, concentration-of-measure]
prerequisites: [rmt-source-map]
ai_domains: [scientific-communication, statistical-learning, graph-ml, neural-networks]
source_refs:
  - id: rmt4ml-2022
    pages: "44-410"
    role: primary
level: advanced
created: 2026-07-27
updated: 2026-07-27
---

# Промты визуализаций RMT: модули 02–08, версия 3

## Постоянная часть

> ICML-style scientific figure, clean academic vector infographic, white background, muted blue-gray palette with one accent color, minimal typography, precise arrows, thin lines, labeled panels, no photorealism, no 3D glossy rendering, no decorative background, conference-paper figure aesthetics, mathematically clean, visually balanced.

## Содержательная структура

Каждая фигура использует три панели:

1. математический механизм и условия;
2. образ или аналогия для переноса идеи;
3. применение в ИИ с явной границей применимости.

| Файл | Математическая идея | Образ | Ограничение |
|---|---|---|---|
| `deterministic-equivalent-resolvent-insight-v3.png` | резольвента и сходимость наблюдаемых следов | настраиваемый спектрометр | не операторно-нормовая сходимость |
| `covariance-distance-correction-insight-v3.png` | поправка смещения ковариационного функционала | калибровка искажённого сканера | не восстановление всей ковариации |
| `random-kernel-scaling-insight-v3.png` | концентрация расстояний и локальные коэффициенты ядра | усиление микрофона | не всякое ядро оптимально |
| `random-feature-gram-insight-v3.png` | эффективное ядро случайных признаков | вместимость мест и двойной спуск | один фиксированный случайный слой |
| `high-dimensional-convex-classifier-insight-v3.png` | исключение объекта, проксимальное отображение, фиксированная точка | упругая перегородка | гладкая потеря; SVM отдельно |
| `dense-sbm-spectral-transition-insight-v3.png` | выброс и согласование в плотной блочной модели | радиостанция в шуме | разреженный режим требует других операторов |
| `concentrated-data-universality-insight-v3.png` | липшицева устойчивость концентрации | испытание масштабного макета | не все реальные данные и не все функционалы |

## Проверка

- Основной язык подписей — русский.
- Формулы сведены к коротким, проверяемым обозначениям.
- В каждой фигуре присутствует прикладная аналогия.
- В каждой фигуре отмечено, что именно установлено, а что не следует из теоремы.
- Исходные изображения сгенерированы встроенной моделью GPT.Image и сохранены в `80_assets/random-matrix-theory/gpt-image-v3`.
