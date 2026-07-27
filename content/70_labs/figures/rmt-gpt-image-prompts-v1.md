---
id: lab-rmt-gpt-image-prompts-v1
title: "Реестр запросов GPT.Image для RMT: версии 1–2"
aliases: ["RMT GPT.Image prompts", "RMT visual prompts v1-v2"]
type: lab
status: canonical
publish: true
areas: [random-matrix-theory, visualization]
concepts: [empirical-spectral-distribution, resolvent-stieltjes-transform, marchenko-pastur-law, spiked-covariance-transition, random-feature-gram-matrix, spiked-tensor-model]
prerequisites: [random-matrix-theory-map]
ai_domains: [scientific-communication, statistical-learning, random-features, tensor-learning]
source_refs:
  - id: rmt4ml-2022
    pages: "44-46, 60-61, 113-121"
    role: primary
level: advanced
created: 2026-07-10
updated: 2026-07-27
---

# Реестр запросов GPT.Image для RMT

## Постоянная стилевая часть

> ICML-style scientific figure, clean academic vector infographic, white background, muted blue-gray palette with one accent color, minimal typography, precise arrows, thin lines, labeled panels, no photorealism, no 3D glossy rendering, no decorative background, conference-paper figure aesthetics, mathematically clean, visually balanced.

Дополнение: русскоязычные научные подписи; английский язык только в стандартных сокращениях. Явно различать установленный результат, аналогию, исследовательскую гипотезу и режим отказа.

## Содержательные части

| Файл | Математическая идея | Понятный образ | Перенос в ИИ и граница |
|---|---|---|---|
| `rmt-module-01-insight.png` | Двойная асимптотика, шумовой массив, спайк | Хор и акустика зала | Выбор оператора и нулевой модели; нельзя смешивать спектры |
| `resolvent-stieltjes-insight.png` | Резольвента, след и обращение Штильтьеса | Настраиваемый спектрометр | Детерминированные эквиваленты; малое $\eta$ неустойчиво |
| `marchenko-pastur-insight.png` | Плотность и края MP, атом в нуле | Один истинный тон размывается в полосу | Нулевой спектр ковариации; не переносить на веса и `softmax` |
| `spiked-transition-insight.png` | Порог $\ell=\sqrt c$ и отделившийся выброс | Буй среди случайных волн | PCA установлено; ранг внимания — гипотеза |
| `rmt-spectral-diagnostics-insight.png` | Структура плюс случайность | Калибровка помещения звукорежиссёром | Пять шагов диагностики и шесть типичных ошибок |
| `random-feature-network-insight-v2.png` | Резольвента матрицы Грама случайных признаков | Спектральная призма | Предсказание ошибок и настройки только для однослойной случайной сети |
| `random-tensor-contractions-insight-v2.png` | Развёртка и свёртка как разные матричные окна | Несколько проекций многомерного объекта | Порог восстановления в тензорных моделях; не доказательство для LoRA |

Фигуры первого набора находятся в `80_assets/random-matrix-theory/gpt-image-v1`, две дополнительные фигуры — в `gpt-image-v2`. Текст заметок остаётся математическим источником истины; подписи внутри изображений служат учебной навигацией.

## Содержательная часть версии 2

### Случайные признаки

Четыре панели: $X\to\Sigma=\sigma(WX)$; матрица Грама и её спектр; спектральная призма, разделяющая шумовой массив и устойчивую структуру; детерминированное предсказание ошибок обучения и тестирования с явной границей «однослойная случайная сеть, совместный рост $n,p,T$».

### Случайные тензоры

Четыре панели: тензор «сигнал плюс гауссов шум»; развёртка и свёртка как два разных матричных окна; аналогия нескольких проекций многомерного объекта; пороговая диаграмма обнаружения и восстановления с явной зависимостью от модели шума, свёртки и режима роста размерностей.
