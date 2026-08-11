---
id: visual-complex-analysis-source-map
title: "Карта источника: Visual Complex Analysis"
aliases: ["Source map Нидэма", "Покрытие Нидэма"]
type: map
status: canonical
publish: true
areas: [complex-analysis, source-mapping, geometry]
concepts: [source-coverage, complex-map, conformality, contour-integral]
prerequisites: [visual-complex-analysis-map]
ai_domains: [spectral-methods, geometric-deep-learning, scientific-machine-learning]
source_refs:
  - id: needham-visual-complex-analysis-1997
    pages: "1-570"
    role: primary
level: advanced
created: 2026-07-30
updated: 2026-08-12
---

# Карта источника: Visual Complex Analysis

## Соглашение о страницах

В таблицах указана печатная нумерация книги. В PDF начало первой главы находится на PDF-странице 22, поэтому для основной части действует смещение \(+21\). Формулы и рисунки проверяются по визуальному рендеру PDF, а извлечённый текст используется только для навигации.

Обозначения:

- `R` — покрыто в релизе 1A;
- `E` — расширяет существующий канонический узел;
- `P` — запланировано для релизов 1B или 1C;
- `V` — ключевые исходные рисунки заносятся в визуальный реестр.

## Глава 1. Геометрия и комплексная арифметика, с. 1–54

| Раздел | Страницы | Решение | Целевой узел |
|---|---:|---|---|
| Историческая мотивация, обозначения и геометрическая арифметика | 1–9 | R | `vca-01-complex-geometry` |
| Формула Эйлера: движущаяся точка и степенной ряд | 10–14 | R, V | `thm-euler-formula-geometric` |
| Тригонометрия, геометрия, анализ, алгебра и векторные операции | 14–29 | R | `vca-01-complex-geometry` |
| Преобразования, движения, отражения и подобия | 30–44 | R | `vca-01-complex-geometry` |
| Упражнения | 45–54 | R | модуль 1 и лабораторный эксперимент |

## Глава 2. Комплексные функции как преобразования, с. 55–121

| Раздел | Страницы | Решение | Целевой узел |
|---|---:|---|---|
| Введение: функция как преобразование плоскости | 55–56 | R | `vca-02-functions-transformations` |
| Многочлены, степени и кривые Кассини | 57–63 | R, V | `vca-02-functions-transformations` |
| Степенные ряды, круг сходимости, единственность и операции | 64–78 | R | `vca-02-functions-transformations` |
| Экспонента | 79–83 | R | `vca-02-functions-transformations` |
| Синус, косинус и гиперболические функции | 84–89 | R | `vca-02-functions-transformations` |
| Многозначные функции и ветви | 90–97 | R | `vca-02-functions-transformations` |
| Логарифм и общие степени | 98–101 | R | `vca-02-functions-transformations` |
| Усреднение по многоугольникам и окружностям | 102–110 | R | `vca-02-functions-transformations` |
| Упражнения | 111–121 | R | модуль 2 |

## Глава 3. Преобразования Мёбиуса и инверсия, с. 122–188

| Раздел | Страницы | Решение | Целевой узел |
|---|---:|---|---|
| Определение и разложение на простые преобразования | 122–123 | R | `mobius-transformation` |
| Инверсия: окружности, углы, симметрия и сфера | 124–135 | R, V | `thm-mobius-generalized-circle-preservation` |
| Три геометрических применения инверсии | 136–138 | R | `vca-03-mobius-inversion` |
| Сфера Римана и стереографическая проекция | 139–147 | R, V | `riemann-sphere` |
| Сохранение окружностей, углов и симметрии; группа и неподвижные точки | 148–155 | R | `mobius-transformation` |
| Однородные координаты и матричное представление | 156–161 | R | `vca-03-mobius-inversion` |
| Эллиптический, гиперболический, локсодромический и параболический типы | 162–171 | R, V | `vca-03-mobius-inversion` |
| Разложение в отражения | 172–175 | R | `vca-03-mobius-inversion` |
| Автоморфизмы единичного круга и введение в теорему Римана | 176–180 | R | `vca-03-mobius-inversion` |
| Упражнения | 181–188 | R | модуль 3 |

