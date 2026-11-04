---
id: cap-volume-unbiased-theorem
title: "Нормировка объёмной выборки и несмещённость регрессии"
aliases: []
type: theorem
status: canonical
publish: true
areas: [numerical-analysis, probability]
concepts: [sampling, least-squares, max-volume]
prerequisites: [cap-05-rectangular-d-optimal]
ai_domains: [compression]
source_refs:
  - id: selection-regression-primary-sources
    pages: "Dereziński–Warmuth 2018: с. 7–11, теоремы 2 и 5"
    role: primary
level: advanced
created: 2026-11-04
updated: 2026-11-04
---

# Несмещённость объёмной регрессии

Пусть $X\in\mathbb R^{n\times d}$ имеет ранг $d$, $d\le s\le n$, $y\in\mathbb R^n$ фиксирован. Для подмножеств размера $s$ положим

$$
p(S)=\frac{\det(X_S^TX_S)}{\binom{n-d}{s-d}\det(X^TX)}.
$$

Это вероятности; вырожденные наборы имеют вероятность ноль. Для невырожденных наборов $\widehat w_S=(X_S^TX_S)^{-1}X_S^Ty_S$ выполняется

$$
\mathbb E_S\widehat w_S=(X^TX)^{-1}X^Ty.
$$

## Доказательство

По Коши–Бине каждый квадратный минор входит ровно в $\binom{n-d}{s-d}$ наборов размера $s$. Отсюда нормировка. Добавим $ty$ в столбец $j$ матрицы $X$. Производная каждого невырожденного определителя информации равна $2\det(X_S^TX_S)\widehat w_{S,j}$. Для вырожденного набора производная нулевая, поскольку определитель — сумма квадратов нулевых в исходной точке миноров. Дифференцируя конечную сумму нормирующего тождества, получаем требуемое среднее для каждой координаты. Полная запись производной — [[30_mathematics/computational-algebra-principles/modules/cap-07-volume-sampling|§3 модуля 07]].

## Граница применения

Для $X=(1,2)^T$, $y=(1,0)^T$, $s=1$ полное решение равно $1/5$, а детерминированный максимум объёма даёт 0. Вероятности $1/5,4/5$ возвращают правильное среднее. Поэтому теорема относится к распределению, а не к одному самому объёмному набору.

![Математическое ожидание решений совпадает с полной регрессией](80_assets/computational-algebra-principles/plots-v2-branches17/cap-07-unbiased-geometry.svg)

[Открыть рисунок в полном размере](80_assets/computational-algebra-principles/plots-v2-branches17/cap-07-unbiased-geometry.svg)

**Установленный результат.** при известной матрице признаков можно выбирать дорогие отклики без знания их значений. Несмещённость не доказывает малую дисперсию, точность каждого ответа или качество на новой генеральной совокупности. Эти вопросы требуют других теорем.

Обратная выборка, точный численный перебор и пять решённых задач — [[30_mathematics/computational-algebra-principles/modules/cap-07-volume-sampling|модуль 07]]. [[60_sources/selection-regression-primary-sources|Первичный источник]].
