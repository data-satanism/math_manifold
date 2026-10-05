---
id: source-candes-recht-matrix-completion
title: "Candès–Recht: условия точного восстановления матрицы"
aliases: ["Exact Matrix Completion via Convex Optimization", "Candès–Recht и заполнение пропусков"]
type: source
status: canonical
publish: true
areas: [big-data-algorithms, low-rank-methods]
concepts: [matrix-completion, coherence, source-verification]
prerequisites: [nla-02-unitary-matrices-and-svd]
ai_domains: [matrix-factorization, recommender-systems]
source_refs:
  - id: candes-recht-matrix-completion-2008
    pages: "arXiv v1, PDF 3–6: препятствия; Definition 1.2, A0/A1, Theorem 1.3"
    role: primary
level: advanced
created: 2026-10-02
updated: 2026-10-02
---

# Candès–Recht: условия точного восстановления матрицы

Emmanuel J. Candès, Benjamin Recht. *Exact Matrix Completion via Convex Optimization*. Проверенная редакция — [arXiv:0805.4471v1](https://arxiv.org/abs/0805.4471v1), 29 мая 2008 года, 49 PDF-страниц. Это паспорт конкретного препринта; нумерация последующей журнальной версии здесь не используется.

SHA-256 приватной копии закрытом архиве: `4f7703089d806a910bef3d2a306dc71fe5f51187d634e46a1a5f7099fed08d69`. Исходный PDF и рендеры не включаются в учебный экспорт.

Математический исполнитель визуально просмотрел PDF 3–6. На PDF 3–4 независимо проверены примеры препятствий восстановлению: локализованная матрица ранга один и отсутствие наблюдений в строке или столбце. На PDF 6 визуально проверены определение когерентности, условия A0/A1 и Theorem 1.3. Они поддерживают существенную границу: низкий ранг сам по себе не гарантирует восстановления по произвольной маске. Теорема использует случайную выборку наблюдений, ограничения на сингулярные подпространства и достаточное число наблюдений. Её нельзя переносить на произвольную матрицу пользовательских оценок по одному названию «низкоранговая».

[[30_mathematics/big-data-algorithms/modules/bda-05-matrix-completion|Пятый модуль]] отделяет эту вероятностную теорию от самостоятельно доказанного [[30_mathematics/big-data-algorithms/theorems/bda-matrix-completion-identifiability|критерия для ранга один]]. Последний рассматривает фиксированный граф ненулевых наблюдений и не является доказательством Theorem 1.3. Полное доказательство вероятностного результата, включая оценки случайных операторов, в данном учебном блоке не раскрывается.
