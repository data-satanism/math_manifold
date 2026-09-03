---
id: lab-rmt-resolvent-density-recovery
title: "Лаборатория RMT 03. Резольвентное восстановление спектральной плотности"
aliases: ["RMT resolvent lab", "Спектральный сканер Штильтьеса"]
type: lab
status: canonical
publish: true
areas: [random-matrix-theory, complex-analysis, scientific-computing]
concepts: [resolvent-stieltjes-transform, empirical-spectral-distribution]
prerequisites: [resolvent-stieltjes-transform]
ai_domains: [spectral-diagnostics, covariance-estimation]
source_refs:
  - id: rmt4ml-2022
    pages: "44-50, 60-74"
    role: primary
level: advanced
created: 2026-07-30
updated: 2026-08-12
---

# Лаборатория RMT 03. Резольвентное восстановление спектральной плотности

## Исследовательский вопрос

Как параметр $\eta=\operatorname{Im}z$ меняет компромисс между разрешением отдельных собственных значений и устойчивостью оценки плотности?

## Эксперимент

Для собственных значений $\lambda_i$ вычисляется

$$
\widehat\rho_\eta(x)
=\frac1{\pi p}\sum_{i=1}^p
\frac{\eta}{(\lambda_i-x)^2+\eta^2}.
$$

```powershell
python 70_labs/rmt/rmt_release_experiments.py `
  --experiment resolvent `
  --output-dir 80_assets/random-matrix-theory/labs-v1
```

![Восстановление спектральной плотности по мнимой части резольвенты при трёх уровнях сглаживания](80_assets/random-matrix-theory/labs-v1/lab-resolvent-density-recovery.webp)

## Интерпретация

Малое $\eta$ показывает конечномерные пики, но создаёт высокую дисперсию. Большое $\eta$ стабилизирует оценку, но размывает края и близкие выбросы.

## Перенос

**Установлено.** Формула является сглаженной версией обращения Штильтьеса.

**Аналогия.** $\eta$ играет роль ширины полосы спектрального прибора.

**Граница.** Настройка $\eta$ не исправляет неверно выбранный оператор или зависимую выборку.
