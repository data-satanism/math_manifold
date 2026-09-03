---
id: hoeffding-inequality
title: "Неравенство Хёффдинга"
aliases: ["Теорема Хёффдинга", "Hoeffding inequality"]
type: theorem
status: canonical
publish: true
areas: [probability, concentration-of-measure]
concepts: [bounded-random-variable, exponential-moment-method, finite-sample-bound]
prerequisites: [probability-01-refresher, expectation, independence]
ai_domains: [statistical-learning, evaluation, uncertainty]
source_refs:
  - id: vershynin-hdp-2026
    pages: "28-30, 39-41"
    role: primary
level: intermediate
created: 2026-07-27
updated: 2026-08-12
---

# Неравенство Хёффдинга

## Зачем оно нужно

Неравенство Хёффдинга превращает три проверяемых предпосылки — независимость, ограниченность и известный диапазон каждого вклада — в конечновыборочную оценку вероятности ошибки суммы или среднего.

## Формулировка

Пусть $X_1,\ldots,X_n$ — независимые случайные величины и

$$
X_i\in[a_i,b_i]
$$

почти наверное. Тогда для любого $t>0$

$$
\mathbb P\left\{
\sum_{i=1}^n(X_i-\mathbb EX_i)\ge t
\right\}
\le
\exp\left(
-\frac{2t^2}{\sum_{i=1}^n(b_i-a_i)^2}
\right).
$$

Применяя результат к $-X_i$, получаем двустороннюю форму:

$$
\mathbb P\left\{
\left|\sum_{i=1}^n(X_i-\mathbb EX_i)\right|\ge t
\right\}
\le
2\exp\left(
-\frac{2t^2}{\sum_{i=1}^n(b_i-a_i)^2}
\right).
$$

## Геометрическая интуиция

Каждое слагаемое может изменить сумму только внутри известного диапазона. Независимость не даёт всем отклонениям систематически двигаться в одну сторону. Поэтому линейный масштаб неопределённости складывается не как $\sum_i(b_i-a_i)$, а квадратично:

$$
\left(\sum_i(b_i-a_i)^2\right)^{1/2}.
$$

## Доказательство

### Шаг 1. Лемма Хёффдинга

Если $Y\in[a,b]$ и $\mathbb EY=0$, то

$$
\mathbb E e^{\lambda Y}
\le
\exp\left(\frac{\lambda^2(b-a)^2}{8}\right).
$$

Обозначим

$$
\psi(\lambda)=\log\mathbb E e^{\lambda Y}.
$$

Имеем $\psi(0)=0$ и $\psi'(0)=\mathbb EY=0$. Вторая производная равна дисперсии $Y$ относительно экспоненциально наклонённого распределения:

$$
\psi''(\lambda)=\operatorname{Var}_{\lambda}(Y).
$$

Наклонение меняет вероятности, но не меняет диапазон $[a,b]$. Для любой величины в этом диапазоне неравенство Поповичу даёт

$$
\operatorname{Var}_{\lambda}(Y)\le\frac{(b-a)^2}{4}.
$$

Дважды интегрируя оценку $\psi''$, получаем

$$
\psi(\lambda)
\le
\frac{\lambda^2(b-a)^2}{8}.
$$

### Шаг 2. Экспоненциальный момент суммы

Положим

$$
S=\sum_{i=1}^n(X_i-\mathbb EX_i).
$$

Для $\lambda>0$ неравенство Маркова даёт

$$
\mathbb P\{S\ge t\}
\le
e^{-\lambda t}\mathbb E e^{\lambda S}.
$$

### Шаг 3. Использование независимости

Независимость позволяет факторизовать:

$$
\mathbb E e^{\lambda S}
=
\prod_{i=1}^n
\mathbb E e^{\lambda(X_i-\mathbb EX_i)}.
$$

По лемме Хёффдинга

$$
\mathbb E e^{\lambda S}
\le
\exp\left(
\frac{\lambda^2}{8}
\sum_{i=1}^n(b_i-a_i)^2
\right).
$$

Следовательно,

$$
\mathbb P\{S\ge t\}
\le
\exp\left(
-\lambda t+\frac{\lambda^2V}{8}
\right),
\qquad
V=\sum_i(b_i-a_i)^2.
$$

### Шаг 4. Оптимизация

Квадратичная функция по $\lambda$ минимальна при

$$
\lambda_*=\frac{4t}{V}.
$$

Подстановка даёт

$$
-\lambda_*t+\frac{\lambda_*^2V}{8}
=
-\frac{2t^2}{V}.
$$

Теорема доказана.

## Частный случай: среднее ограниченных потерь

Если $0\le\ell_i\le1$ и

$$
\widehat R=\frac1n\sum_i\ell_i,
\qquad
R=\mathbb E\ell_i,
$$

то

$$
\mathbb P\{|\widehat R-R|\ge\varepsilon\}
\le
2e^{-2n\varepsilon^2}.
$$

Для доверия $1-\delta$ достаточно

$$
|\widehat R-R|
\le
\sqrt{\frac{\log(2/\delta)}{2n}}.
$$

## Контрпример при нарушении независимости

Пусть $Z$ принимает значения $\pm1$ с равными вероятностями и $X_i=Z$ для всех $i$. Каждое слагаемое ограничено, но

$$
\sum_iX_i=nZ.
$$

Поэтому

$$
\mathbb P\left\{\left|\sum_iX_i\right|\ge n/2\right\}=1,
$$

тогда как механическое применение независимой оценки предсказало бы экспоненциально малую вероятность. Ограниченности без независимости недостаточно.

## Вычислительный эксперимент

```python
import numpy as np

rng = np.random.default_rng(23)
n, repeats = 200, 100_000
independent = rng.choice([-1, 1], size=(repeats, n)).mean(axis=1)
common = rng.choice([-1, 1], size=repeats)

eps = np.linspace(0.05, 0.5, 20)
tail_independent = [(np.abs(independent) >= e).mean() for e in eps]
tail_common = [(np.abs(common) >= e).mean() for e in eps]
hoeffding = [2 * np.exp(-n * e * e / 2) for e in eps]
```

## Перенос в ИИ

- **`established`**: оценка риска одной заранее фиксированной модели по независимой проверочной выборке ограниченных потерь;
- **`established`**: одновременная оценка конечного заранее заданного семейства после применения оценки объединения;
- **`analogy`**: усреднение независимых датчиков как образ уменьшения неопределённости;
- **`research hypothesis`**: применять ту же границу к модели, многократно выбранной по этой проверочной выборке, без учёта адаптивности.

## Визуализация

![Неравенство Хёффдинга: независимые ограниченные вклады, аналогия с датчиками, оценка риска и отказ при общем шуме](80_assets/probability/gpt-image-v1/hoeffding-inequality-insight-v1.webp)

## Самопроверка

1. Где именно в доказательстве используется независимость?
2. Почему диапазоны входят в квадрате?
3. Как получить двустороннюю форму?
4. Что меняется, если модель выбрана по той же проверочной выборке?

## Источник

- [[60_sources/vershynin-high-dimensional-probability|Вершинин]], теорема 2.2.6 и раздел 2.7, стр. 28–30, 39–41.
