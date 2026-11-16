---
id: pom-map
title: "Популяционная оптимизация на римановых многообразиях"
aliases: ["Разбор монографии Фонга и Тино", "Population-Based Optimization on Riemannian Manifolds"]
type: map
status: canonical
publish: true
areas: [optimization, riemannian-geometry, information-geometry]
concepts: [population-search, stochastic-relaxation, mixture-distributions, rsdfo, grassmann-manifold]
prerequisites: [linear-algebra, calculus, probability]
ai_domains: [numerical-optimization, representation-learning]
source_refs:
  - id: source-fong-tino-population-optimization
    pages: "Главы 1–10, с. 1–165"
    role: primary
level: advanced
created: 2026-11-16
updated: 2026-11-16
---

# Популяционная оптимизация на римановых многообразиях

Фонг и Тино рассматривают поиск, где цель можно измерять в допустимых точках, а собственных производных чёрный ящик не предоставляет. Локальная геометрия определяет, как перенести пробу из касательной плоскости на многообразие. Информационная геометрия описывает семейство распределений, которое генерирует эти пробы. Extended RSDFO объединяет несколько моделей и распределяет поисковые запуски между ними.

Разбор охватывает **10 глав, 38 разделов, 28 подразделов по оглавлению и вложенный пункт 2.2.1.1**. В начале каждой главы есть блок «Простыми словами». Выводы формул, контрпримеры и численные проверки привязаны к печатным страницам.

[Указатель разделов и страниц](30_mathematics/population-optimization-manifolds/pom-source-map) · [Карточка монографии](60_sources/source-fong-tino-population-optimization) · [Геометрическая лаборатория](70_labs/population-optimization-manifolds/pom-geometry-lab)

## Главы

| Глава | Страницы | Основной вопрос |
| --- | --- | --- |
| [1. Две геометрии поиска](30_mathematics/population-optimization-manifolds/chapters/pom-01-introduction) | 1–8 | Чем измерение в центре отличается от качества всей окрестности? |
| [2. Риманова геометрия](30_mathematics/population-optimization-manifolds/chapters/pom-02-riemannian-geometry) | 11–26 | Как получить следующую допустимую точку и перенести туда состояние? |
| [3. Информационная геометрия](30_mathematics/population-optimization-manifolds/chapters/pom-03-information-geometry) | 27–36 | На каком пространстве определены метрика Фишера и две сопряжённые связности? |
| [4. Плотности вероятности](30_mathematics/population-optimization-manifolds/chapters/pom-04-probability-densities) | 37–49 | Какая мера придаёт координатной плотности геометрический смысл? |
| [5. Перенос локальных плотностей](30_mathematics/population-optimization-manifolds/chapters/pom-05-inherited-densities) | 51–66 | Какие свойства статистического семейства сохраняются при переносе? |
| [6. Смеси плотностей](30_mathematics/population-optimization-manifolds/chapters/pom-06-mixture-densities) | 67–85 | Как объединить окрестности и что меняется, когда индекс компоненты скрыт? |
| [7. Геометрия методов оптимизации](30_mathematics/population-optimization-manifolds/chapters/pom-07-geometry-in-optimization) | 89–104 | Как экспонента, логарифм и перенос входят в рой частиц и CMA-ES? |
| [8. Extended RSDFO](30_mathematics/population-optimization-manifolds/chapters/pom-08-rsdfo) | 105–137 | Что гарантирует отбор, как меняются веса и когда можно покрыть всё пространство? |
| [9. Численные эксперименты](30_mathematics/population-optimization-manifolds/chapters/pom-09-experiments) | 139–159 | Как читать результаты на сфере, Грассмане и лестнице Иакова при разных бюджетах? |
| [10. Итоги и исследовательские вопросы](30_mathematics/population-optimization-manifolds/chapters/pom-10-conclusion) | 161–165 | Что нужно знать для общих гарантий и воспроизводимого сравнения? |

## Два маршрута к Extended RSDFO

Чтобы проследить вычисление, начните с главы 2 о геодезическом шаге и главы 8. Сделайте одну локальную пробу, а затем проследите отбор центров, перенормировку весов и обследование границы. В лаборатории каждому переходу соответствует отдельный рисунок или GIF.

Чтобы проверить предпосылки, прочтите главы 3–6 перед главой 8. Различайте плотность относительно площади, её координатную запись и метрику на статистических параметрах. У смеси с перекрытием геометрия наблюдаемых точек и геометрия полной модели с известными метками дают разную информацию о весе. В главе 8 точное сравнение этих объектов позволяет увидеть, где авторский вывод требует усиления.

## Связи с атласом

- [Матричные многообразия в курсе Manopt](30_mathematics/matrix-manifolds-manopt/chapters/mda-03-matrix-manifolds) дают конструкции для реперов, ортогональных проекторов и взвешенных метрик.
- [Маршрут по информационной геометрии](30_mathematics/information-geometry/ig-map) углубляет метрику Фишера, естественный градиент и дивергенции.
- [Курс Manopt целиком](30_mathematics/matrix-manifolds-manopt/mda-map) использует ту же геометрию поиска в задачах многомерного анализа.
