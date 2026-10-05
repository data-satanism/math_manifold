---
id: source-demmel-grigori-hoemmen-langou-tsqr
title: "Demmel–Grigori–Hoemmen–Langou — последовательное TSQR"
aliases: ["TSQR и коммуникации QR", "Communication-optimal QR and LU"]
type: source
status: canonical
publish: true
areas: [numerical-linear-algebra, big-data-algorithms]
concepts: [qr-factorization, least-squares, numerical-stability]
prerequisites: [nla-02-unitary-matrices-and-svd]
ai_domains: [linear-regression, distributed-learning]
source_refs:
  - id: demmel-grigori-hoemmen-langou-tsqr-2008
    pages: "PDF 19–21, 46–47; печатные с. 17–19, 44–45"
    role: primary
level: advanced
created: 2026-10-02
updated: 2026-10-02
---

# Demmel–Grigori–Hoemmen–Langou — последовательное TSQR

## Издание и проверенная копия

James Demmel, Laura Grigori, Mark Hoemmen, Julien Langou. *Communication-optimal parallel and sequential QR and LU factorizations*. Технический отчёт UCB/EECS-2008-89, 4 августа 2008 года; LAPACK Working Note 204.

[Официальный PDF в архиве LAPACK](https://www.netlib.org/lapack/lawnspdf/lawn204.pdf) содержит 136 физических страниц. В рассматриваемых разделах физическая PDF-страница равна печатной странице плюс два. SHA-256 проверенной копии: `426cb08133e54f2eb9bedc2367d8e3c2bd3575c78c5c0003ae85f8ea920040c4`.

Приватная копия хранится в закрытом архиве; она и рендеры не входят в публичный экспорт. Этот паспорт относится к техническому отчёту 2008 года. Диапазоны страниц нельзя переносить на последующую журнальную версию без отдельной сверки.

## Роль в новом блоке

- §4.2, печатные с. 17–19, PDF 19–21: последовательное TSQR, объединение текущего треугольного фактора с новым блоком строк; схема алгоритма на Figure 2.
- §10 и Table 12, печатные с. 44–45, PDF 46–47: численная устойчивость и отличие от QR через матрицу Грама.

Страницы визуально сверены математическим исполнителем. Учебный модуль [[30_mathematics/big-data-algorithms/modules/bda-04-batch-streaming-least-squares|пакетных и потоковых наименьших квадратов]] использует эту опору для последовательного ортогонального сжатия. Сохранение функции потерь с преобразованной правой частью выводится непосредственно в модуле.

Полная теория оптимальности коммуникаций, распределённые деревья и универсальные оценки скорости не объявляются раскрытыми. Обратная устойчивость не устраняет чувствительность плохо обусловленной исходной задачи.
