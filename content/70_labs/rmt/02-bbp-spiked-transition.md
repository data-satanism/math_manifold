---
id: lab-rmt-bbp-spiked-transition
title: "Лаборатория RMT 02. Спайковый переход и согласование PCA"
aliases: ["RMT lab BBP", "Численный спайковый переход"]
type: lab
status: canonical
publish: true
areas: [random-matrix-theory, scientific-computing]
concepts: [spiked-random-matrix-model, spectral-edge-outlier, eigenvector-alignment]
prerequisites: [spiked-covariance-transition]
ai_domains: [pca, signal-detection, representation-learning]
source_refs:
  - id: rmt4ml-2022
    pages: "113-121"
    role: primary
level: advanced
created: 2026-07-30
updated: 2026-11-18
---

# Лаборатория RMT 02. Спайковый переход и согласование PCA

> [!note] Как повторить опыт
> Полный сценарий и перечисленные файлы измерений находятся в авторском хранилище. На сайте доступны описание опыта и опубликованные иллюстрации. Самостоятельная проверка ниже запускается стандартным Python 3.

## Ложный корень и допустимая ветвь

При $c=1/4$ спайки $\ell=1/4$ и $\ell=1$ дают одинакового алгебраического
кандидата $5/2$. Подставьте физическую MP-ветвь: остатки скалярного уравнения
должны быть $3/5$ и $0$, для допустимого корня квадрат согласования $3/5$.
Допуск $10^{-12}$. Это проверка предельных формул на фиксированных параметрах.

```python
from math import sqrt

c = 0.25
lo, hi = (1 - sqrt(c))**2, (1 + sqrt(c))**2
residuals = []
for spike in (0.25, 1.0):
    z = (1 + spike)*(1 + c/spike)
    m = (1 - c - z + sqrt((z - lo)*(z - hi)))/(2*c*z)
    residuals.append(1 + z*spike*m/(1 + spike))
overlap = (1 - c/1.0**2)/(1 + c/1.0)
assert abs(residuals[0] - 0.6) < 1e-12 and abs(residuals[1]) < 1e-12
assert abs(overlap - 0.6) < 1e-12
print(residuals, overlap)
```

## Исследовательский вопрос

Совпадают ли появление спектрального выброса и возникновение информативного направления PCA в конечной размерности?

## Эксперимент

Для ковариации $C=I+\ell uu^T$ изменяется $\ell$. Измеряются верхнее собственное значение выборочной ковариации и квадрат согласования главного собственного вектора с $u$.

```powershell
python 70_labs/rmt/rmt_release_experiments.py `
  --experiment bbp `
  --output-dir 80_assets/random-matrix-theory/labs-v1
```

![Численное отделение верхнего собственного значения и рост согласования PCA после спайкового порога](80_assets/random-matrix-theory/labs-v1/lab-bbp-spiked-transition.webp)

## Проверки

1. Измените отношение $c=p/n$.
2. Увеличьте число повторов и постройте доверительную полосу.
3. Сравните порог отделения значения с порогом устойчивой корреляции направления.

## Перенос

**Установлено.** В спайковой ковариационной модели порог равен $\ell=\sqrt c$.

**Граница.** Выбор ранга обученного представления требует отдельной нулевой модели и проверки стабильности направления на новых данных.
