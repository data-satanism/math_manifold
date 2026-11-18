---
id: ten-course-map
title: "Тензорные и малоранговые методы"
aliases: ["Tensor Methods", "Low-rank Methods"]
type: map
status: canonical
publish: true
areas: [tensor-methods, low-rank-methods]
concepts: [learning-path, source-integration, ai-transfer]
prerequisites: [topology, norm, spectrum]
ai_domains: [model-compression, llm, scientific-machine-learning]
source_refs:
  - id: kolda-bader-tensors-2009
    pages: "PDF 1–46; журнальные с. 455–500"
    role: primary
  - id: halko-randomized-matrices-2011
    pages: "PDF 1–74"
    role: primary
level: advanced
created: 2026-08-12
updated: 2026-11-18
---

# Тензорные и малоранговые методы

Курс соединяет строгий математический маршрут с вычислительными экспериментами и явно маркированными переносами в ИИ. Он не создаёт дубликаты общих понятий: нормы, спектр, топология, компактность, свёртка и операторы переиспользуются через существующие канонические узлы.

## Маршрут

1. [[30_mathematics/tensor-methods/modules/ten-01-multilinear-objects|Тензоры как многолинейные объекты]].
2. [[30_mathematics/tensor-methods/modules/ten-02-cp-rank|CP-разложение и тензорный ранг]].
3. [[30_mathematics/tensor-methods/modules/ten-03-tucker-hosvd|Разложение Таккера и HOSVD]].
4. [[30_mathematics/tensor-methods/modules/ten-04-tensor-networks|Тензорные сети и последовательные разложения]].
5. [[30_mathematics/tensor-methods/modules/ten-05-identifiability-degeneracy|Идентифицируемость, единственность и вырождение]].
6. [[30_mathematics/tensor-methods/modules/ten-06-randomized-range-finding|Рандомизированный поиск подпространства и SVD]].
7. [[30_mathematics/tensor-methods/modules/ten-07-completion-cur-sampling|Матричное и тензорное заполнение, CUR и когерентность]].
8. [[30_mathematics/tensor-methods/modules/ten-08-low-rank-ai-protocol|Малоранговые методы в обучении и сжатии моделей]].

## Маршрут с одним расчётом

Сначала проверьте [[30_mathematics/tensor-methods/modules/ten-01-multilinear-objects|порядок индексов развёртки]], затем пройдите [[30_mathematics/tensor-methods/modules/ten-formats-worked-example|один тензор в CP, Таккере и TT]]. На нём вычисляются ранги, один шаг ALS, размеры ядер, остаток и ошибка на входе слоя.

Для единственности прочитайте [[30_mathematics/tyrtyshnikov-video-2026/lectures/tva-08-kruskal-proof|доказательство Крускала]] и [[30_mathematics/tensor-methods/modules/ten-05-identifiability-degeneracy|пример вырождения CP]]. Чтобы восстановить шаг алгоритма на произвольных факторах, переходите к [[30_mathematics/tyrtyshnikov-tensors-2023-2024/lectures/tga-10|лекции об ALS]]. Вычисления собраны в [[70_labs/tensor-methods/stage-4/tensor-stage-4-diagnostics|лаборатории]].

## Карта источников и пересечений

- [[30_mathematics/tensor-methods/ten-source-map|Постраничная карта источников]].
- Правила устранения дубликатов заданы в административном документе `90_admin/content-integration-policy.md`.
