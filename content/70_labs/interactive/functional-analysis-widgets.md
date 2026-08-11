---
id: lab-functional-analysis-widgets
title: "Интерактивы курса функционального анализа"
aliases: ["Интерактивные модели функционального анализа"]
type: lab
status: canonical
publish: true
areas: [functional-analysis, visualization]
concepts: [norm, convergence-modes, compactness, hilbert-space, spectrum, fixed-point]
prerequisites: [functional-analysis-map]
ai_domains: [optimization, kernels, model-compression, implicit-models]
source_refs: []
level: intermediate
created: 2026-07-10
updated: 2026-07-27
---

# Интерактивы курса функционального анализа

Каждая интерактивная модель работает целиком в браузере, не отправляет данные наружу и имеет статическую SVG-версию.

## 1. Геометрия норм

[Открыть интерактив Lp-геометрии](80_assets/interactive/norm-geometry.html)

![Сравнение геометрии единичных шаров при разных значениях p](80_assets/functional-analysis/interactive-norms.svg)

## 2. Виды сходимости

[Открыть интерактив всплесков](80_assets/interactive/convergence-modes.html)

![Сужающийся всплеск различает поточечную сходимость и сходимость по норме](80_assets/functional-analysis/interactive-convergence.svg)

## 3. Компактность

[Открыть интерактив компактности](80_assets/interactive/compactness.html)

![Разделённая и сходящаяся последовательности в ограниченном множестве](80_assets/functional-analysis/interactive-compactness.svg)

## 4. Гильбертова проекция

[Открыть интерактив проекции](80_assets/interactive/hilbert-projection.html)

![Ортогональная проекция точки на замкнутое подпространство](80_assets/functional-analysis/interactive-projection.svg)

## 5. Спектр и малоранговое приближение

[Открыть интерактив спектрального усечения](80_assets/interactive/spectrum-low-rank.html)

![Спектральное усечение отделяет сохраняемые направления от остатка](80_assets/functional-analysis/interactive-spectrum.svg)

## 6. Сжимающее отображение

[Открыть интерактив неподвижной точки](80_assets/interactive/contraction-map.html)

![Итерации сжимающего отображения сходятся к неподвижной точке](80_assets/functional-analysis/interactive-fixed-point.svg)

## Проверка доступности

- Элементы управления имеют подписи и доступны с клавиатуры.
- Область рисунка снабжена атрибутом `aria-label`.
- Цвет не является единственным носителем смысла.
- При отключённом JavaScript показывается статическая SVG-версия.
- Компоновка перестраивается на узком экране.
