---
id: coordinate-recovery-operator
title: "Оператор восстановления по выбранным координатам"
aliases: []
type: concept
status: canonical
publish: true
areas: [numerical-linear-algebra]
concepts: [projection, interpolation, least-squares]
prerequisites: [orthogonal-projection]
ai_domains: [compression, scientific-ml]
source_refs:
  - id: deim-primary-sources
    pages: "Sorensen–Embree v2: с. 5–8"
    role: primary
  - id: selection-regression-primary-sources
    pages: "Михалёв–Оселедец v4: с. 4–6"
    role: primary
level: advanced
created: 2026-11-04
updated: 2026-11-04
---

# Оператор восстановления по координатам

Пусть $y$ приближённо лежит в известном пространстве $\operatorname{range}U$, $U\in\mathbb R^{n\times r}$, а $P^Ty$ содержит выбранные значения. Если $B=P^TU$ имеет полный столбцовый ранг, восстановление методом наименьших квадратов имеет вид

$$
\widehat y=UB^+P^Ty.
$$

При числе координат $s=r$ это интерполяция: $P^T\widehat y=P^Ty$. При $s>r$ выбранные значения в общем случае воспроизводятся в смысле наименьших квадратов: $P^T\widehat y=BB^+P^Ty$, где $BB^+$ — проектор на образ $B$. Сам оператор $D=UB^+P^T$ всё ещё идемпотентен, поскольку $B^+B=I_r$.

Из $DU=U$ следует $y-Dy=(I-D)e$ для любой записи $y=U\theta+e$. У ошибки есть два независимых источника: насколько хорошо выбрано пространство и насколько сильно оператор восстановления усиливает остаток и шум.

![Косая и ортогональная проекции одной точки на прямую](80_assets/computational-algebra-principles/gpt-image-static-v2/cap-06-oblique-geometry.png)

Для $f=(1,0)$ косой проектор возвращает $(1,2)$ и сохраняет измеренную координату. Ближайшая точка равна $(1/5,2/5)$. Длины остатков отличаются в $\sqrt5$ раз.

[Исходный рисунок](80_assets/computational-algebra-principles/plots-v2-branches17/cap-06-oblique-geometry.svg)

[Открыть рисунок в полном размере](80_assets/computational-algebra-principles/gpt-image-static-v2/cap-06-oblique-geometry.png)

> [!example]- Анимация (GIF)
>
> ![Косая проекция сохраняет координату](80_assets/course-gif-pca-v2/early/cap-06-oblique-geometry.gif)
>
> Когда точка покидает модельную прямую, косая проекция возвращает её вдоль линии с постоянной первой координатой. Ортогональная проекция выбирает ближайшую точку, но меняет эту координату.
>
> [Открыть GIF в полном размере](80_assets/course-gif-pca-v2/early/cap-06-oblique-geometry.gif)


Ортонормальность $U$ позволяет интерпретировать $\|(P^TU)^{-1}\|$ как усиление при квадратной интерполяции; точная [[30_mathematics/computational-algebra-principles/theorems/cap-deim-projector|теорема DEIM]] доказывает это. [[30_mathematics/computational-algebra-principles/theorems/cap-rectangular-coefficients|Прямоугольная теорема]] контролирует нормы внешних строк коэффициентов при доминантности набора.

Контрпример: у $u=(\varepsilon,\sqrt{1-\varepsilon^2})$ выбор первой координаты имеет усиление $1/\varepsilon$. Независимость измерения не равна его устойчивости.

**Установленный результат.** фиксированные линейные пространства применяются в гиперредукции и регрессии с дорогими откликами. Связь с нелинейным обучаемым представлением — **analogy**, пока не ограничены изменение пространства и ошибка модели. Подробнее: [[30_mathematics/computational-algebra-principles/modules/cap-05-rectangular-d-optimal|модуль 05]], [[30_mathematics/computational-algebra-principles/modules/cap-06-deim|модуль 06]], [[30_mathematics/computational-algebra-principles/modules/cap-07-volume-sampling|модуль 07]].
