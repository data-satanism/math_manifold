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
updated: 2026-11-18
---

# Лаборатория RMT 03. Резольвентное восстановление спектральной плотности

> [!note] Как повторить опыт
> Полный сценарий и перечисленные файлы измерений находятся в авторском хранилище. На сайте доступны описание опыта и опубликованные иллюстрации. Самостоятельная проверка ниже запускается стандартным Python 3.

## Разрешение двух собственных значений

Примем спектр $\{1,3\}$ с одинаковыми массами. В точке $x=1$ сглаженная
плотность равна $(1/\eta+\eta/(4+\eta^2))/(2\pi)$. При уменьшении $\eta$
с $1/2$ до $1/4$ пик растёт. Проверим тождество для каждого $\eta$ с допуском $10^{-12}$.

```python
from math import pi

peaks = []
for eta in (0.5, 0.25):
    z = 1 + eta*1j
    m = sum(1/(value - z) for value in (1, 3))/2
    density = m.imag/pi
    expected = (1/eta + eta/(4 + eta**2))/(2*pi)
    assert abs(density - expected) < 1e-12
    peaks.append(density)
assert peaks[0] < peaks[1]
print(peaks)
```

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
