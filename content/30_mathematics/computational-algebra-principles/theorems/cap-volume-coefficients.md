---
id: cap-volume-coefficient-theorem
title: Контроль коэффициентов по объёму выбранных строк
aliases: []
status: canonical
publish: true
areas:
- numerical-analysis
- numerical-linear-algebra
concepts:
- max-volume
- interpolation
- low-rank-approximation
prerequisites: []
ai_domains:
- compression
- scientific-ml
level: advanced
created: '2026-11-03'
updated: '2026-11-03'
type: theorem
source_refs:
- id: maxvol-principles-primary-sources
  pages: Ссылки и границы использования в тексте
  role: primary
---

# Контроль коэффициентов по объёму

![Геометрия коэффициентного контроля через выбранные строки](80_assets/computational-algebra-principles/gpt-image-v1/cap-01-insight.webp)

<a href="80_assets/computational-algebra-principles/gpt-image-v1/cap-01-insight.png" target="_blank" rel="noopener" data-router-ignore>Открыть рисунок в полном размере</a>

> [!example]- Анимация (GIF)
>
> ![Коэффициент измеряет замену опоры](80_assets/course-gif-pca-v2/early/cap-01-insight.gif)
>
> Замена одной опорной строки меняет ориентированный объём в число раз, равное её коэффициенту восстановления. У выбора с максимальным объёмом модуль любого такого коэффициента не больше единицы.
>
> [Открыть GIF в полном размере](80_assets/course-gif-pca-v2/early/cap-01-insight.gif)


## Утверждение

Пусть $U\in\mathbb R^{m\times r}$ имеет полный столбцовый ранг, а $B=U[I,:]$ невырождена. Если замена любой строки $B$ на любую невыбранную строку $U$ увеличивает модуль определителя не более чем в $\tau$ раз, $\tau\ge1$, то для $C=UB^{-1}$

$$

U=CB,\qquad C[I,:]=I_r,\qquad |c_{ij}|\le\tau.

$$

Глобальный максимальный объём даёт частный случай $\tau=1$. Глобальность не является необходимым условием этой теоремы.

## Доказательство

Разложим $u_i=\sum_k c_{ik}b_k$. При замене строки $j$ линейность определителя оставляет только слагаемое с $k=j$: все остальные содержат две одинаковые строки. Поэтому $\det B^{(j\leftarrow i)}=c_{ij}\det B$. Условие на отношение объёмов даёт требуемое ограничение; для выбранных строк коэффициенты — единичная матрица.

## Почему это полезно и чего не следует

При восстановлении скалярных значений $y=U\theta$ из измерений $y_I+\eta$ ошибка равна $C\eta$. Следовательно,

$$

\|C\eta\|_\infty
\le\left(\max_i\sum_j|c_{ij}|\right)\|\eta\|_\infty
\le r\tau\|\eta\|_\infty.

$$

Это контроль линейного восстановления при фиксированной модели. Он не гарантирует минимальной обусловленности или качества предсказаний вне модели.

Матрица со строками $(1,0),(0,1),(0.9,0.9),(0.9,-0.9)$ показывает, что отсутствие улучшающей одиночной замены не означает глобального максимума: первые две строки имеют объём 1, последние — 1.62. При зависимых столбцах невырожденного блока вообще нет.

Подробные вычисления, алгоритм, отрицательные примеры и упражнения: [[30_mathematics/computational-algebra-principles/modules/cap-01-volume-coefficients|модуль 01]]. Графики: [[70_labs/computational-algebra-principles/cap-visual-lab|лаборатория]]. Источник: [Михалёв–Оселедец, §3](https://arxiv.org/html/1502.07838v4#S3). Самостоятельное упражнение: выведите дисперсию ошибки в одной строке при ковариации шума $\sigma^2I$; ответ $\sigma^2\|c_i\|_2^2$.
