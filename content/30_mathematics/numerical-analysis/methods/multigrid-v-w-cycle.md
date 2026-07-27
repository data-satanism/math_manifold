---
id: multigrid-v-w-cycle-method
title: "Многосеточные V- и W-циклы"
aliases: ["V-цикл", "W-цикл"]
type: method
status: canonical
publish: true
areas: [numerical-analysis, partial-differential-equations]
concepts: [multigrid, smoother, restriction, prolongation, coarse-grid-correction]
prerequisites: [nla-24-multigrid-subspace-corrections]
ai_domains: [scientific-machine-learning, multiscale-learning]
source_refs:
  - id: tyrtyshnikov-numerical-analysis
    pages: "241-248"
    role: primary
level: advanced
created: 2026-07-15
updated: 2026-07-27
---

# Многосеточные V- и W-циклы

## Один цикл

1. Выполнить $m$ предсглаживаний.
2. Вычислить невязку $r=b-Ax$.
3. Огрубить невязку $\widehat r=Pr$.
4. Приближённо решить $\widehat A\widehat e=\widehat r$ на грубом уровне.
5. Продлить поправку $x\leftarrow x+Q\widehat e$.
6. Выполнить $m$ постсглаживаний.

V-цикл делает один рекурсивный грубый вызов, W-цикл — два.

## Критерии качества

- высокочастотная ошибка быстро уменьшается сглаживателем;
- гладкая ошибка хорошо представима на грубом уровне;
- операторы переноса согласованы с энергией;
- суммарная стоимость уровней образует геометрический ряд.

## Режимы отказа

Плохой перенос теряет режим, слишком слабый сглаживатель оставляет осцилляции, а слишком точная грубая задача уничтожает выигрыш по времени.

## Перенос в ИИ

**Аналогия.** Многоуровневая модель полезна, если каждый масштаб исправляет собственную часть измеримой ошибки, а не просто добавляет признаки.

## Визуализация

![V-цикл разделяет работу между сглаживанием и грубой коррекцией](80_assets/numerical-analysis/gpt-image-v5/nla-ch23-multigrid-insight.png)

## Источник

[[60_sources/tyrtyshnikov-numerical-analysis|Тыртышников]], §23.1–23.10, стр. 241–248.

