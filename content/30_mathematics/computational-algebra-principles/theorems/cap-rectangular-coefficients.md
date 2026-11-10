---
id: cap-rectangular-coefficients-theorem
title: "Коэффициенты восстановления по доминантному прямоугольному блоку"
aliases: []
type: theorem
status: canonical
publish: true
areas: [numerical-analysis, numerical-linear-algebra]
concepts: [max-volume, least-squares]
prerequisites: [cap-01-volume-coefficients]
ai_domains: [compression, scientific-ml]
source_refs:
  - id: selection-regression-primary-sources
    pages: "Михалёв–Оселедец v4: с. 4–6, лемма 4.1 и теорема 4.2"
    role: primary
level: advanced
created: 2026-11-04
updated: 2026-11-04
---

# Коэффициенты прямоугольного восстановления

## Условия и вывод

Пусть $A\in\mathbb R^{n\times r}$ имеет ранг $r$, $r\le s\le n$, $B=A[S,:]$ имеет $s$ строк и ранг $r$. Если любая одиночная замена строки $B$ внешней строкой не увеличивает $\sqrt{\det(B^TB)}$, то для всех $i\notin S$

$$
c_i=a_iB^+,\qquad c_iB=a_i,\qquad
\|c_i\|_2\le\sqrt{\frac r{s+1-r}}.
$$

$c_i$ — решение минимальной евклидовой нормы. Глобальный максимум объёма достаточен, но не необходим.

## Доказательство

Для $H=(B;a_i)$ лемма об определителе даёт $\det(H^TH)=\det(B^TB)(1+\|c_i\|^2)$. По Коши–Бине каждый минор порядка $r$ содержится в $s+1-r$ матрицах после удаления строки, поэтому

$$
 (s+1-r)\det(H^TH)=\sum_{j=1}^{s+1}\det(H_{-j}^TH_{-j})
\le(s+1)\det(B^TB).
$$

Подстановка первого тождества даёт границу. Любое другое решение равно $c_i+z$ с $zB=0$; $c_i\perp z$, значит оно не короче.

## Смысл и граница

При независимом одинаковом шуме выбранных значений с дисперсией $\sigma^2$ дисперсия восстановленного отклика внешней строки равна $\sigma^2\|c_i\|^2$. Это **установленный результат**, условное следствие линейной модели. Граница не относится автоматически к любому набору строк, выбранному процедурой добавления.

Без доминантности даже при $r=s=1$ можно взять $A=(\varepsilon,1)^T$, $B=(\varepsilon)$: коэффициент внешней строки равен $1/\varepsilon$. Для выбранных строк при $s>r$ матрица $BB^+$ — проектор; внешнюю границу на них без доказательства не переносят.

![Изменение модели шума меняет геометрическую информацию](80_assets/computational-algebra-principles/plots-v2-branches17/cap-05-noise-weights.svg)

[Открыть рисунок в полном размере](80_assets/computational-algebra-principles/plots-v2-branches17/cap-05-noise-weights.svg)

> [!example]- Анимация (GIF)
>
> ![Разный шум меняет лучший набор строк](80_assets/course-gif-pca-v2/early/cap-05-noise-weights.gif)
>
> Если дисперсии различаются, вклад каждой строки нужно взвесить. В показанном переборе оптимум переходит от пары 1, 2 к паре 2, 3.
>
> [Открыть GIF в полном размере](80_assets/course-gif-pca-v2/early/cap-05-noise-weights.gif)


*Даже обоснованный объёмный критерий нужно применять к матрице с правильными весами шума. Это отдельная граница статистической интерпретации теоремы.*

Полная геометрия, пример, алгоритм и пять решённых задач — [[30_mathematics/computational-algebra-principles/modules/cap-05-rectangular-d-optimal|в модуле 05]]. [[60_sources/selection-regression-primary-sources|Источник и страницы]].
