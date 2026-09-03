---
id: lab-rmt-sbm-dense-sparse
title: "Лаборатория RMT 05. Плотный и разреженный режимы блочной модели"
aliases: ["SBM RMT lab", "Плотная и разреженная SBM"]
type: lab
status: canonical
publish: true
areas: [random-matrix-theory, graph-spectra, scientific-computing]
concepts: [stochastic-block-model, spectral-edge-outlier, eigenvector-alignment]
prerequisites: [dense-sbm-spectral-transition, wigner-semicircle-law]
ai_domains: [graph-ml, community-detection, spectral-clustering]
source_refs:
  - id: rmt4ml-2022
    pages: "366-390"
    role: primary
level: advanced
created: 2026-07-30
updated: 2026-08-12
---

# Лаборатория RMT 05. Плотный и разреженный режимы блочной модели

## Исследовательский вопрос

Почему порог, полученный из вигнеровского фона плотного графа, нельзя переносить на граф ограниченной средней степени?

## Эксперимент

Для двух сообществ сравнивается квадрат согласования спектрального направления с метками в плотном режиме и при фиксированной средней степени.

```powershell
python 70_labs/rmt/rmt_release_experiments.py `
  --experiment sbm `
  --output-dir 80_assets/random-matrix-theory/labs-v1
```

![Сравнение согласования спектрального направления с метками в плотной и разреженной блочных моделях](80_assets/random-matrix-theory/labs-v1/lab-sbm-dense-sparse.webp)

## Важная деталь

Центрирование должно удалять только глобальную вероятность ребра. Если вычесть полную матрицу вероятностей по классам, вместе с фоном исчезнет и исследуемый сигнал.

## Граница

**Установлено.** Теорема плотной SBM использует полукруговой шумовой массив.

**Наблюдение эксперимента.** В разреженном режиме тот же простой оператор имеет другую конечномерную динамику.

**Не следует.** Различие кривых само по себе не задаёт оптимальный оператор для разреженного графа.
