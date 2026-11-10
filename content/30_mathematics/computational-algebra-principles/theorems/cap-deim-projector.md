---
id: cap-deim-projector-theorem
title: "DEIM: норма косого проектора и ошибка интерполяции"
aliases: []
type: theorem
status: canonical
publish: true
areas: [numerical-analysis, numerical-linear-algebra]
concepts: [projection, interpolation]
prerequisites: [orthogonal-projection]
ai_domains: [scientific-ml, compression]
source_refs:
  - id: deim-primary-sources
    pages: "Sorensen–Embree v2: с. 7–8, лемма 4.1"
    role: primary
level: advanced
created: 2026-11-04
updated: 2026-11-04
---

# Ошибка косого восстановления DEIM

Пусть $U\in\mathbb R^{n\times m}$, $U^TU=I_m$, $1\le m<n$, $P$ выбирает $m$ различных координат и $B=P^TU$ невырождена. Тогда

$$
D=UB^{-1}P^T,\qquad D^2=D,\quad DU=U,\quad P^TD=P^T,
$$

$$
\|D\|_2=\|I-D\|_2=\|B^{-1}\|_2,\qquad
\|f-Df\|_2\le\|B^{-1}\|_2\|(I-UU^T)f\|_2.
$$

## Доказательство

Первые тождества следуют умножением. Из изометричности $U$ и координатного характера $P$ получаем $\|D\|=\|B^{-1}\|$: верхняя граница очевидна, нижняя достигается на входе $Pz$ для максимизирующего $z$. В базисе $(U,U_\perp)$ проектор имеет вид $(I,K;0,0)$, а его дополнение — $(0,-K;0,I)$. Нормы обоих равны $\sqrt{1+\|K\|^2}$. Наконец, $I-D$ обнуляет $U$, поэтому действует только на $(I-UU^T)f$.

## Контрпример и вычислительный смысл

Для $u=(\varepsilon,\sqrt{1-\varepsilon^2})$ и выбора первой координаты норма равна $1/\varepsilon$. На единичном векторе, ортогональном $u$, граница ошибки достигается. Следовательно, малый остаток SVD без контроля выбранных координат недостаточен.

![Обусловленность выбранной компоненты определяет усиление остатка](80_assets/computational-algebra-principles/plots-v2-branches17/cap-06-amplification.svg)

[Открыть рисунок в полном размере](80_assets/computational-algebra-principles/plots-v2-branches17/cap-06-amplification.svg)

> [!example]- Анимация (GIF)
>
> ![Слабая измеренная компонента усиливает ошибку](80_assets/course-gif-pca-v2/early/cap-06-amplification.gif)
>
> Когда выбранная координата единичного базиса приближается к нулю, косое восстановление всё сильнее увеличивает ортогональный остаток. В этом примере множитель равен $1/|u_1|$.
>
> [Открыть GIF в полном размере](80_assets/course-gif-pca-v2/early/cap-06-amplification.gif)


**Установленный результат.** для доступной по компонентам нелинейности это позволяет оценивать ошибку гиперредукции. Быстрое вычисление выбранных компонент и устойчивость всей динамики — дополнительные условия. Для обучаемых нейросетевых активаций без их проверки связь остаётся **analogy**.

Алгоритм невырожденного выбора, полное геометрическое объяснение и задачи — [[30_mathematics/computational-algebra-principles/modules/cap-06-deim|модуль 06]]. [[60_sources/deim-primary-sources|Источники]].
