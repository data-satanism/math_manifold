---
id: boss-linear-algebra-map
title: "Линейная алгебра Босса: интеграционный маршрут"
aliases: ["Курс линейной алгебры Босса", "Boss linear algebra map"]
type: map
status: canonical
publish: true
areas: [linear-algebra, matrix-analysis, numerical-linear-algebra]
concepts: [linear-map, quadratic-form, canonical-form, matrix-function, matrix-equation, positive-matrix]
prerequisites: [school-algebra, mathematical-analysis]
ai_domains: [representation-learning, optimization, spectral-diagnostics, graph-learning, markov-models]
source_refs:
  - id: boss-linear-algebra-2005
    pages: "10-215"
    role: primary
level: intermediate
created: 2026-07-16
updated: 2026-07-27
---

# Линейная алгебра Босса: интеграционный маршрут

## Принцип курса

Эта карта не создаёт параллельный вводный учебник рядом с [[30_mathematics/numerical-analysis/numerical-linear-algebra-map|численным анализом]]. Она отвечает на другой вопрос: какие алгебраические структуры ещё отсутствуют в графе и какие из них объясняют методы ИИ.

## Решения по главам

1. [[30_mathematics/linear-algebra/modules/01-coordinate-geometry-invariants|Аналитическая геометрия и инварианты]] — геометрический пререквизит.
2. [[30_mathematics/linear-algebra/modules/02-linear-representations-recognition|Векторы, признаки и линейное распознавание]] — новый прикладной слой; рутинные операции остаются `reference-only`.
3. Линейные преобразования — дополнение конечномерной интуиции к [[30_mathematics/functional-analysis/modules/06-linear-operators|линейным операторам]].
4. Квадратичные формы — расширение геометрии гессиана, положительности и сигнатуры.
5. [[30_mathematics/linear-algebra/modules/05-annihilating-polynomials-root-spaces|Аннулирующие многочлены и корневые подпространства]] дополняют жорданову структуру.
6. [[30_mathematics/linear-algebra/modules/06-matrix-functions-linear-dynamics|Функции от матриц и линейная динамика]] расширяют [[30_mathematics/numerical-analysis/modules/03-conditioning-and-matrix-series|матричные ряды]].
7. [[30_mathematics/linear-algebra/modules/07-matrix-equations|Матричные уравнения]] — новый маршрут к уравнениям Сильвестра и Ляпунова.
8. [[30_mathematics/linear-algebra/modules/08-linear-programming-duality-games|Неравенства, конусы и линейное программирование]] дополнены [[30_mathematics/linear-algebra/theorems/gordan-alternative-theorem|теоремой Гордана об альтернативе]].
9. [[30_mathematics/linear-algebra/modules/09-positive-stochastic-matrices|Положительные и стохастические матрицы]] расширяют [[30_mathematics/functional-analysis/modules/12-positive-operators|положительные операторы]] и связывают их с марковскими моделями.
10. Численные методы — `reference-only` относительно курса Тыртышникова, кроме новых вероятностных оценок.
11. Сводка — итоговая карта зависимостей, без повторения доказательств.

## Перенос в ИИ

Канонические формы помогают различать спектральный рост и ненормальный переходный режим; матричные функции возникают в моделях непрерывной глубины и пространства состояний; уравнения Ляпунова проверяют устойчивость; положительные и стохастические матрицы задают марковскую динамику; квадратичные формы описывают локальную геометрию функции потерь.

Полный перечень 82 подразделов: [[30_mathematics/linear-algebra/boss-linear-algebra-source-map|карта источника]]. Карточка книги: [[60_sources/boss-linear-algebra|Босс — линейная алгебра]].

## Текущее покрытие

- главы 1–2: [[30_mathematics/linear-algebra/modules/01-coordinate-geometry-invariants|координатная геометрия]] и [[30_mathematics/linear-algebra/modules/02-linear-representations-recognition|линейное распознавание]];
- главы 3–6 интегрируются через [[30_mathematics/linear-algebra/modules/04-quadratic-forms-canonical-structure|квадратичные формы и каноническую структуру]];
- новый инвариант форм: [[30_mathematics/linear-algebra/theorems/sylvester-law-inertia|закон инерции Сильвестра]];
- новый узел ненормальной структуры: [[30_mathematics/linear-algebra/theorems/jordan-canonical-form|жорданова форма]];
- глава 5: [[30_mathematics/linear-algebra/modules/05-annihilating-polynomials-root-spaces|минимальный многочлен и корневые подпространства]], [[30_mathematics/linear-algebra/theorems/cayley-hamilton-theorem|теорема Кэли—Гамильтона]];
- глава 6: [[30_mathematics/linear-algebra/modules/06-matrix-functions-linear-dynamics|матричная экспонента и линейный поток]];
- глава 8 объединена с материалом Мышкиса в [[30_mathematics/linear-algebra/modules/08-linear-programming-duality-games|модуле линейного программирования]];
- сертификат несовместности: [[30_mathematics/linear-algebra/theorems/gordan-alternative-theorem|теорема Гордана]];
- критерий оптимальности: [[30_mathematics/linear-algebra/theorems/linear-programming-complementary-slackness|дополняющая нежёсткость]];
- перенос в ИИ: [[50_bridges/linear-programming-structured-prediction|двойственные сертификаты и устойчивые к возмущениям смеси]];
- глава 7: [[30_mathematics/linear-algebra/modules/07-matrix-equations|кронекеровы произведения, уравнения Сильвестра и Ляпунова]];
- спектральный критерий: [[30_mathematics/linear-algebra/theorems/sylvester-equation-uniqueness|единственность решения уравнения Сильвестра]];
- перенос в ИИ: [[50_bridges/matrix-equations-control-learning|устойчивость, стационарные ковариации и неявное обучение]];
- глава 9: [[30_mathematics/linear-algebra/modules/09-positive-stochastic-matrices|положительная и марковская динамика]], [[30_mathematics/linear-algebra/theorems/perron-frobenius-theorem|теорема Перрона—Фробениуса]].
