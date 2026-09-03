---
id: subgaussian-norm-concentration
title: "Концентрация нормы субгауссовского случайного вектора"
aliases: ["Теорема о тонком слое", "Subgaussian norm concentration"]
type: theorem
status: canonical
publish: true
areas: [probability, high-dimensional-geometry]
concepts: [thin-shell, subgaussian-vector, euclidean-norm, isotropy]
prerequisites: [bernstein-inequality, subgaussian-subexponential, norm]
ai_domains: [representation-learning, random-features, pca]
source_refs:
  - id: vershynin-hdp-2026
    pages: "59-61"
    role: primary
level: advanced
created: 2026-07-27
updated: 2026-08-12
---

# Концентрация нормы субгауссовского случайного вектора

## Зачем это нужно

В высокой размерности длина случайного вектора часто почти детерминирована. Теорема объясняет, почему облако независимых нормированных признаков сосредоточено около сферы, и одновременно показывает, какие предпосылки нельзя заменять одной изотропностью.

## Формулировка

Пусть

$$
X=(X_1,\ldots,X_d)\in\mathbb R^d
$$

имеет независимые субгауссовские координаты, причём

$$
\mathbb EX_i^2=1.
$$

Обозначим

$$
K=\max_i\|X_i\|_{\psi_2}.
$$

Тогда

$$
\left\|
\|X\|_2-\sqrt d
\right\|_{\psi_2}
\le
CK^2,
$$

где $C$ — абсолютная константа. Эквивалентная хвостовая форма:

$$
\mathbb P\left\{
\left|\|X\|_2-\sqrt d\right|\ge t
\right\}
\le
2\exp\left(-c\frac{t^2}{K^4}\right).
$$

Толщина типичной оболочки не растёт с $d$, тогда как радиус растёт как $\sqrt d$.

## Интуиция

Квадрат нормы — сумма:

$$
\|X\|_2^2=\sum_{i=1}^dX_i^2.
$$

Её ожидание равно $d$. Флуктуация суммы квадратов имеет масштаб $\sqrt d$, но переход от квадрата длины к длине делит отклонение примерно на $2\sqrt d$:

$$
\sqrt{d+O(\sqrt d)}
=
\sqrt d+O(1).
$$

## Доказательство

### Шаг 1. Центрированная сумма квадратов

Положим

$$
Y_i=X_i^2-1.
$$

Тогда $\mathbb EY_i=0$ и

$$
\frac1d\|X\|_2^2-1
=
\frac1d\sum_{i=1}^dY_i.
$$

### Шаг 2. Хвост квадратов

Если $X_i$ субгауссовская, то $X_i^2$ субэкспоненциальна:

$$
\|X_i^2\|_{\psi_1}
=
\|X_i\|_{\psi_2}^2
\le
K^2.
$$

После центрирования

$$
\|Y_i\|_{\psi_1}
\le
CK^2.
$$

### Шаг 3. Бернштейн

Применяя [[30_mathematics/probability/theorems/bernstein-inequality|неравенство Бернштейна]] к коэффициентам $1/d$, получаем

$$
\mathbb P\left\{
\left|\frac1d\|X\|_2^2-1\right|\ge u
\right\}
\le
2\exp\left[
-cd\min\left(
\frac{u^2}{K^4},
\frac{u}{K^2}
\right)
\right].
$$

### Шаг 4. Переход от квадрата нормы к норме

Для $z\ge0$ и $\delta\ge0$:

$$
|z-1|\ge\delta
\quad\Longrightarrow\quad
|z^2-1|\ge\max(\delta,\delta^2).
$$

Берём

$$
z=\frac{\|X\|_2}{\sqrt d}.
$$

Тогда

$$
\mathbb P\left\{
\left|
\frac{\|X\|_2}{\sqrt d}-1
\right|\ge\delta
\right\}
\le
2\exp\left(-c\frac{d\delta^2}{K^4}\right).
$$

После замены $t=\delta\sqrt d$ получаем требуемую хвостовую оценку.

## Почему независимость существенна

Пусть $G\sim\mathcal N(0,I_d)$, а независимая $\xi$ равна $0$ или $\sqrt2$ с вероятностями $1/2$. Для

$$
X=\xi G
$$

имеем $\mathbb EXX^T=I$: вектор изотропен. Каждая линейная проекция субгауссовская. Но половину времени $\|X\|_2=0$, а половину — примерно $\sqrt{2d}$. Тонкого слоя около $\sqrt d$ нет.

Общий множитель создаёт зависимость всех координат.

## Вычислительный эксперимент

```python
import numpy as np

rng = np.random.default_rng(31)
for d in [20, 100, 500, 2000]:
    G = rng.normal(size=(30_000, d))
    r = np.linalg.norm(G, axis=1)
    print(d, r.mean() - np.sqrt(d), r.std())
```

Для контрпримера умножьте каждую строку на независимый общий масштаб $\xi$.

## Перенос в ИИ

- **`established`**: тонкий слой для независимых нормированных субгауссовских признаков;
- **`analogy`**: если длины эмбеддингов мало различаются, направление становится более информативной координатой сходства;
- **`research hypothesis`**: перенос теоремы на обученные эмбеддинги без проверки изотропности, зависимости и хвостов.

Практическая страница: [[50_bridges/thin-shell-embedding-geometry|тонкий слой и геометрия эмбеддингов]].

## Визуализация

![Концентрация нормы: тонкая сферическая оболочка, понятный образ, эмбеддинги и отказ при общем случайном масштабе](80_assets/probability/gpt-image-v1/subgaussian-norm-concentration-insight-v1.webp)

## Самопроверка

1. Почему квадрат координаты становится субэкспоненциальным?
2. Откуда исчезает множитель $\sqrt d$ в толщине оболочки?
3. Почему изотропность не заменяет независимость?
4. Как эмпирически проверить применимость идеи к эмбеддингам?

## Источник

- [[60_sources/vershynin-high-dimensional-probability|Вершинин]], теорема 3.1.1, стр. 59–61.
