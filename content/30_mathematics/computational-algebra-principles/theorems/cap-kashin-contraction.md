---
id: cap-kashin-contraction-theorem
title: "Два базиса: геометрическое сжатие остатка и малые координаты"
aliases: []
type: theorem
status: canonical
publish: true
areas: [functional-analysis, numerical-linear-algebra]
concepts: [greedy-approximation, quantization]
prerequisites: [orthogonal-projection]
ai_domains: [compression]
source_refs:
  - id: kashin-two-bases-primary-sources
    pages: "Кашин–Ромский: с. 945–946, теорема 1; Кашин–Оселедец–Рудиков: с. 436–437"
    role: primary
level: advanced
created: 2026-11-04
updated: 2026-11-04
---

# Сжатие остатка в словаре двух кубов

Пусть $T$ ортогонален и для всех $z$

$$
\max(\|z\|_1,\|Tz\|_1)\ge\beta_N\|z\|_2,\quad0<\beta_N\le\sqrt N.
$$

Выбираем максимальный по корреляции атом из $Q_N\cup T^TQ_N$, где $Q_N=\{-1,1\}^N$, и вычитаем его ортогональную проекцию. Для $\|x\|\le1$, $q_N=\sqrt{1-\beta_N^2/N}$ после $k$ шагов

$$
\|x-u_k-v_k\|_2\le q_N^k,\qquad
\max(\|u_k\|_\infty,\|Tv_k\|_\infty)\le\frac1{\sqrt N(1-q_N)}.
$$

## Доказательство

Максимальная корреляция равна $\max(\|z\|_1,\|Tz\|_1)$, поскольку максимум на кубе достигается на знаковом векторе. У каждого атома квадрат нормы $N$. Коэффициент проекции равен $\lambda=\langle z,w\rangle/N$, и

$$
\|z-\lambda w\|^2=\|z\|^2-\langle z,w\rangle^2/N\le q_N^2\|z\|^2.
$$

Кроме того, $\lambda_j\le q_N^{j-1}/\sqrt N$. Суммируем отдельно атомы первого и второго кубов: в соответствующем базисе их координаты равны $\pm\lambda_j$. Геометрическая сумма даёт вторую границу.

## Что существенно

Если $\beta_N=c\sqrt N$, $q_N$ не зависит от размерности. Для быстрого знакового оператора статьи 2025 используется другая предпосылка: $\beta_N=R(N)/(K\sqrt2)$, поэтому скорость и координатная константа имеют полилогарифмическую зависимость. Само применение быстрого преобразования не доказывает прежнюю сильную оценку.

При $T=I$ и $x=e_1$ точное разложение с обеими нормами не выше $C/\sqrt N$ требует $C\ge\sqrt N/2$. Это исключает размерностно независимую гарантию для произвольной пары одинаковых базисов.

![Остатки плотного и быстрого вариантов на одном собственном входе](80_assets/computational-algebra-principles/plots-v2-branches17/journal-01-kashin-residual.svg)

[Открыть рисунок в полном размере](80_assets/computational-algebra-principles/plots-v2-branches17/journal-01-kashin-residual.svg)

> [!example]- Анимация (GIF)
>
> ![Уменьшение нормы и изменение координат остатка при разложении синтетического вектора плотным и быстрым операторами](80_assets/course-gif-pca-v2/late/journal-01-kashin-residual.gif)
>
> Два оператора разлагают один синтетический вектор. Точки показывают вычисленные остатки, а их нормы после 45 шагов в обоих случаях ниже $10^{-8}$.
>
> [Открыть GIF в полном размере](80_assets/course-gif-pca-v2/late/journal-01-kashin-residual.gif)


**Established, условное следствие:** малый диапазон упрощает равномерное квантование двух координатных векторов. Выигрыш в полном числе битов и влияние на обучение модели не следуют из теоремы; применение к сжатию градиентов требует отдельного опыта.

Спектральное доказательство быстрого варианта, вычислительная стоимость, границы вероятности и задачи — [[30_mathematics/computational-algebra-principles/modules/journal-01-kashin-two-bases|в модуле]]. [[60_sources/kashin-two-bases-primary-sources|Источники]].
