---
id: source-de-lathauwer-multilinear-svd
title: "Де Латхаувер—Де Мур—Вандевалле: многолинейное SVD"
aliases: ["A Multilinear Singular Value Decomposition"]
type: source
status: canonical
publish: true
areas: [tensor-methods, numerical-linear-algebra]
concepts: [hosvd, multilinear-rank, quasioptimality]
prerequisites: []
ai_domains: [model-compression, scientific-machine-learning]
source_refs:
  - id: de-lathauwer-multilinear-svd-2000
    pages: "PDF 15–17; журнальные с. 1267–1269"
    role: primary
level: research
created: 2026-10-02
updated: 2026-10-02
---

# Де Латхаувер—Де Мур—Вандевалле: многолинейное SVD

Lieven De Lathauwer, Bart De Moor, Joos Vandewalle. *A Multilinear Singular Value Decomposition*. SIAM Journal on Matrix Analysis and Applications, 21 (2000), 1253–1278. [DOI](https://doi.org/10.1137/S0895479896305696).

Проверенная версия — [PDF, размещённый на сайте UC Davis](https://www.math.ucdavis.edu/~saito/data/tensor/lathauwer-etal_mulilinear-SVD.pdf), 26 страниц, 251384 байта. SHA-256: `84FB68AC66F7C6E406E12173A0CA6175E1813E1393463B3B6DFE78C40ED1AFAB`. Печатная страница равна PDF-странице плюс 1252.

## Точная опора

Свойство 10 и формула (24): PDF 15, с. 1267. Доказательство и пример 5: PDF 17, с. 1269. Страницы PDF 15–17 сверены визуально. Источник поддерживает оценку ошибки усечения по модам; полный проекторный вывод раскрыт в [[30_mathematics/tensor-methods/theorems/hosvd-quasioptimality|существующей теореме атласа]].

[[30_mathematics/tensor-methods/modules/ten-03-tucker-hosvd|Модуль Tucker/HOSVD]] содержит алгоритм, вычислительную стоимость и пример, различающий квазиоптимальность и точный оптимум. Этот источник не является доказательством сходимости HOOI к глобальному минимуму или гарантией качества сжатой нейросети.

Приватная копия: закрытом архиве. Она не включается в публичный экспорт.
