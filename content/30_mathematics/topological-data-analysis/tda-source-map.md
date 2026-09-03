---
id: tda-source-map
title: "Карта источников: Топологический анализ данных и многообразное обучение"
aliases: ["Source map tda"]
type: source
status: canonical
publish: true
areas: [topological-data-analysis, manifold-learning, source-mapping]
concepts: [source-coverage, content-overlap]
prerequisites: [tda-course-map]
ai_domains: [topological-data-analysis, representation-learning, graph-ml]
source_refs:
  - id: otter-persistent-homology-2017
    pages: "PDF 1–45"
    role: primary
level: research
created: 2026-08-12
updated: 2026-09-03
---

# Карта источников: Топологический анализ данных и многообразное обучение

| № | Источник и страницы | Целевой модуль | Статус |
|---:|---|---|---|
| 1 | otter-persistent-homology-2017, PDF 6–10 | [[30_mathematics/topological-data-analysis/modules/tda-01-simplicial-homology|Симплициальные комплексы и гомология]] | canonical |
| 2 | otter-persistent-homology-2017, PDF 10–18 | [[30_mathematics/topological-data-analysis/modules/tda-02-filtrations-vietoris-rips|Фильтрации и комплекс Вьеториса—Рипса]] | canonical |
| 3 | otter-persistent-homology-2017, PDF 10–13, 19–23 | [[30_mathematics/topological-data-analysis/modules/tda-03-persistence-modules-barcodes|Модули персистентности, barcode и диаграммы]] | canonical |
| 4 | otter-persistent-homology-2017, PDF 18–22 | [[30_mathematics/topological-data-analysis/modules/tda-04-boundary-reduction|Матричный алгоритм вычисления персистентности]] | canonical |
| 5 | otter-persistent-homology-2017, PDF 22–24 | [[30_mathematics/topological-data-analysis/modules/tda-05-stability-bottleneck|Устойчивость персистентных диаграмм]] | canonical |
| 6 | otter-persistent-homology-2017, PDF 22–25, 33–34 | [[30_mathematics/topological-data-analysis/modules/tda-06-vectorization-statistics|Векторизация диаграмм и статистическая проверка]] | canonical |
| 7 | otter-persistent-homology-2017, PDF 2–5, 13–18 | [[30_mathematics/topological-data-analysis/modules/tda-07-manifold-learning|Многообразное обучение: от локальных окрестностей к глобальному вложению]] | canonical |
| 8 | otter-persistent-homology-2017, PDF 24–34 | [[30_mathematics/topological-data-analysis/modules/tda-08-topological-ml-protocol|Протокол TDA для данных и нейронных представлений]] | canonical |

## Полное покрытие подразделов

| Источник | Глава и все входящие подразделы | Страницы | Решение или целевые модули |
|---|---|---:|---|
| otter-persistent-homology-2017 | 1–2. Введение и связанные работы | PDF 2–6 | tda-08-topological-ml-protocol |
| otter-persistent-homology-2017 | 3. Симплициальные комплексы, гомология и построение комплексов | PDF 6–10 | tda-01-simplicial-homology |
| otter-persistent-homology-2017 | 4. Персистентная гомология и фильтрованные комплексы | PDF 10–13 | tda-03-persistence-modules-barcodes |
| otter-persistent-homology-2017 | 5.1. Типы данных: сети, изображения и конечные метрические пространства | PDF 14–15 | tda-08-topological-ml-protocol |
| otter-persistent-homology-2017 | 5.2. Комплексы Вьеториса—Рипса, Делоне, альфа-комплексы и комплексы свидетелей; дополнительные методы и способы редукции | PDF 15–19 | tda-02-filtrations-vietoris-rips |
| otter-persistent-homology-2017 | 5.3. От фильтрованного комплекса к штрихкоду: стандартный алгоритм, чтение интервалов и другие алгоритмы | PDF 19–22 | tda-04-boundary-reduction |
| otter-persistent-homology-2017 | 5.4–5.5. Статистическая интерпретация и устойчивость | PDF 22–23 | tda-05-stability-bottleneck;tda-06-vectorization-statistics |
| otter-persistent-homology-2017 | 6. Обобщённая персистентность | PDF 23–24 | tda-03-persistence-modules-barcodes |
| otter-persistent-homology-2017 | 7. Программные средства и сравнительные испытания: наборы данных, вычислительные среды, проверки и выводы | PDF 24–33 | tda-08-topological-ml-protocol |
| otter-persistent-homology-2017 | 8–9. Будущие направления и доступность материалов | PDF 33–45 | reference-only |

## Правило покрытия

Каждый указанный диапазон проверяется в исходном PDF. Если соседние подразделы объединены, их границы остаются видимыми в этой таблице и в `source_refs` модуля. Совпадающее содержание расширяет существующий узел или получает ссылку `reference-only`; отдельное определение-дубликат не создаётся.
