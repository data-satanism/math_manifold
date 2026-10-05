---
id: source-lin-projected-gradient-nmf
title: "Lin: проекционный градиент и условия остановки NMF"
aliases: ["Projected Gradient Methods for Nonnegative Matrix Factorization", "KKT для NMF"]
type: source
status: canonical
publish: true
areas: [big-data-algorithms, low-rank-methods, optimization]
concepts: [nonnegative-matrix-factorization, projected-gradient, kkt-conditions]
prerequisites: [nla-02-unitary-matrices-and-svd]
ai_domains: [matrix-factorization, topic-modeling]
source_refs:
  - id: lin-projected-gradient-nmf-2007
    pages: "Авторский PDF 4, 6–7, 14–15; (2), (3), Algorithm 2, Theorem 2, (19)–(21)"
    role: primary
level: advanced
created: 2026-10-05
updated: 2026-10-05
---

# Lin: проекционный градиент и условия остановки NMF

Chih-Jen Lin. *Projected Gradient Methods for Nonnegative Matrix Factorization*. Neural Computation 19(10), 2756–2779, 2007. [Страница автора](https://www.csie.ntu.edu.tw/~cjlin/nmf/); [проверенный авторский PDF](https://www.csie.ntu.edu.tw/~cjlin/papers/pgradnmf.pdf).

Авторский PDF содержит 27 физических страниц. SHA-256 приватной копии закрытом архиве: `dcbd4d257bd9908de84166cbbec4c6e38f34c915cb18368c9e6cfb503652b24d`. Номера далее относятся к этой копии, а не к журнальной пагинации.

Визуально сверены условия оптимальности (2), (3) на PDF 4, точная попеременная схема Algorithm 2 и Theorem 2 на PDF 6–7, проекционный градиент и критерии остановки (19)–(21) на PDF 14–15. Источник различает точное решение неотрицательных подзадач и эвристику, которая сначала решает обычные наименьшие квадраты, а затем обнуляет отрицательные коэффициенты.

[[30_mathematics/big-data-algorithms/modules/bda-06-nmf-als-hals|Модуль NMF]] использует условия KKT для проверки границ допустимой области. Малый проекционный градиент подтверждает приближение к условиям первого порядка при выбранном масштабе факторов; он не доказывает глобального минимума или смысловой интерпретации компонент. При обоих нулевых факторах градиенты тоже равны нулю, хотя ненулевая матрица данных не реконструирована. Поэтому критерий остановки должен сопровождаться проверкой инициализации и значения цели.
