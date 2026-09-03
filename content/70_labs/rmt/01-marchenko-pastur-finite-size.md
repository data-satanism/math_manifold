---
id: lab-rmt-marchenko-pastur-finite-size
title: "Лаборатория RMT 01. Конечномерный закон Марченко—Пастура"
aliases: ["RMT lab MP", "Моделирование закона Марченко—Пастура"]
type: lab
status: canonical
publish: true
areas: [random-matrix-theory, scientific-computing]
concepts: [marchenko-pastur-law, spectral-edge-outlier]
prerequisites: [marchenko-pastur-law]
ai_domains: [pca, covariance-estimation, spectral-diagnostics]
source_refs:
  - id: rmt4ml-2022
    pages: "60-74"
    role: primary
level: advanced
created: 2026-07-30
updated: 2026-08-12
---

# Лаборатория RMT 01. Конечномерный закон Марченко—Пастура

## Исследовательский вопрос

Насколько хорошо предельная плотность описывает конечную выборочную ковариацию и почему собственное значение немного выше $E_+$ ещё не является готовым доказательством сигнала?

## Эксперимент

Генерируется $X\in\mathbb R^{p\times n}$ со стандартными гауссовыми элементами, вычисляется спектр $XX^T/n$ и сравнивается с [[30_mathematics/random-matrix-theory/theorems/marchenko-pastur-law|законом Марченко—Пастура]].

```powershell
python 70_labs/rmt/rmt_release_experiments.py `
  --experiment mp `
  --output-dir 80_assets/random-matrix-theory/labs-v1
```

![Конечномерная гистограмма собственных значений выборочной ковариации и предельная плотность Марченко—Пастура с отмеченными краями](80_assets/random-matrix-theory/labs-v1/lab-marchenko-pastur-finite-size.webp)

## Что измерять

- расстояние между эмпирическим верхним краем и $E_+$;
- зависимость ошибки от $p,n$ при фиксированном $p/n$;
- частоту ложных выбросов при наивном пороге $\lambda_{\max}>E_+$.

## Вывод и граница

**Установлено.** Массовая часть спектра приближается к закону Марченко—Пастура.

**Граница.** Для статистического теста крупнейшего собственного значения нужны конечномерные флуктуации и выбранный уровень ошибки, а не только асимптотический край.
