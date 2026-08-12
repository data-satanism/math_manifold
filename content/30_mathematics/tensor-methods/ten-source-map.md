---
id: ten-source-map
title: "Карта источников: Тензорные и малоранговые методы"
aliases: ["Source map ten"]
type: source
status: canonical
publish: true
areas: [tensor-methods, low-rank-methods, source-mapping]
concepts: [source-coverage, content-overlap]
prerequisites: [ten-course-map]
ai_domains: [model-compression, llm, scientific-machine-learning]
source_refs:
  - id: kolda-bader-tensors-2009
    pages: "PDF 1–46; журнальные с. 455–500"
    role: primary
  - id: halko-randomized-matrices-2011
    pages: "PDF 1–74"
    role: primary
level: research
created: 2026-08-12
updated: 2026-08-12
---

# Карта источников: Тензорные и малоранговые методы

| № | Источник и страницы | Целевой модуль | Статус |
|---:|---|---|---|
| 1 | kolda-bader-tensors-2009, PDF 1–9 | [[30_mathematics/tensor-methods/modules/ten-01-multilinear-objects|Тензоры как многолинейные объекты]] | canonical |
| 2 | kolda-bader-tensors-2009, PDF 4–25 | [[30_mathematics/tensor-methods/modules/ten-02-cp-rank|CP-разложение и тензорный ранг]] | canonical |
| 3 | kolda-bader-tensors-2009, PDF 25–36 | [[30_mathematics/tensor-methods/modules/ten-03-tucker-hosvd|Разложение Таккера и HOSVD]] | canonical |
| 4 | kolda-bader-tensors-2009, PDF 36–44 | [[30_mathematics/tensor-methods/modules/ten-04-tensor-networks|Тензорные сети и последовательные разложения]] | canonical |
| 5 | kolda-bader-tensors-2009, PDF 9–25 | [[30_mathematics/tensor-methods/modules/ten-05-identifiability-degeneracy|Идентифицируемость, единственность и вырождение]] | canonical |
| 6 | halko-randomized-matrices-2011, PDF 1–20, 38–63 | [[30_mathematics/tensor-methods/modules/ten-06-randomized-range-finding|Рандомизированный поиск подпространства и SVD]] | canonical |
| 7 | halko-randomized-matrices-2011, PDF 20–38, 64–72; kolda-bader-tensors-2009, PDF 36–44 | [[30_mathematics/tensor-methods/modules/ten-07-completion-cur-sampling|Матричное и тензорное заполнение, CUR и когерентность]] | canonical |
| 8 | kolda-bader-tensors-2009, PDF 1–46; halko-randomized-matrices-2011, PDF 1–74 | [[30_mathematics/tensor-methods/modules/ten-08-low-rank-ai-protocol|Малоранговые методы в обучении и сжатии моделей]] | canonical |

## Полное покрытие подразделов

| Источник | Глава и все входящие подразделы | Страницы | Решение или целевые модули |
|---|---|---:|---|
| kolda-bader-tensors-2009 | 1. Введение | PDF 1–3 | ten-01-multilinear-objects |
| kolda-bader-tensors-2009 | 2. Нотация и предварительные сведения: fibers/slices, rank-one, symmetry, diagonal tensors, matricization, products | PDF 3–9 | ten-01-multilinear-objects |
| kolda-bader-tensors-2009 | 3. CP: rank/border rank, uniqueness, algorithms, computational issues, applications | PDF 9–25 | ten-02-cp-rank;ten-05-identifiability-degeneracy |
| kolda-bader-tensors-2009 | 4. Tucker: compression, n-rank, HOSVD/HOOI, computation, applications | PDF 25–36 | ten-03-tucker-hosvd |
| kolda-bader-tensors-2009 | 5. Другие разложения: INDSCAL, PARAFAC2, CANDELINC, DEDICOM, PARATUCK2 | PDF 36–42 | ten-04-tensor-networks |
| kolda-bader-tensors-2009 | 6–7. Программное обеспечение и выводы | PDF 42–46 | reference-only |
| halko-randomized-matrices-2011 | 1. Введение: двухэтапная схема, fixed-rank/fixed-precision, random sampling, степенная итерация | PDF 1–10 | ten-06-randomized-range-finding |
| halko-randomized-matrices-2011 | 2–3. Обозначения, deterministic framework и преобразование базиса в разложения | PDF 10–20 | ten-06-randomized-range-finding |
| halko-randomized-matrices-2011 | 4–7. Randomized range finder, error estimation, SVD/ID/CUR, single-pass и варианты | PDF 20–38 | ten-06-randomized-range-finding;ten-07-completion-cur-sampling |
| halko-randomized-matrices-2011 | 8–11. Вероятностный анализ гауссовых схем, power scheme и fixed-precision | PDF 38–63 | ten-06-randomized-range-finding |
| halko-randomized-matrices-2011 | 12. Реализация, численные эксперименты и рекомендации | PDF 63–74 | ten-08-low-rank-ai-protocol |

## Правило покрытия

Каждый указанный диапазон проверяется в исходном PDF. Если соседние подразделы объединены, их границы остаются видимыми в этой таблице и в `source_refs` модуля. Совпадающее содержание расширяет существующий узел или получает ссылку `reference-only`; отдельное определение-дубликат не создаётся.
