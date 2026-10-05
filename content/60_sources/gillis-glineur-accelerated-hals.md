---
id: source-gillis-glineur-accelerated-hals
title: "Gillis–Glineur: ускоренные обновления и HALS для NMF"
aliases: ["Accelerated Multiplicative Updates and Hierarchical ALS", "Первичный источник HALS"]
type: source
status: canonical
publish: true
areas: [big-data-algorithms, low-rank-methods, optimization]
concepts: [nonnegative-matrix-factorization, coordinate-descent, computational-complexity]
prerequisites: [nla-02-unitary-matrices-and-svd]
ai_domains: [matrix-factorization, topic-modeling]
source_refs:
  - id: gillis-glineur-accelerated-hals-2012
    pages: "arXiv:1107.5194v2, PDF 2–4, 8, 11–12"
    role: primary
level: advanced
created: 2026-10-05
updated: 2026-10-05
---

# Gillis–Glineur: ускоренные обновления и HALS для NMF

Nicolas Gillis, François Glineur. *Accelerated Multiplicative Updates and Hierarchical ALS Algorithms for Nonnegative Matrix Factorization*. Neural Computation 24(4), 1085–1105, 2012. [Карточка препринта](https://arxiv.org/abs/1107.5194); [проверенная редакция PDF](https://arxiv.org/pdf/1107.5194v2).

Проверена редакция arXiv:1107.5194v2, 17 физических PDF-страниц. SHA-256 приватной копии закрытом архиве: `aaf334636a8ebd8a5cc6c4789e96150fb511554bed8e77b997549a153825cc28`. Ссылки на страницы ниже относятся к этому препринту, а не к журнальной пагинации.

Визуально сверены постановка и координатные формулы на PDF 2–4, ускоренная схема Algorithm 3 на PDF 8 и обсуждение условий сходимости на PDF 11–12. [[30_mathematics/big-data-algorithms/modules/bda-06-nmf-als-hals|Шестой модуль]] использует статью для вывода HALS и объяснения повторного использования матричных произведений. [[30_mathematics/big-data-algorithms/theorems/bda-hals-coordinate-descent|Самостоятельная теорема]] подробно доказывает один точный подшаг, его уменьшение цели и обработку нулевого знаменателя.

Уменьшение значений цели при последовательных подшагах не даёт права объявить произвольную реализацию глобально оптимальной или автоматически сходящейся к стационарным факторам. Теоретические условия и защита от вырожденных компонент требуют отдельного соблюдения. Результаты скорости из статьи относятся к её алгоритмам, данным и окружению; они не являются измерениями нынешней лаборатории.
