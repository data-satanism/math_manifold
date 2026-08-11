---
id: fft-circulant-matvec-method
title: "Умножение циркулянта и теплицевой матрицы через БПФ"
aliases: ["Циркулянт через БПФ", "Теплицево умножение"]
type: method
status: canonical
publish: true
areas: [numerical-analysis, harmonic-analysis]
concepts: [fft, circulant-matrix, toeplitz-embedding, convolution]
prerequisites: [circulant-fourier-diagonalization-theorem]
ai_domains: [convolutional-networks, time-series, spectral-methods]
source_refs:
  - id: tyrtyshnikov-numerical-analysis
    pages: "254-256"
    role: primary
level: advanced
created: 2026-07-15
updated: 2026-07-27
---

# Умножение циркулянта и теплицевой матрицы через БПФ

## Циркулянт

Предварительно вычислить $\widehat c=\operatorname{FFT}(c)$. Для каждого $x$:

$$
Cx=\operatorname{IFFT}(\widehat c\odot\operatorname{FFT}(x)).
$$

## Теплицева матрица

1. Вложить $T$ в циркулянт порядка $N\ge2n-1$.
2. Дополнить $x$ нулями.
3. Выполнить циркулянтное умножение.
4. Взять первые $n$ компонент.

## Сложность

Хранение $O(n)$, подготовка и применение $O(n\log n)$. При многократных умножениях спектр первого столбца переиспользуется.

## Режимы отказа

Недостаточное дополнение вызывает циклическое наложение; несогласованная нормировка прямого и обратного преобразований меняет масштаб; явное построение $F_n$ возвращает квадратичную стоимость.

## Визуализация

![Повторяющийся сдвиг раскрывается как покомпонентное масштабирование частот](80_assets/numerical-analysis/gpt-image-v5/nla-ch24-toeplitz-fft-insight.png)

## Источник

[[60_sources/tyrtyshnikov-numerical-analysis|Тыртышников]], §24.3–24.4, стр. 254–256.
