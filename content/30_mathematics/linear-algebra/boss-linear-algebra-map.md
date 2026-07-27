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

1. Аналитическая геометрия — новый геометрический пререквизит.
2. Векторы и матрицы — `reference-only`, кроме новых примеров распознавания образов.
3. Линейные преобразования — дополнение конечномерной интуиции к [[30_mathematics/functional-analysis/modules/06-linear-operators|линейным операторам]].
4. Квадратичные формы — расширение геометрии гессиана, положительности и сигнатуры.
5. Канонические представления — новые узлы для жордановой формы, аннулирующего многочлена и корневых подпространств.
6. Функции от матриц — расширение [[30_mathematics/numerical-analysis/modules/03-conditioning-and-matrix-series|матричных рядов]] и динамических моделей.
7. [[30_mathematics/linear-algebra/modules/07-matrix-equations|Матричные уравнения]] — новый маршрут к уравнениям Сильвестра и Ляпунова.
8. Неравенства — теоремы об альтернативах, конусы и линейное программирование.
9. Положительные матрицы — расширение [[30_mathematics/functional-analysis/modules/12-positive-operators|положительных операторов]] и связь с марковскими моделями.
10. Численные методы — `reference-only` относительно курса Тыртышникова, кроме новых вероятностных оценок.
11. Сводка — итоговая карта зависимостей, без повторения доказательств.

## Перенос в ИИ

Канонические формы помогают различать спектральный рост и ненормальный переходный режим; матричные функции возникают в моделях непрерывной глубины и пространства состояний; уравнения Ляпунова проверяют устойчивость; положительные и стохастические матрицы задают марковскую динамику; квадратичные формы описывают локальную геометрию функции потерь.

Полный перечень 82 подразделов: [[30_mathematics/linear-algebra/boss-linear-algebra-source-map|карта источника]]. Карточка книги: [[60_sources/boss-linear-algebra|Босс — линейная алгебра]].

## Текущее покрытие

- главы 3–6 интегрируются через [[30_mathematics/linear-algebra/modules/04-quadratic-forms-canonical-structure|квадратичные формы и каноническую структуру]];
- новый инвариант форм: [[30_mathematics/linear-algebra/theorems/sylvester-law-inertia|закон инерции Сильвестра]];
- новый узел ненормальной структуры: [[30_mathematics/linear-algebra/theorems/jordan-canonical-form|жорданова форма]];
- глава 8 объединена с материалом Мышкиса в [[30_mathematics/linear-algebra/modules/08-linear-programming-duality-games|модуле линейного программирования]];
- критерий оптимальности: [[30_mathematics/linear-algebra/theorems/linear-programming-complementary-slackness|дополняющая нежёсткость]];
- AI-перенос: [[50_bridges/linear-programming-structured-prediction|двойственные сертификаты и робастные смеси]].
- глава 7: [[30_mathematics/linear-algebra/modules/07-matrix-equations|кронекеровы произведения, уравнения Сильвестра и Ляпунова]];
- спектральный критерий: [[30_mathematics/linear-algebra/theorems/sylvester-equation-uniqueness|единственность решения уравнения Сильвестра]];
- AI-перенос: [[50_bridges/matrix-equations-control-learning|устойчивость, стационарные ковариации и неявное обучение]].
