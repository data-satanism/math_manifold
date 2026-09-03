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
updated: 2026-08-12
---

# Лаборатория RMT 02. Спайковый переход и согласование PCA

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
