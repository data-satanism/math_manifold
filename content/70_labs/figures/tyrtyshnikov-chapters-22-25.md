---
id: lab-tyrtyshnikov-chapters-22-25-figures
title: "Реестр визуализаций глав 22–25 Тыртышникова"
aliases: ["Промты визуализаций Галёркин—многосетка—структурированные матрицы"]
type: lab
status: canonical
publish: true
areas: [numerical-analysis, visualization]
concepts: [figure-provenance, visual-qa, image-generation]
prerequisites: [numerical-linear-algebra-map]
ai_domains: [scientific-communication]
source_refs:
  - id: tyrtyshnikov-numerical-analysis
    pages: "227-278"
    role: mathematical-foundation
level: advanced
created: 2026-07-15
updated: 2026-07-27
---

# Реестр визуализаций глав 22–25 Тыртышникова

## Неизменяемая часть промта

> ICML-style scientific figure, clean academic vector infographic, white background, muted blue-gray palette with one accent color, minimal typography, precise arrows, thin lines, labeled panels, no photorealism, no 3D glossy rendering, no decorative background, conference-paper figure aesthetics, mathematically clean, visually balanced.

Добавлено требование: русские научные подписи, английский только для стандартных сокращений; установленные результаты, аналогии, гипотезы и режимы отказа визуально разделены.

## Реестр

| Файл | Математическое содержание | Перенос к ИИ | Проверка |
|---|---|---|---|
| `gpt-image-v5/nla-ch22-operator-galerkin-insight.png` | слабая форма, конечные элементы, устойчивость и коэрцитивность | обучаемое пробное пространство с внешней проверкой | формулы и русские подписи проверены |
| `gpt-image-v5/nla-ch23-multigrid-insight.png` | сглаживание, грубая коррекция, V-цикл | многоуровневое представление как аналогия | нет ложного равенства с U-Net |
| `gpt-image-v5/nla-ch24-toeplitz-fft-insight.png` | теплицева и циркулянтная структура, БПФ, кластер спектра | свёрточный и спектральный слой | периодическая граница указана явно |
| `gpt-image-v5/nla-ch25-hierarchical-low-rank-insight.png` | допустимые блоки, крест, вейвлеты, остаток | ядровые взаимодействия и внимание | показан медленный спад сингулярных чисел |

## Составные описания

1. **Глава 22.** Переход к слабой форме, галёркинская проекция, обучаемый базис и три режима нарушения условий.
2. **Глава 23.** Разложение ошибки на гладкую и осциллирующую, V-цикл, многоуровневая аналогия и сбои переноса.
3. **Глава 24.** Повторяющиеся диагонали, независимые частотные каналы, точная связь со свёрткой и граничные артефакты.
4. **Глава 25.** Геометрическое дерево блоков, опорный крест, проверяемая сжимаемость ядра и потеря редкого события.

## Контроль качества

- активы записаны в новой версии `gpt-image-v5`, старые изображения не перезаписаны;
- видимый текст проверен на смешение языков и обрезку;
- каждая теорема, модуль и мост глав 22–25 содержит связанную содержательную фигуру;
- четыре интерактива имеют автономные SVG-версии;
- статус материалов: `review`, `publish: false`.

## Связи

- [[70_labs/interactive/operator-multigrid-structured-widgets]].
- [[30_mathematics/numerical-analysis/tyrtyshnikov-source-map]].

