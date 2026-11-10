---
id: cap-gaussian-residual-theorem
title: Независимая гауссова проверка остатка
aliases: []
type: theorem
status: canonical
publish: true
areas:
- numerical-linear-algebra
concepts: []
prerequisites: []
ai_domains:
- compression
- scientific-ml
source_refs: []
level: advanced
created: '2026-11-04'
updated: '2026-11-04'
---

# Проверка, независимая от построения

Пусть фиксирован $R\in\mathbb R^{m\times n}$ и $g_1,\ldots,g_s$ независимы со стандартным гауссовым распределением. Пусть также они независимы от всех данных, по которым построен $R$. Тогда для $Z_s=s^{-1}\sum_j\|Rg_j\|^2$ и $0<\eta<1$

$$

\mathbb P\left(|Z_s-\|R\|_F^2|>\eta\|R\|_F^2\right)
\le\min\left(1,\frac{2}{s\eta^2}\right).

$$

## Доказательство

При $R=0$ обе величины равны нулю. Иначе диагонализируем $R^\top R$ с собственными значениями $\lambda_i\ge0$. Ортогональная инвариантность даёт $\|Rg\|^2=\sum_i\lambda_i h_i^2$ с независимыми стандартными $h_i$. Моменты $\mathbb E h_i^2=1$ и $\mathbb E h_i^4=3$ дают среднее $\sum_i\lambda_i=\|R\|_F^2$ и дисперсию $2\sum_i\lambda_i^2\le2\|R\|_F^4$. Независимое усреднение делит дисперсию на $s$. Применяем неравенство Чебышёва.

На событии успеха $\|R\|_2\le\sqrt{Z_s/(1-\eta)}$. Вероятностная верхняя граница контролирует норму, а не только среднее.

## Контрпример к снятию независимости

Пусть $n>s$, выбранные пробы линейно независимы и $R=I-P$, где $P$ — проектор на их линейную оболочку. Тогда $Rg_j=0$ для всех проб, но $R\ne0$ и $\|R\|_2=1$. Поэтому проверку нельзя обучать на тех же направлениях.

![Риск проверки остатка по разным режимам доступа](80_assets/computational-algebra-principles/full-plan-v1/principle-certificate.svg)

[Открыть полный рисунок](80_assets/computational-algebra-principles/full-plan-v1/principle-certificate.svg)

> [!example]- Анимация (GIF)
>
> ![При чтении элементов матрицы без повторений постепенно открываются ячейки, а график сопоставляет вероятность пропуска пика и границу риска гауссовской оценки](80_assets/course-gif-pca-v2/late/principle-certificate.gif)
>
> По мере чтения элементов без повторений уменьшается вероятность пропустить одиночный пик. Для независимых гауссовых произведений график показывает верхнюю границу вероятности ошибки оценки свыше 50 %.
>
> [Открыть GIF в полном размере](80_assets/course-gif-pca-v2/late/principle-certificate.gif)


Правая панель показывает доказанную консервативную границу при $\eta=1/2$. Левый график относится к другому режиму — чтению отдельных элементов. Подробный разбор и адаптивная остановка — [[30_mathematics/computational-algebra-principles/modules/cap-p05-certificates]]. Использование при случайном сжатии — [[30_mathematics/computational-algebra-principles/modules/cap-p02-random-subspace]]. Источники — [[60_sources/source-cap-principles]].
