---
id: cap-publication-plan
title: Полный маршрут публикаций по вычислительной алгебре
aliases: []
type: map
status: canonical
publish: true
areas:
- numerical-linear-algebra
concepts: []
prerequisites: []
ai_domains:
- compression
- scientific-ml
source_refs: []
level: advanced
created: '2026-11-04'
updated: '2026-11-04'
---

# Полный маршрут вычислительной алгебры

Курс проходит от выбора измерений к выбору координат, модели ошибки и формата представления. Каждый раздел включает точные условия, доказательство или явно обозначенный внешний результат, примеры, контрпримеры и воспроизводимые рисунки.

## 1. Максимальный объём и выбор информации

- [[30_mathematics/computational-algebra-principles/modules/cap-01-volume-coefficients|01. Объём и коэффициенты восстановления: как выбрать достаточную информацию]]
- [[30_mathematics/computational-algebra-principles/modules/cap-02-cross-schur|02. Крест и дополнение Шура: от выбранного блока к оценке ошибки]]
- [[30_mathematics/computational-algebra-principles/modules/cap-03-fekete-interpolation|03. Узлы Фекете: объём, кардинальные функции и устойчивость интерполяции]]
- [[30_mathematics/computational-algebra-principles/papers/cap-malyhin-2025|Малыхин 2025: почему малоранговое приближение единичной матрицы не может быть слишком разреженным]]
- [[30_mathematics/computational-algebra-principles/modules/cap-a04-qr-numerical-rank|А04. QR и численный ранг: ортогональность, выбор столбцов и сильный RRQR]]
- [[30_mathematics/computational-algebra-principles/modules/cap-05-rectangular-d-optimal|05. Прямоугольный объём и D-оптимальный эксперимент]]
- [[30_mathematics/computational-algebra-principles/modules/cap-06-deim|06. DEIM: нелинейность по нескольким координатам]]
- [[30_mathematics/computational-algebra-principles/modules/cap-07-volume-sampling|07. Объёмная случайная выборка и несмещённая регрессия]]

## 2. Геометрия малоранговых моделей

- [[30_mathematics/computational-algebra-principles/modules/cap-g01-fixed-rank-geometry|Г01. Геометрия фиксированного ранга: матрица, факторы и инвариантный шаг]]
- [[30_mathematics/computational-algebra-principles/modules/cap-g02-riemannion|Г02. Riemannion: Muon на многообразии малоранговых адаптеров]]
- [[30_mathematics/computational-algebra-principles/modules/cap-a05-coala|А05. COALA: малоранговое приближение с учётом входов]]
- [[30_mathematics/computational-algebra-principles/modules/cap-a06-orthogonal-procrustes|А06. Ортогональные преобразования, Прокруст и интерполяция]]
- [[30_mathematics/computational-algebra-principles/modules/cap-g04-procrustesgpt|Г04. ProcrustesGPT: согласованный поворот и структурное сжатие]]
- [[30_mathematics/computational-algebra-principles/modules/cap-g05-orthofuse|Г05. OrthoFuse: блочные геодезические и коррекция фаз]]
- [[70_labs/computational-algebra-principles/cap-orthogonal-lab|Лаборатория ортогональных преобразований и сжатия]]

## 3. Общие тензорные факторы

- [[30_mathematics/computational-algebra-principles/modules/cap-g03-sf-tucker|Г03. SF-Tucker: общие подпространства и касательная геометрия]]
- [[30_mathematics/computational-algebra-principles/modules/cap-t01-tt|Т01. Тензорный поезд, ранги разрезов и TT-SVD]]
- [[30_mathematics/computational-algebra-principles/modules/cap-t02-sf-ett|Т02. SF-ETT: общие факторы, TT-ядро и ранговые условия]]
- [[30_mathematics/computational-algebra-principles/modules/cap-t03-cherry-picking|Т03. Cherry-Picking Gradients: крест, производные и выбор индексов]]

## 4. Структурированная статистика

- [[30_mathematics/computational-algebra-principles/modules/cap-s01-structured-covariance|С01. Структурированная ковариация: перестановка, эффективный ранг и статистическая ошибка]]

## 5. Научные вычисления и QTT-FEM

- [[30_mathematics/computational-algebra-principles/modules/cap-q01-qtt-fem|Ч01. QTT-FEM: двоичная сетка, регулярность и многошкальная диффузия]]

## 6. Комплексная геометрия

- [[30_mathematics/computational-algebra-principles/modules/cap-s02-schottky-variation|К01. Модель Шоттки: как вариации генераторов меняют абелевы интегралы]]

## 7. Математические заметки

- [[30_mathematics/computational-algebra-principles/papers/cap-malyhin-2025|Малыхин 2025: почему малоранговое приближение единичной матрицы не может быть слишком разреженным]]
- [[30_mathematics/computational-algebra-principles/modules/journal-01-kashin-two-bases|Два базиса для малых координат: Кашин–Ромский 2023 и ускорение 2025]]
- [[30_mathematics/computational-algebra-principles/modules/journal-02-greedy-projection|Жадный выбор: знак корреляции, проекция словаря и граница сходимости]]

## 8. Общие вычислительные принципы

- [[30_mathematics/computational-algebra-principles/modules/cap-p01-isometric-core|П01. Ортогональность и малое активное ядро]]
- [[30_mathematics/computational-algebra-principles/modules/cap-p02-random-subspace|П02. Поиск подпространства и случайное сжатие]]
- [[30_mathematics/computational-algebra-principles/modules/cap-p03-structure-locality|П03. Структура, локальность связей и порядок переменных]]
- [[30_mathematics/computational-algebra-principles/modules/cap-p04-conditioning|П04. Обусловленность, регуляризация и предобусловливание]]
- [[30_mathematics/computational-algebra-principles/modules/cap-p05-certificates|П05. Информация, сертификаты и правила остановки]]
- [[70_labs/computational-algebra-principles/cap-full-plan-lab|Лаборатория полного цикла: ранги, градиенты и сертификаты]]

## Как читать доказательства и примеры

В карточках источников отмечены версии и прочитанные разделы. Импортированные сложные теоремы названы прямо, а собственные выводы отделены от результатов авторов. В SF-ETT дан альтернативный локальный аргумент для рангов общей конкатенации. В ковариационной оценке отмечено расхождение точной константы вероятностного доказательства. В журнальной ветке сохраняется различие размерностно независимого существования и быстрого построения с логарифмическими потерями.

Лабораторные опыты проверяют малые математические механизмы. Ускорение больших моделей, экспериментальные показатели статей и локальные проверки указываются раздельно.

## Материалы основания

- [[30_mathematics/tyrtyshnikov-video-2026/tva-map|Авторский видеокурс Тыртышникова]]
- [[30_mathematics/computational-algebra-principles/cap-map|Максимальный объём и восстановление]]
- [[30_mathematics/computational-algebra-principles/cap-hse-research-map|Карта направлений по публикациям]]
- [[60_sources/source-cap-tensor-research|Первичные тензорные источники]]
- [[60_sources/source-cap-principles|Источники общего цикла]]
