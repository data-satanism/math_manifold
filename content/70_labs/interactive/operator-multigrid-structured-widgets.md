---
id: lab-operator-multigrid-structured-widgets
title: "Интерактивы операторных, многосеточных и структурированных методов"
aliases: ["Интерактивы глав 22–25 Тыртышникова"]
type: lab
status: canonical
publish: true
areas: [numerical-analysis, visualization]
concepts: [galerkin-projection, multigrid, fourier-diagonalization, hierarchical-compression]
prerequisites: [nla-23-operator-equations-fem-galerkin, nla-24-multigrid-subspace-corrections, nla-25-structured-toeplitz-circulant, nla-26-hierarchical-low-rank-wavelets]
ai_domains: [scientific-machine-learning, spectral-methods, compression]
source_refs:
  - id: tyrtyshnikov-numerical-analysis
    pages: "227-278"
    role: mathematical-foundation
level: advanced
created: 2026-07-15
updated: 2026-07-27
---

# Интерактивы глав 22–25 Тыртышникова

Все интерактивы являются автономными локальными страницами без серверной части. Управление доступно с клавиатуры; рядом хранится статическая SVG-версия.

## Слабая форма и проекция

[Открыть интерактив](80_assets/interactive/galerkin-weak-form.html)

![Статическая схема слабой формы и устойчивости](80_assets/numerical-analysis/interactive-galerkin-weak-form.svg)

Меняются размер пробного пространства и константа устойчивости. Наблюдение: уменьшение аппроксимационной ошибки не компенсирует неограниченное усиление.

## Ошибка по масштабам

[Открыть интерактив](80_assets/interactive/multigrid-error-modes.html)

![Статическая схема сглаживания и грубой коррекции](80_assets/numerical-analysis/interactive-multigrid-error-modes.svg)

Раздельно меняются сила сглаживания и качество грубой коррекции. Энергия ошибки уменьшается только при совместной работе механизмов.

## Частотные режимы циркулянта

[Открыть интерактив](80_assets/interactive/circulant-fourier-modes.html)

![Статическая схема частотной диагонализации](80_assets/numerical-analysis/interactive-circulant-fourier-modes.svg)

Выбираются частота и спектральный множитель. Переключатель непериодической границы показывает источник артефакта обёртки.

## Иерархическое сжатие

[Открыть интерактив](80_assets/interactive/hierarchical-low-rank-compression.html)

![Статическая схема блочно-малорангового сжатия](80_assets/numerical-analysis/interactive-hierarchical-compression.svg)

Меняются допустимый ранг и размер ближней зоны. Шумоподобный режим показывает потерю сжимаемости при медленном спаде сингулярных чисел.

## Ограничения

Демонстрации показывают механизмы и диагностические величины, но не заменяют доказательства и не воспроизводят конкретный промышленный решатель.

## Связи

- [[30_mathematics/numerical-analysis/tyrtyshnikov-source-map]].
- [[70_labs/figures/tyrtyshnikov-chapters-22-25]].

