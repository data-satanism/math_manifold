---
id: "source-cap-displacement-structure"
title: "Источники по рангу смещения и сингулярным числам"
aliases: []
type: "source"
status: "canonical"
publish: true
areas: ["numerical-linear-algebra"]
concepts: []
prerequisites: []
ai_domains: ["compression"]
source_refs: []
level: "advanced"
created: "2026-11-06"
updated: "2026-11-06"
---

# Смещение и отделение спектров

T. Kailath, S. Y. Kung, M. Morf, *Displacement Ranks of Matrices and Linear Equations*, Journal of Mathematical Analysis and Applications 68(2), 1979, с. 395–407. Источник введения рангов смещения. Библиография и назначение конструкции проверены по университетской записи. В [[cap-r03-displacement-rank]] граничное представление теплицевой матрицы и восстановление из генераторов выведены напрямую. [Запись Принстонского университета](https://collaborate.princeton.edu/en/publications/displacement-ranks-of-matrices-and-linear-equations/), [издание](https://doi.org/10.1016/0022-247X(79)90124-0).

B. Beckermann, A. Townsend, *On the Singular Values of Matrices with Displacement Structure*, SIAM Journal on Matrix Analysis and Applications 38(4), 2017, с. 1227–1248. В открытом препринте §2 и теорема 2.1 содержат оценку через рациональное разделение спектров. На PDF-страницах 4–5 визуально сверены ранг правой части, индексы сингулярных чисел и нормальность. В §4.2 рассмотрены матрицы Коши. [Препринт](https://arxiv.org/pdf/1609.09494), [издание](https://doi.org/10.1137/16M1096426).

[[cap-rational-displacement-tail|Теоремная заметка]] раскрывает оценку для конкретных полиномов без необходимости находить экстремальную рациональную функцию. Выражение через $q(R)p(R)^{-1}$ оставляет допустимыми нули $q$ на правом спектре. [[cap-r05-displacement-singular-values|Пример с двумя интервалами]] использует собственный простой разделитель, для которого получена оценка $9^{-k}$. Это верхняя оценка данного выбора, оптимальное число Золотарёва не вычислялось.

Пример единичной матрицы относится к точному различию ранга смещения и спада сингулярных чисел. Граница численного разрешения спектра отражена в [[cap-rank-spectrum-lab|лаборатории]].