## Глава 4. Дифференцирование и локальный поворот с масштабированием, с. 189–215

| Раздел | Страницы | Решение | Целевой узел |
|---|---:|---|---|
| Общая локальная деформация и матрица Якоби | 189–193 | R, V | `vca-04-amplitwist-derivative` |
| Комплексная производная как локальное подобие | 194–198 | R, V | `complex-analytic-map` |
| Простые примеры: перенос, умножение, квадрат и сопряжение | 199–200 | R | `vca-04-amplitwist-derivative` |
| Локальная конформность и аналитичность | 200–203 | R, E | `cauchy-riemann-conformality-theorem` |
| Критические и ветвящиеся точки | 204–206 | R | `vca-04-amplitwist-derivative` |
| Условия Коши–Римана | 207–210 | R, E | `cauchy-riemann-conformality-theorem` |
| Упражнения | 211–215 | R | модуль 4 и интерактив Якобиана |

## Глава 5. Дальнейшая геометрия дифференцирования, с. 216–266

| Раздел | Страницы | Решение | Целевой узел |
|---|---:|---|---|
| Декартова и полярная формы условий Коши–Римана | 216–219 | R, E | `vca-05-differentiation-geometry` |
| Аналитическая жёсткость | 219–221 | R | `thm-identity-theorem-analytic-functions` |
| Геометрическое дифференцирование логарифма | 222–223 | R | `vca-05-differentiation-geometry` |
| Правила композиции, обратной функции, суммы и произведения | 223–225 | R | `vca-05-differentiation-geometry` |
| Многочлены, степенные ряды и рациональные функции | 226–228 | R | `vca-05-differentiation-geometry` |
| Степенная и экспоненциальная функции | 229–233 | R | `vca-05-differentiation-geometry` |
| Геометрическое решение \(E'=E\) | 232–234 | R | `thm-euler-formula-geometric` |
| Кривизна при аналитическом отображении | 234–240 | R | `vca-05-differentiation-geometry` |
| Центральные силы и преобразование орбит | 241–246 | R | `vca-05-differentiation-geometry` |
| Аналитическое продолжение, единственность и отражение Шварца | 247–257 | R, V | `thm-identity-theorem-analytic-functions` |
| Упражнения | 258–266 | R | модуль 5 |

## Главы 6–12

| Глава | Страницы | Статус | Целевой модуль |
|---|---:|---|---|
| 6. Неевклидова геометрия | 267–337 | R, V | [[30_mathematics/complex-analysis/modules/06-hyperbolic-geometry]] |
| 7. Числа вращения и топология | 338–376 | R, V | [[30_mathematics/complex-analysis/modules/07-winding-number-topology]] |
| 8. Комплексное интегрирование и теорема Коши | 377–426 | R, V | [[30_mathematics/complex-analysis/modules/08-complex-integration-cauchy]] |
| 9. Формула Коши и приложения | 427–449 | R, V | [[30_mathematics/complex-analysis/modules/09-cauchy-formula-applications]] |
| 10. Векторные поля: физика и топология | 450–471 | R, V | [[30_mathematics/complex-analysis/modules/10-vector-fields-physics-topology]] |
| 11. Векторные поля и комплексное интегрирование | 472–507 | R, V | [[30_mathematics/complex-analysis/modules/11-vector-fields-complex-integrals]] |
| 12. Потоки и гармонические функции | 508–570 | R, V | [[30_mathematics/complex-analysis/modules/12-flows-harmonic-functions]] |

## Контроль полноты курса

- все главы 1–12 имеют модуль и диапазон страниц;
- общие теоремы Коши–Римана не дублируются;
- четыре первых ключевых рисунка уже зарегистрированы в `90_admin/needham_figure_inventory.csv`;
- рисунки глав 6–12 создаются как самостоятельные композиции и регистрируются вместе с визуальным пакетом релиза;
- новые материалы остаются `review` до ручного утверждения.
