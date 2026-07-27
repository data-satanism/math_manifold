---
id: myshkis-applied-mathematics-source-map
title: "Карта источника: прикладная математика Мышкиса"
aliases: ["Source map Мышкиса", "Карта 32 параграфов прикладной математики"]
type: map
status: canonical
publish: true
areas: [applied-mathematics, source-mapping]
concepts: [source-integration, duplicate-control]
prerequisites: [content-integration-policy]
ai_domains: [scientific-machine-learning]
source_refs:
  - id: myshkis-applied-mathematics-engineers-2006
    pages: "11-671"
    role: primary
level: advanced
created: 2026-07-16
updated: 2026-07-27
---

# Карта источника: прикладная математика Мышкиса

Номера страниц соответствуют печатной нумерации книги. Решение показывает, как параграф войдёт в единый граф знаний: `new` — новый узел, `extend` — дополнение существующего, `reference-only` — только источник и новые примеры.

| Раздел | Параграф | Страницы | Основной вклад | Решение |
|---|---|---:|---|---|
| I.1 | Введение в теорию поля | 11–17 | Скалярные и векторные поля, поток, циркуляция | new |
| I.2 | Оператор Гамильтона | 18–24 | Операции первого и второго порядка, интегральные формулы | new |
| I.3 | Специальные типы полей | 25–36 | Потенциальные и соленоидальные поля, ньютонов потенциал | new |
| II.1 | Введение в аналитические функции | 37–39 | Комплексная структура и область задач | new |
| II.2 | Дифференцирование и отображения | 40–74 | Коши–Риман, конформность, поверхности Римана | new |
| II.3 | Интегрирование и степенные ряды | 75–93 | Интеграл Коши, ряды Лорана и Тейлора | new |
| II.4 | Особые точки и нули | 94–130 | Вычеты, принцип максимума, Руше, эллиптические функции | new |
| II.5 | Асимптотические разложения | 131–146 | Интегралы типа Фурье и метод перевала | extend |
| III.1 | Общая теория операционного исчисления | 147–162 | Прямое и обратное преобразования Лапласа | extend |
| III.2 | Приложения операционного исчисления | 163–173 | ОДУ, разностные, интегральные и дифференциальные уравнения | extend |
| III.3 | Варианты интегральных преобразований | 174–184 | Дискретное преобразование Лапласа и преобразование Фурье | extend |
| IV.1 | Сопряжённые отображения | 186–194 | Инвариантные подпространства и самосопряжённость | extend |
| IV.2 | Квадратичные формы | 195–199 | Инерция, Сильвестр, одновременная диагонализация | extend |
| IV.3 | Структура линейного отображения | 200–213 | Жорданова структура и функции от матриц | extend |
| IV.4 | Некоторые численные методы | 214–229 | Гаусс, обусловленность, Якоби, степенные итерации | reference-only |
| IV.5 | Задачи линейного программирования | 230–250 | Геометрия, улучшение решения и матричные игры | new |
| V.1 | Тензорная алгебра | 252–266 | Евклидовы и аффинные тензоры, метрические формы | new |
| V.2 | Тензорные поля | 267–280 | Ковариантная производная и риманова геометрия | new |
| VI.1 | Первая вариация и необходимые условия | 281–323 | Функционал, вариация, уравнение Эйлера, связи | extend |
| VI.2 | Вторая вариация и достаточные условия | 324–349 | Условия Лежандра и Якоби, собственные значения | extend |
| VI.3 | Канонические уравнения и принципы | 350–391 | Гамильтон–Якоби, Нётер, Гамильтон, устойчивость | new |
| VI.4 | Прямые методы | 392–418 | Ритц, Канторович, Эйлер и приближения функционалов | extend |
| VII.1 | Введение в интегральные уравнения | 419–423 | Классы уравнений и гильбертово пространство | extend |
| VII.2 | Теория Фредгольма | 424–456 | Вырожденные ядра, резольвента, положительные ядра | extend |
| VII.3 | Уравнения с симметричными ядрами | 457–471 | Характеристические числа и самосопряжённость | extend |
| VII.4 | Специальные классы уравнений | 472–495 | Вольтерра, Фредгольм и разностные ядра | extend |
| VII.5 | Сингулярные интегральные уравнения | 496–513 | Формулы обращения и краевые задачи | new |
| VII.6 | Нелинейные интегральные уравнения | 514–530 | Итерации, малый параметр, неподвижная точка | extend |
| VIII.1 | Линейные уравнения и системы | 531–566 | Резонанс, Гамильтоновы системы, асимптотика | new |
| VIII.2 | Автономные системы | 567–599 | Фазовая плоскость, циклы, инварианты, эргодичность | new |
| VIII.3 | Устойчивость решений | 600–628 | Ляпунов, первое приближение, техническая устойчивость | new |
| VIII.4 | Нелинейные колебания | 629–671 | Автоколебания, пограничный слой, усреднение | new |

## Текущее покрытие

