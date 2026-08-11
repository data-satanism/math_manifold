---
id: hierarchical-low-rank-matrix-method
title: "Иерархическое блочно-малоранговое представление матрицы"
aliases: ["Иерархическая матрица", "Блочно-малоранговое сжатие"]
type: method
status: canonical
publish: true
areas: [numerical-analysis, numerical-linear-algebra]
concepts: [hierarchical-matrix, cluster-tree, admissibility, low-rank-block]
prerequisites: [hierarchical-matrix-compressibility-theorem]
ai_domains: [kernel-methods, attention, compression]
source_refs:
  - id: tyrtyshnikov-numerical-analysis
    pages: "268-271"
    role: primary
level: research
created: 2026-07-15
updated: 2026-07-27
---

# Иерархическое блочно-малоранговое представление матрицы

## Алгоритмический каркас

1. Построить дерево геометрических кластеров строк и столбцов.
2. Проверить допустимость пары кластеров по расстоянию и диаметру.
3. Для допустимого блока найти $UV^*$ требуемой точности.
4. Недопустимый блок разделить или хранить плотно.
5. Контролировать остаток на каждом уровне.

## Стоимость

При ограниченном ранге и сбалансированном дереве хранение и умножение требуют порядка $O(n\log n)$ операций с множителем, зависящим от ранга.

## Режимы отказа

Случайная или сильно осциллирующая структура не даёт малого ранга; несбалансированное дерево увеличивает глубину; ошибка локальных блоков может накапливаться в требуемой операторной норме.

## Визуализация

![Ближние взаимодействия хранятся точно, а дальние — узкими множителями](80_assets/numerical-analysis/gpt-image-v5/nla-ch25-hierarchical-low-rank-insight.png)

## Источник

[[60_sources/tyrtyshnikov-numerical-analysis|Тыртышников]], §25.3–25.5, стр. 268–271.
