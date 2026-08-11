---
id: source-lebeau-chatelain-couillet-2025-tensor-approximation
title: "H. Lebeau, F. Chatelain, R. Couillet — A Random Matrix Approach to Low-Multilinear-Rank Tensor Approximation"
aliases: ["Lebeau–Chatelain–Couillet 2025", "RMT for low-multilinear-rank tensors"]
type: source
status: canonical
publish: true
areas: [random-matrix-theory, tensor-methods]
concepts: [spiked-tensor-model, tensor-unfolding, multilinear-svd]
prerequisites: [probability, linear-algebra, singular-value-decomposition]
ai_domains: [tensor-learning, dimensionality-reduction, multimodal-learning]
source_refs:
  - id: lebeau2025tensor
    pages: "1-64 PDF pages"
    role: primary
level: advanced
created: 2026-07-13
updated: 2026-07-27
---

# A Random Matrix Approach to Low-Multilinear-Rank Tensor Approximation

- Авторы: Hugo Lebeau, Florent Chatelain, Romain Couillet.
- Издание: *Journal of Machine Learning Research*, 26, 1–64, 2025; статья 24-0193.
- Лицензия статьи: CC BY 4.0.
- Контрольная сумма SHA-256: `6E8602E810C299E5EDE01CA95E4696A0D46CAC5D24969E4F67BCF36AAC20A66D`.
- Приватная копия: `_private/sources/rmt/additional/rmt-lora.pdf`; в публичный экспорт не входит.

## Что именно установлено

Для общей спайковой тензорной модели работа описывает спектры матричных развёрток, пороги обнаружимости главных направлений и качество усечённого многолинейного SVD. Также дано достаточное условие сходимости итерации высшего порядка с ортогонализацией после спектральной инициализации.

## Карта страниц

- стр. 1–8 PDF: задача низкого многолинейного ранга и вклад статьи;
- стр. 9–12: тензорные определения и инструменты RMT;
- стр. 12–20: спектральный анализ развёрток и качество усечённого многолинейного SVD;
- стр. 20–24: итерация высшего порядка и восстановимость сигнала;
- стр. 26–45: резольвенты, концентрация, детерминированные эквиваленты, выбросы и согласованность собственных векторов.

## Важное замечание об имени файла

Локальное имя `rmt-lora.pdf` вводит в заблуждение: статья посвящена низкому **многолинейному рангу тензора**, а не методу низкоранговой адаптации LoRA. Она не подтверждает выбор ранга LoRA по спектральным выбросам.