- I.1–I.3: [[30_mathematics/applied-mathematics/modules/01-field-theory|модуль теории поля]];
- формула потока: [[30_mathematics/applied-mathematics/theorems/gauss-ostrogradsky|формула Остроградского]];
- формула циркуляции: [[30_mathematics/applied-mathematics/theorems/stokes-theorem|формула Стокса]];
- перенос теории поля в ИИ: [[50_bridges/field-invariants-physics-informed-models|интегральные инварианты в физически информированных моделях]];
- II.1–II.5: [[30_mathematics/applied-mathematics/modules/02-complex-analysis|модуль аналитических функций]];
- локальная геометрия: [[30_mathematics/applied-mathematics/theorems/cauchy-riemann-conformality|условия Коши–Римана и конформность]];
- восстановление по границе: [[30_mathematics/applied-mathematics/theorems/cauchy-integral-formula|интегральная формула Коши]];
- локализация особенностей: [[30_mathematics/applied-mathematics/theorems/residue-theorem|теорема о вычетах]];
- перенос комплексного анализа в ИИ: [[50_bridges/complex-analysis-spectral-learning|контурные спектральные методы]];
- III.1–III.3: [[30_mathematics/applied-mathematics/modules/03-operational-calculus|модуль операционного исчисления]];
- новый метод без дублирования свёртки: [[30_mathematics/applied-mathematics/methods/laplace-transform|метод преобразования Лапласа]];
- существующий узел дополнен односторонней теоремой: [[20_concepts/convolution|свёртка]];
- перенос операционного исчисления в ИИ: [[50_bridges/laplace-state-space-learning|модели пространства состояний и длинные свёртки]].
- IV.1–IV.3: [[30_mathematics/linear-algebra/modules/04-quadratic-forms-canonical-structure|интеграционный модуль о формах и канонической структуре]] без дублирования SVD и общей спектральной теории;
- инвариант формы: [[30_mathematics/linear-algebra/theorems/sylvester-law-inertia|закон инерции Сильвестра]];
- недиагонализируемый случай: [[30_mathematics/linear-algebra/theorems/jordan-canonical-form|жорданова каноническая форма]];
- IV.4: только маршрут в [[30_mathematics/numerical-analysis/numerical-linear-algebra-map|курс численного анализа]];
- IV.5: [[30_mathematics/linear-algebra/modules/08-linear-programming-duality-games|линейное программирование, двойственность и матричные игры]];
- сертификат оптимальности: [[30_mathematics/linear-algebra/theorems/linear-programming-complementary-slackness|дополняющая нежёсткость]];
- перенос в ИИ: [[50_bridges/linear-programming-structured-prediction|структурное предсказание и робастное обучение]].
- V.1–V.2: [[30_mathematics/applied-mathematics/modules/05-tensor-calculus|тензорная алгебра, тензорные поля и риманова геометрия]];
- координатно-согласованная производная: [[30_mathematics/applied-mathematics/theorems/covariant-derivative-tensoriality|тензорность ковариантной производной]];
- перенос в ИИ: [[50_bridges/tensors-geometric-deep-learning|геометрическое глубокое обучение и локальные системы координат]].
- VI.1–VI.4: [[30_mathematics/applied-mathematics/modules/06-calculus-of-variations|вариационное исчисление, канонические принципы и прямые методы]];
- необходимое условие: [[30_mathematics/applied-mathematics/theorems/euler-lagrange-equation|уравнение Эйлера—Лагранжа]];
- достаточный анализ: [[30_mathematics/applied-mathematics/theorems/legendre-jacobi-sufficient-criterion|вторая вариация и сопряжённые точки]];
- симметрия и сохранение: [[30_mathematics/applied-mathematics/theorems/noether-variational-symmetry|теорема Нётер]];
- перенос в ИИ: [[50_bridges/variational-principles-energy-models|энергетические модели, неявные слои и нейронные операторы]].
- VII.1–VII.6: [[30_mathematics/applied-mathematics/modules/07-integral-equations|интегральные уравнения, структурированные ядра и нелинейные модели]];
- точная редукция: [[30_mathematics/applied-mathematics/theorems/degenerate-kernel-finite-rank-reduction|вырожденное ядро и конечномерная система]];
- симметрия и моды: [[30_mathematics/applied-mathematics/theorems/hilbert-schmidt-symmetric-kernel-expansion|спектральное разложение ядра Гильберта—Шмидта]];
- сингулярная граница: [[30_mathematics/applied-mathematics/theorems/sokhotski-plemelj-boundary-values|формулы Сохоцкого—Племеля]];
- перенос в ИИ: [[50_bridges/integral-equations-attention-neural-operators|внимание, низкоранговые ядра и нейронные операторы]].
- VIII.1–VIII.4: [[30_mathematics/applied-mathematics/modules/08-dynamical-systems|линейные и автономные системы, устойчивость и нелинейные колебания]];
- плоская геометрия: [[30_mathematics/applied-mathematics/theorems/poincare-bendixson-trapping-region|теорема Пуанкаре—Бендиксона]];
- энергетический сертификат: [[30_mathematics/applied-mathematics/theorems/lyapunov-direct-stability-method|прямой метод Ляпунова]];
- устойчивость цикла: [[30_mathematics/applied-mathematics/theorems/floquet-multipliers-periodic-orbit|поперечные мультипликаторы Флоке]];
- многомасштабная динамика: [[30_mathematics/applied-mathematics/methods/averaging-slow-amplitude-phase|усреднение амплитуды и фазы]];
- перенос в ИИ: [[50_bridges/dynamical-systems-recurrent-models|рекуррентные модели и нейронные дифференциальные уравнения]].

Всего учтено 42 параграфа. Детальные решения по пересекающимся главам фиксируются в `90_admin/content_overlap_registry.csv`.
