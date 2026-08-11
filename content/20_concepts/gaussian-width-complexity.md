---
id: gaussian-width-complexity
title: "Гауссовская ширина и эффективная сложность множества"
aliases: ["Гауссовская сложность", "Gaussian width"]
type: concept
status: canonical
publish: true
areas: [probability, high-dimensional-geometry, empirical-processes]
concepts: [gaussian-width, gaussian-complexity, effective-dimension, support-function]
prerequisites: [probability-03-random-vectors-high-dimensions, supremum, convex-hull]
ai_domains: [statistical-learning, compressed-sensing, dimensionality-reduction]
source_refs:
  - id: vershynin-hdp-2026
    pages: "209-214"
    role: primary
level: advanced
created: 2026-07-27
updated: 2026-08-12
---

# Гауссовская ширина и эффективная сложность множества

## Зачем это нужно

Окружающая размерность $n$ часто завышает сложность структурированного множества. Разреженные векторы, низкоранговые матрицы и конечные облака могут занимать большое пространство, но иметь малую геометрическую сложность. Гауссовская ширина измеряет средний экстремальный отклик множества на случайное направление.

## Определение

Для $T\subset\mathbb R^n$

$$
\boxed{
w(T)=\mathbb E\sup_{x\in T}\langle g,x\rangle,
\qquad
g\sim N(0,I_n).
}
$$

Родственная симметричная величина:

$$
\gamma(T)
=
\mathbb E\sup_{x\in T}|\langle g,x\rangle|.
$$

Если $0\in T$, то при естественных условиях

$$
\gamma(T)\asymp w(T).
$$

## Геометрический смысл

В направлении единичного вектора $\theta$ ширина множества — расстояние между двумя опорными гиперплоскостями. Гауссовская ширина усредняет такое измерение по случайным направлениям и дополнительно учитывает случайную длину гауссовского вектора.

## Основные свойства

Для ограниченных множеств:

$$
w(UT+y)=w(T)
$$

для ортогонального $U$ и сдвига $y$;

$$
w(\operatorname{conv}T)=w(T);
$$

$$
w(T+S)=w(T)+w(S);
$$

$$
w(aT)=|a|w(T).
$$

Особенно важно равенство для выпуклой оболочки: ширину определяют экстремальные точки, но не обязательно их число.

## Примеры

$$
w(B_2^n)\asymp\sqrt n,
$$

$$
w(B_1^n)\asymp\sqrt{\log n},
$$

$$
w(B_\infty^n)\asymp n.
$$

Для конечного $T$:

$$
w(T)
\lesssim
\operatorname{diam}(T)\sqrt{\log|T|}.
$$

## Эффективная размерность

Устойчивая версия размерности:

$$
d_{\mathrm{eff}}(T)
\asymp
\frac{w(T)^2}{\operatorname{diam}(T)^2}.
$$

Она может быть намного меньше размерности линейной оболочки и слабо меняется при малых возмущениях множества.

## Вычислительная оценка

Если $T=\{x_1,\ldots,x_N\}$ конечно, можно использовать метод Монте-Карло:

```python
import numpy as np

def gaussian_width(points, draws=2000, seed=71):
    rng = np.random.default_rng(seed)
    g = rng.normal(size=(draws, points.shape[1]))
    return np.mean(np.max(g @ points.T, axis=1))
```

Для непрерывного множества внутренний супремум превращается в задачу оптимизации.

## Перенос в ИИ

- **`established`**: гауссовская ширина входит в оценки случайных проекций, матричных отклонений и восстановления структурированных сигналов.
- **`analogy`**: ширина — среднее число степеней свободы, которые множество показывает случайному измерению.
- **`research hypothesis`**: эмпирическая ширина локального множества представлений может быть полезным индикатором эффективной сложности, но её оценка зависит от способа локализации.

## Режимы отказа

- Ширина не измеряет семантическую сложность напрямую.
- Для неограниченного множества она может быть бесконечной.
- Оценка по конечной выборке может пропустить редкие направления.
- Нельзя заменять ширину только диаметром: множества одинакового диаметра могут иметь ширины, различающиеся как $\sqrt n$.

## Связи

- [[30_mathematics/probability/modules/07-random-processes-gaussian-width|Случайные процессы и гауссовская ширина]].
- [[30_mathematics/probability/theorems/dudley-integral-inequality|Интегральное неравенство Дадли]].
- [[30_mathematics/probability/theorems/matrix-deviation-inequality|Матричное неравенство об отклонении]].
- [[50_bridges/gaussian-width-sample-complexity|Гауссовская ширина и сложность выборки]].

## Источник

- [[60_sources/vershynin-high-dimensional-probability|Роман Вершинин, High-Dimensional Probability]], §7.5, с. 209–214.
