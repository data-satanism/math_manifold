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
updated: 2026-11-18
---

# Лаборатория RMT 01. Конечномерный закон Марченко—Пастура

> [!note] Как повторить опыт
> Полный сценарий и перечисленные файлы измерений находятся в авторском хранилище. На сайте доступны описание опыта и опубликованные иллюстрации. Самостоятельная проверка ниже запускается стандартным Python 3.

## Края и нормировка плотности

Вычислим края и массу непрерывной части. При $c=1/4$ ожидаются $1/4$, $9/4$
и масса $1$. При $c=2$ ожидаемая непрерывная масса равна $1/2$, ещё $1/2$ составляет атом в нуле.
Края проверяем с допуском $10^{-12}$, массу по квадратуре — с допуском $10^{-5}$.

```python
from math import pi, sqrt

def measure(c, cells=20000):
    lo, hi = (1 - sqrt(c))**2, (1 + sqrt(c))**2
    step = (hi - lo)/cells
    grid = (lo + step*(i + 0.5) for i in range(cells))
    mass = step*sum(sqrt((x - lo)*(hi - x))/(2*pi*c*x) for x in grid)
    return lo, hi, mass, max(0.0, 1 - 1/c)

lo, hi, mass, atom = measure(0.25)
assert abs(lo - 0.25) < 1e-12 and abs(hi - 2.25) < 1e-12
assert abs(mass + atom - 1) < 1e-5 and atom == 0
print(lo, hi, mass, atom)
lo, hi, mass, atom = measure(2.0)
assert abs(mass - 0.5) < 1e-5 and atom == 0.5
print(lo, hi, mass, atom)
```

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
