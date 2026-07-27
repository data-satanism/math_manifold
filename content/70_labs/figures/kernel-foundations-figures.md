---
id: lab-kernel-foundations-figures
title: "Паспорт визуализаций основ ядерных методов"
aliases: ["Фигуры ядер и RKHS"]
type: lab
status: canonical
publish: true
areas: [kernel-methods, scientific-visualization]
concepts: [visual-prompt, figure-provenance, source-verification]
prerequisites: [km-01-positive-definite-kernels-rkhs]
ai_domains: [kernels, gaussian-processes, representation-learning]
source_refs:
  - id: hofmann-scholkopf-smola-kernel-methods-2006
    pages: "3-19"
    role: visual-source
level: advanced
created: 2026-07-17
updated: 2026-07-27
---

# Паспорт визуализаций основ ядерных методов

## Стилевой контракт

Все фигуры создаются по общей неизменной первой части составного промпта:

> ICML-style scientific figure, clean academic vector infographic, white background, muted blue-gray palette with one accent color, minimal typography, precise arrows, thin lines, labeled panels, no photorealism, no 3D glossy rendering, no decorative background, conference-paper figure aesthetics, mathematically clean, visually balanced.

Дополнительные требования: русские научные подписи; английский только для стандартных сокращений; на одной фигуре разделены строгий механизм, понятный образ, перенос к ИИ и режим отказа.

## Фигуры

### Обзор модуля

Файл: [kernel-foundations-module-insight-v1.png](80_assets/kernel-methods/gpt-image-v1/kernel-foundations-module-insight-v1.png)

Смысловые слои: функция сходства; матрица Грама; пространство функций; конечное разложение; проверка переноса.

Контрольная сумма SHA-256: `F199E3DA05D466023F5C09F556E3D56BDEA52C854600AD3A6878191C893F5262`.

### Положительно определённое ядро

Файл: [positive-definite-kernel-insight-v1.png](80_assets/kernel-methods/gpt-image-v1/positive-definite-kernel-insight-v1.png)

Смысловые слои: квадратичная форма; геометрия признаков; согласование измерений; неопределённое сходство как режим отказа.

Контрольная сумма SHA-256: `87D126A9EC9AD84DB32F465C9359C0E7F261775F967427D4235EA2EBF331A681`.

### Теорема Мура—Ароншайна

Файл: [moore-aronszajn-correspondence-v1.png](80_assets/kernel-methods/gpt-image-v1/moore-aronszajn-correspondence-v1.png)

Смысловые слои: ядерные сечения; скалярное произведение; пополнение; воспроизводящее свойство; конечная выборка как неполный снимок.

Контрольная сумма SHA-256: `3B13F8D4798123D753B40F66E44E5E030D472672860B48CCA292A2AAE7922D4B`.

### Теорема о представителе

Файл: [representer-theorem-insight-v1.png](80_assets/kernel-methods/gpt-image-v1/representer-theorem-insight-v1.png)

Смысловые слои: ортогональная декомпозиция; невидимая компонента; снижение нормы; якоря обучающей выборки; границы совместного обучения признаков.

Контрольная сумма SHA-256: `415D8613C800E272AEAF6C08B94FB64A54257A6EED6F463BA0D954139D633A07`.

### Правила конструирования

Файл: [kernel-closure-rules-v1.png](80_assets/kernel-methods/gpt-image-v1/kernel-closure-rules-v1.png)

Смысловые слои: сумма каналов; тензорное взаимодействие; композиция с признаками; отрицательный вес как режим отказа.

Контрольная сумма SHA-256: `90ED38EBBC21EDF0FB246DA1EB3D92CD16F832C675CF367A3AC19F0F61DA84DA`.

## Источниковая сверка

- с. 4–6: определения матрицы Грама, положительности, построение RKHS и воспроизводящее равенство;
- с. 6–14: замкнутость и примеры ядер;
- с. 15–16: формулировка и доказательство теоремы о представителе;
- с. 16–19: сокращённые разложения и регуляризационный смысл.

Формулы проверены по визуальному рендеру страниц исходного PDF. Извлечённый текст использовался для навигации, но не как единственный источник математических обозначений.
