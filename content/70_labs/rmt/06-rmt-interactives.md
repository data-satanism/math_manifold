---
id: lab-rmt-release-interactives
title: "Интерактивы RMT: спектральный массив и спайковый переход"
aliases: ["RMT interactives", "Интерактивные RMT-демонстрации"]
type: lab
status: canonical
publish: true
areas: [random-matrix-theory, scientific-visualization]
concepts: [marchenko-pastur-law, spiked-random-matrix-model, spectral-edge-outlier]
prerequisites: [marchenko-pastur-law, spiked-covariance-transition]
ai_domains: [spectral-diagnostics, pca, representation-learning]
source_refs:
  - id: rmt4ml-2022
    pages: "60-74, 113-121"
    role: primary
level: advanced
created: 2026-07-30
updated: 2026-08-12
---

# Интерактивы RMT: спектральный массив и спайковый переход

## Спектральный массив Марченко—Пастура

<iframe src="80_assets/interactive/rmt-mp-spectrum.html" title="Интерактив спектрального массива Марченко—Пастура" loading="lazy" style="width:100%;min-height:700px;border:0"></iframe>

Статическая резервная версия:

![Статическая схема зависимости шумового спектрального массива от отношения размерности к числу наблюдений](80_assets/random-matrix-theory/interactive-rmt-mp-spectrum.svg)

## Спайковый переход

<iframe src="80_assets/interactive/rmt-bbp-transition.html" title="Интерактив спайкового перехода выборочной ковариации" loading="lazy" style="width:100%;min-height:700px;border:0"></iframe>

Статическая резервная версия:

![Статическая схема перехода от скрытого спайка к отделившемуся собственному значению](80_assets/random-matrix-theory/interactive-rmt-bbp-transition.svg)

## Доступность

- все параметры управляются нативными ползунками;
- поддерживаются стрелки клавиатуры;
- состояние дублируется текстом через `aria-live`;
- серверная часть и внешние библиотеки не используются;
- при отключённом JavaScript доступна резервная SVG-версия.
