---
id: circulant-preconditioning-toeplitz-method
title: "Циркулянтное предобусловливание теплицевых систем"
aliases: ["Оптимальный циркулянт", "Предобусловливатель для теплицевой матрицы"]
type: method
status: canonical
publish: true
areas: [numerical-analysis, numerical-linear-algebra]
concepts: [circulant-preconditioner, toeplitz-matrix, spectral-clustering, fft]
prerequisites: [toeplitz-circulant-spectral-clustering-theorem]
ai_domains: [gaussian-processes, time-series, kernel-methods]
source_refs:
  - id: tyrtyshnikov-numerical-analysis
    pages: "256-259"
    role: primary
level: research
created: 2026-07-15
updated: 2026-07-27
---

# Циркулянтное предобусловливание теплицевых систем

## Идея

Заменить дорогой теплицев оператор близким циркулянтом $C$, для которого $C^{-1}$ применяется через преобразование Фурье. Цель — кластеризовать спектр $C^{-1}A$ около единицы.

## Протокол

1. Построить оптимальный циркулянт из диагонали $FAF^*$.
2. Проверить положительность его частотных множителей.
3. Применять $C^{-1}$ без формирования плотных матриц.
4. Измерять число спектральных выбросов и фактические крыловские итерации.

## Режимы отказа

Малые частотные множители делают $C^{-1}$ неустойчивым; сложная граница нарушает стационарную структуру; несколько выбросов могут доминировать в начальной фазе.

## Перенос в ИИ

**Установленный результат.** Метод применим к стационарным ковариационным системам на регулярных сетках.

## Визуализация

![Предобусловливание собирает основную массу собственных значений около единицы](80_assets/numerical-analysis/gpt-image-v5/nla-ch24-toeplitz-fft-insight.png)

## Источник

[[60_sources/tyrtyshnikov-numerical-analysis|Тыртышников]], §24.5–24.6, стр. 256–259.
