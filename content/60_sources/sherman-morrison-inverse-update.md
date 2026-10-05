---
id: source-sherman-morrison-inverse-update
title: "Sherman–Morrison — обновление обратной матрицы"
aliases: ["Исторический источник формулы Sherman–Morrison"]
type: source
status: canonical
publish: true
areas: [numerical-linear-algebra, big-data-algorithms]
concepts: [inverse-matrix, rank-one-update, least-squares]
prerequisites: [linear-algebra]
ai_domains: [linear-regression, online-learning]
source_refs:
  - id: sherman-morrison-inverse-update-1950
    pages: "с. 124–127 — диапазон статьи; формулы по оригиналу не сверены"
    role: historical-origin
level: advanced
created: 2026-10-02
updated: 2026-10-02
---

# Sherman–Morrison — обновление обратной матрицы

Jack Sherman, Winifred J. Morrison. *Adjustment of an Inverse Matrix Corresponding to a Change in One Element of a Given Matrix*. The Annals of Mathematical Statistics, 21(1), 1950, с. 124–127. DOI: [10.1214/aoms/1177729893](https://doi.org/10.1214/aoms/1177729893).

Карточка указывает историческое происхождение имени формулы. Диапазон 124–127 описывает статью целиком, а не координату конкретного утверждения. Полный оригинал в этом этапе не был визуально сверен; номер формулы и её расположение не заявляются.

В [[30_mathematics/big-data-algorithms/modules/bda-04-batch-streaming-least-squares|модуле потоковых наименьших квадратов]] тождество рангового обновления и условия ненулевого знаменателя выводятся самостоятельно. Доказательство не зависит от недоступной страницы исторического оригинала. Положительная определённость начального состояния обеспечивает допустимость соответствующего рекурсивного шага в точной арифметике; численная устойчивость реализации требует отдельной проверки.
