---
id: source-louart-liao-couillet-2018-random-neural-networks
title: "C. Louart, Z. Liao, R. Couillet — A Random Matrix Approach to Neural Networks"
aliases: ["Louart–Liao–Couillet 2018", "Random neural networks via RMT"]
type: source
status: canonical
publish: true
areas: [random-matrix-theory, high-dimensional-statistics]
concepts: [random-feature-gram-matrix, resolvent-stieltjes-transform, deterministic-equivalent]
prerequisites: [probability, linear-algebra, ridge-regression]
ai_domains: [random-features, neural-networks, kernels, statistical-learning]
source_refs:
  - id: louart2018randomnn
    pages: "1-59 PDF pages; journal pages 1190-1248"
    role: primary
level: advanced
created: 2026-07-13
updated: 2026-07-27
---

# A Random Matrix Approach to Neural Networks

- Авторы: Cosme Louart, Zhenyu Liao, Romain Couillet.
- Издание: *The Annals of Applied Probability*, 28(2), 1190–1248, 2018.
- DOI: `10.1214/17-AAP1328`.
- Контрольная сумма SHA-256: `64EC8C361190899CD773279D177A926E2AD62FD30ADC9075AC2084FE9D8F6609`.
- Приватная копия: `_private/sources/rmt/additional/rmt-neural-networks.pdf`; в публичный экспорт не входит.

## Что именно установлено

Работа рассматривает однослойную сеть случайных признаков

$$
\Sigma=\sigma(WX),\qquad G=\frac1T\Sigma^\top\Sigma,
$$

где данные $X$ детерминированы и ограничены по норме, строки $W$ независимы, а функция активации липшицева. При совместном росте числа нейронов $n$, размерности $p$ и числа объектов $T$ резольвента $G$ получает детерминированный эквивалент. Из него выводятся предельная спектральная мера и детерминированные пределы ошибок гребневой регрессии на обучении и тесте.

## Карта страниц

- стр. 1–4 PDF: постановка, область применимости и модель случайных признаков;
- стр. 7–12: основные результаты для резольвенты, обучения и тестирования;
- стр. 13–19: численные следствия, индуцированное ядро и предельные режимы;
- стр. 20–53: концентрация меры и доказательства детерминированных эквивалентов;
- стр. 54: границы результата и направления продолжения.

## Ограничение переноса

Статья не является теорией обученных глубоких сетей, трансформеров или матриц внимания. Её выводы можно переносить только после явного сведения нового объекта к указанной модели случайных признаков.
