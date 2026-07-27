---
id: applied-mathematics-map
title: "Прикладная математика для инженеров и ИИ"
aliases: ["Курс Мышкиса", "Applied mathematics for engineers"]
type: map
status: canonical
publish: true
areas: [applied-mathematics, complex-analysis, tensor-analysis, calculus-of-variations, integral-equations, dynamical-systems]
concepts: [vector-field, complex-analysis, laplace-transform, tensor, variational-principle, integral-equation, stability]
prerequisites: [mathematical-analysis, linear-algebra, differential-equations]
ai_domains: [scientific-machine-learning, neural-operators, dynamical-systems, control, inverse-problems, geometric-deep-learning]
source_refs:
  - id: myshkis-applied-mathematics-engineers-2006
    pages: "11-671"
    role: primary
level: advanced
created: 2026-07-16
updated: 2026-07-27
---

# Прикладная математика для инженеров и ИИ

## Замысел курса

Курс показывает, как одна и та же математическая структура проходит четыре стадии: геометрическое описание, дифференциальная или интегральная модель, вычислительная схема и проверяемый механизм в системе машинного обучения. Физическая аналогия используется для понимания, но не подменяет условия теоремы.

## Маршрут

1. [[30_mathematics/applied-mathematics/modules/01-field-theory|**Теория поля**]] — градиент, дивергенция, ротор, интегральные инварианты и восстановление поля.
2. [[30_mathematics/applied-mathematics/modules/02-complex-analysis|**Аналитические функции**]] — конформные отображения, вычеты, принцип максимума и асимптотические методы.
3. [[30_mathematics/applied-mathematics/modules/03-operational-calculus|**Операционное исчисление**]] — преобразования Лапласа и Фурье как координаты линейной динамики.
4. **Линейная алгебра и линейное программирование** — [[30_mathematics/linear-algebra/modules/04-quadratic-forms-canonical-structure|квадратичные формы и каноническая структура]] плюс [[30_mathematics/linear-algebra/modules/08-linear-programming-duality-games|двойственность и матричные игры]], без повторения [[30_mathematics/numerical-analysis/numerical-linear-algebra-map|курса численного анализа]].
5. [[30_mathematics/applied-mathematics/modules/05-tensor-calculus|**Тензоры**]] — координатно-инвариантное описание, ковариантное дифференцирование и геометрия.
6. [[30_mathematics/applied-mathematics/modules/06-calculus-of-variations|**Вариационное исчисление**]] — первая и вторая вариации, уравнение Эйлера—Лагранжа, критерий Якоби, теорема Нётер и прямые методы.
7. [[30_mathematics/applied-mathematics/modules/07-integral-equations|**Интегральные уравнения**]] — Фредгольм, Вольтерра, симметричные и сингулярные ядра, нелинейные уравнения.
8. [[30_mathematics/applied-mathematics/modules/08-dynamical-systems|**Динамические системы**]] — фазовые портреты, устойчивость Ляпунова, периодические режимы, быстро-медленные системы и нелинейные колебания.

## Контроль дублирования

Глава IV не воспроизводит заново нормы, SVD, спектральные итерации и обусловленность. Глава VII расширяет [[30_mathematics/functional-analysis/modules/09-operator-equations|операторные уравнения]] специальными классами ядер и инженерными моделями, но не создаёт вторую формулировку альтернативы Фредгольма. Вариационное исчисление связывается с [[30_mathematics/functional-analysis/modules/11-nonlinear-frechet|производной Фреше]] и [[30_mathematics/numerical-analysis/modules/23-operator-equations-fem-galerkin|методом Галёркина]].

## Мосты к ИИ

- [[50_bridges/field-invariants-physics-informed-models|интегральные инварианты поля → физически информированные модели и контроль законов сохранения]];
- [[50_bridges/complex-analysis-spectral-learning|комплексная аналитичность → спектральные представления и устойчивость продолжения]];
- [[50_bridges/laplace-state-space-learning|преобразование Лапласа → линейные динамические слои и модели пространства состояний]];
- [[50_bridges/linear-programming-structured-prediction|линейное программирование → структурное предсказание, двойственные сертификаты и робастные смеси]];
- [[50_bridges/variational-principles-energy-models|вариационный принцип → энергетические модели, неявные слои и нейронные операторы]];
- [[50_bridges/integral-equations-attention-neural-operators|интегральные уравнения → внимание, низкоранговые ядра и нейронные операторы]];
- [[50_bridges/tensors-geometric-deep-learning|тензорная ковариантность → эквивариантные и геометрические нейронные сети]];
- [[50_bridges/dynamical-systems-recurrent-models|динамические системы → рекуррентные модели, нейронные дифференциальные уравнения и устойчивое обучение]].

Каждая созданная связь сопровождается точной сохраняемой структурой, диагностикой и границей применимости. Карта покрытия источника: [[30_mathematics/applied-mathematics/myshkis-applied-mathematics-source-map|все 42 параграфа]]. Карточка книги: [[60_sources/myshkis-applied-mathematics-engineers|Мышкис — Прикладная математика для инженеров]].
