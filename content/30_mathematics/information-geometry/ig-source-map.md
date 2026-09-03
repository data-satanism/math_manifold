---
id: ig-source-map
title: "Карта источников: Информационная геометрия"
aliases: ["Source map ig"]
type: source
status: canonical
publish: true
areas: [information-geometry, differential-geometry, source-mapping]
concepts: [source-coverage, content-overlap]
prerequisites: [ig-course-map]
ai_domains: [probabilistic-modeling, optimization, representation-learning]
source_refs:
  - id: nielsen-information-geometry-2020
    pages: "PDF 1–56"
    role: primary
level: research
created: 2026-08-12
updated: 2026-09-03
---

# Карта источников: Информационная геометрия

| № | Источник и страницы | Целевой модуль | Статус |
|---:|---|---|---|
| 1 | nielsen-information-geometry-2020, PDF 1–10 | [[30_mathematics/information-geometry/modules/ig-01-statistical-manifolds|Статистические модели как многообразия]] | canonical |
| 2 | nielsen-information-geometry-2020, PDF 18–28 | [[30_mathematics/information-geometry/modules/ig-02-fisher-rao-metric|Метрика Фишера—Рао и статистическая различимость]] | canonical |
| 3 | nielsen-information-geometry-2020, PDF 3–18 | [[30_mathematics/information-geometry/modules/ig-03-affine-dual-connections|Аффинные и двойственные связности]] | canonical |
| 4 | nielsen-information-geometry-2020, PDF 13–18 | [[30_mathematics/information-geometry/modules/ig-04-divergences-local-geometry|Дивергенции как генераторы локальной геометрии]] | canonical |
| 5 | nielsen-information-geometry-2020, PDF 14–31 | [[30_mathematics/information-geometry/modules/ig-05-dually-flat-bregman|Двойственно плоские пространства и дивергенции Брэгмана]] | canonical |
| 6 | nielsen-information-geometry-2020, PDF 18–31, 46–52 | [[30_mathematics/information-geometry/modules/ig-06-exponential-mixture-families|Экспоненциальные и смесь-семейства]] | canonical |
| 7 | nielsen-information-geometry-2020, PDF 31–36 | [[30_mathematics/information-geometry/modules/ig-07-natural-gradient|Естественный градиент и координатно-инвариантная оптимизация]] | canonical |
| 8 | nielsen-information-geometry-2020, PDF 36–42 | [[30_mathematics/information-geometry/modules/ig-08-projections-inference-clustering|Геометрические проекции в выводе, проверке гипотез и кластеризации]] | canonical |

## Полное покрытие подразделов

| Источник | Глава и все входящие подразделы | Страницы | Решение или целевые модули |
|---|---|---:|---|
| nielsen-information-geometry-2020 | 1. Введение: обзор и структура | PDF 1–3 | ig-01-statistical-manifolds |
| nielsen-information-geometry-2020 | 2. Дифференциальная геометрия: многообразие, метрика, аффинные связности, ковариантная производная, параллельный перенос, геодезические, кривизна и кручение, Levi–Civita, сравнение с информационной геометрией | PDF 3–10 | ig-01-statistical-manifolds;ig-03-affine-dual-connections |
| nielsen-information-geometry-2020 | 3.1–3.6. Информационные многообразия, сопряжённые связности, статистические многообразия, семейство альфа-связностей, основная теорема, геометрию, порождённую дивергенцией | PDF 10–14 | ig-03-affine-dual-connections;ig-04-divergences-local-geometry |
| nielsen-information-geometry-2020 | 3.7–3.9. Двойственно плоская геометрия и дивергенции Брегмана, гессианова геометрия альфа-связностей, многообразия параметрических семейств | PDF 14–22 | ig-05-dually-flat-bregman;ig-06-exponential-mixture-families |
| nielsen-information-geometry-2020 | 3.10–3.13. Статистическая инвариантность, метрика Фишера—Рао, монотонные вложения и канонические дивергенции Брегмана | PDF 22–31 | ig-02-fisher-rao-metric;ig-05-dually-flat-bregman |
| nielsen-information-geometry-2020 | 4.1. Обычный и естественный градиент, зеркальный спуск, NES | PDF 31–36 | ig-07-natural-gradient |
| nielsen-information-geometry-2020 | 4.2–4.4. Приложения двойственно плоской геометрии, проверка гипотез, кластеризация смесей | PDF 36–40 | ig-08-projections-inference-clustering |
| nielsen-information-geometry-2020 | 5. Выводы, история и перспективы | PDF 40–44 | reference-only |
| nielsen-information-geometry-2020 | A. Оценивание f-дивергенций методом Монте-Карло; B. Многомерное нормальное экспоненциальное семейство | PDF 44–56 | ig-06-exponential-mixture-families |

## Правило покрытия

Каждый указанный диапазон проверяется в исходном PDF. Если соседние подразделы объединены, их границы остаются видимыми в этой таблице и в `source_refs` модуля. Совпадающее содержание расширяет существующий узел или получает ссылку `reference-only`; отдельное определение-дубликат не создаётся.
