---
id: power-and-subspace-iteration
title: "Степенной метод и итерация подпространства"
aliases: ["Power method", "Subspace iteration"]
type: method
status: canonical
publish: true
areas: [numerical-analysis, numerical-linear-algebra]
concepts: [power-method, subspace-iteration, rayleigh-quotient, orthogonalization]
prerequisites: [nla-02-unitary-matrices-and-svd, qr-factorization-theorem]
ai_domains: [pca, randomized-svd, spectral-normalization]
source_refs:
  - id: tyrtyshnikov-numerical-analysis
    pages: "82-91"
    role: primary
level: advanced
created: 2026-07-14
updated: 2026-07-27
---

# Степенной метод и итерация подпространства

## Задача

Найти доминирующую собственную пару или инвариантное подпространство, используя главным образом умножения на матрицу.

## Алгоритм для одного вектора

$$
y_k=Ax_{k-1},
\qquad
x_k=\frac{y_k}{\|y_k\|_2},
\qquad
\widehat\lambda_k=x_k^*Ax_k.
$$

Критерий остановки должен использовать невязку

$$
r_k=Ax_k-\widehat\lambda_kx_k,
$$

а не только изменение $\widehat\lambda_k$.

## Блочный алгоритм

$$
Y_k=AX_{k-1},
\qquad
Y_k=X_kR_k,
\qquad
B_k=X_k^*AX_k.
$$

Собственные пары малой матрицы $B_k$ дают пары Ритца. Для повышения устойчивости QR выполняют на каждом шаге или через контролируемые интервалы с проверкой $\|I-X_k^*X_k\|_2$.

## Стоимость

Главная операция — $m$ умножений матрицы на вектор. Для разреженного оператора стоимость порядка $O(m\,\mathrm{nnz}(A))$ на шаг; QR для $n\times m$ стоит $O(nm^2)$.

## Условия успеха

- спектральный разрыв $|\lambda_m|>|\lambda_{m+1}|$;
- ненулевая начальная компонента в искомом пространстве;
- достаточная ортогональность столбцов;
- контроль ненормальности и невязок.

## Режимы отказа

Равные модули спектра, плохой старт, схлопывание столбцов и длинный переходный рост для ненормальных матриц. Подробное доказательство: [[30_mathematics/numerical-analysis/theorems/subspace-iteration-convergence|теорема о сходимости]].

## Эксперимент и ИИ

Сравните обычную и блочную итерации на ковариационной матрице. Для PCA измеряйте объяснённую дисперсию, проекционную ошибку и невязки. Высокая объяснённая дисперсия не заменяет проверку качества признаков на целевой задаче.

## Визуализация

![Умножение усиливает ведущие спектральные направления, а QR удерживает несколько независимых компонент](80_assets/numerical-analysis/gpt-image-v2/nla-module-10-subspace-iteration-insight.png)

## Источник

[[60_sources/tyrtyshnikov-numerical-analysis|Тыртышников]], §§9.2–9.10, стр. 82–91.

