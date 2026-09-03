---
id: classical-pde-variational-map
title: "Классическая теория уравнений в частных производных и вариационные методы"
aliases: ["Карта курса по PDE и вариационным методам"]
type: map
status: canonical
publish: true
areas: ["partial-differential-equations", "calculus-of-variations", "functional-analysis"]
concepts: ["elliptic-equation", "parabolic-equation", "hyperbolic-equation", "weak-solution", "direct-method", "galerkin-method"]
prerequisites: ["real-analysis-map", "functional-analysis-map", "numerical-linear-algebra-map"]
ai_domains: ["scientific-machine-learning", "neural-operators", "inverse-problems"]
source_refs:
  - id: hunter-pde-notes-2014
    pages: "1–234"
    role: primary
  - id: clason-fem-2021
    pages: "3–112"
    role: primary
  - id: rindler-calculus-variations-2015
    pages: "11–73"
    role: primary
  - id: neural-operator-2021
    pages: "6–59"
    role: bridge
level: research
created: 2026-08-31
updated: 2026-09-03
---
# Классическая теория уравнений в частных производных и вариационные методы

## Назначение курса

Курс строит строгий фундамент для уже существующих материалов по обратным задачам и операторному обучению. Он различает классическое, слабое, вариационное и дискретное решения; связывает тип уравнения с данными, априорной оценкой и режимом распространения информации.

![Эллиптическая, параболическая и гиперболическая геометрии сходятся в пространствах Соболева, вариационных оценках и проверяемом операторе решения](80_assets/pde-variational/gpt-image-v1/pde-course-overview-v1.webp)

## Маршрут из двенадцати модулей

1. [[30_mathematics/classical-pde-variational/modules/pde-01-operator-data-well-posedness|Оператор, данные, тип уравнения и корректность задачи]]
2. [[30_mathematics/classical-pde-variational/modules/pde-02-harmonic-functions-maximum-green|Гармонические функции, принцип максимума и функции Грина]]
3. [[30_mathematics/classical-pde-variational/modules/pde-03-sobolev-weak-compactness|Слабые производные, пространства Соболева, след и компактность]]
4. [[30_mathematics/classical-pde-variational/modules/pde-04-elliptic-weak-lax-milgram|Слабая эллиптическая задача и теорема Лакса—Мильграма]]
5. [[30_mathematics/classical-pde-variational/modules/pde-05-elliptic-regularity-spectrum|Эллиптическая регулярность, компактная резольвента и спектр]]
6. [[30_mathematics/classical-pde-variational/modules/pde-06-heat-kernel-energy-smoothing|Уравнение теплопроводности, ядро, энергия и сглаживание]]
7. [[30_mathematics/classical-pde-variational/modules/pde-07-parabolic-weak-galerkin|Слабые параболические решения и метод Галёркина]]
8. [[30_mathematics/classical-pde-variational/modules/pde-08-wave-energy-domain-dependence|Волновое уравнение, энергия и конечная область зависимости]]
9. [[30_mathematics/classical-pde-variational/modules/pde-09-direct-method-lower-semicontinuity|Прямой метод, коэрцитивность и слабая полунепрерывность]]
10. [[30_mathematics/classical-pde-variational/modules/pde-10-euler-lagrange-constraints-noether|Уравнение Эйлера—Лагранжа, ограничения и симметрии]]
11. [[30_mathematics/classical-pde-variational/modules/pde-11-galerkin-fem-cea-adaptivity|Метод Галёркина, конечные элементы, лемма Сеа и адаптивность]]
12. [[30_mathematics/classical-pde-variational/modules/pde-12-ai-solver-validation-protocol|Протокол проверки нейронного решателя и оператора решения]]

## Новые самостоятельные теоремы

- [[30_mathematics/classical-pde-variational/theorems/harmonic-mean-value-theorem|Теорема о среднем значении для гармонических функций]]
- [[30_mathematics/classical-pde-variational/theorems/elliptic-weak-maximum-principle|Слабый принцип максимума для гармонических и эллиптических функций]]
- [[30_mathematics/classical-pde-variational/theorems/poincare-inequality-h01|Неравенство Пуанкаре в пространстве $H_0^1$]]
- [[30_mathematics/classical-pde-variational/theorems/rellich-kondrachov-compactness|Теорема Реллиха—Кондрашова о компактном вложении]]
- [[30_mathematics/classical-pde-variational/theorems/elliptic-compact-resolvent-spectrum-theorem|Дискретность спектра эллиптического оператора с компактной резольвентой]]
- [[30_mathematics/classical-pde-variational/theorems/heat-energy-uniqueness-theorem|Энергетическое тождество и единственность решения уравнения теплопроводности]]
- [[30_mathematics/classical-pde-variational/theorems/parabolic-galerkin-existence-theorem|Существование слабого параболического решения методом Галёркина]]
- [[30_mathematics/classical-pde-variational/theorems/wave-energy-finite-propagation-theorem|Сохранение энергии и конечная скорость распространения волны]]
- [[30_mathematics/classical-pde-variational/theorems/direct-method-calculus-variations|Теорема существования минимума прямым методом вариационного исчисления]]
- [[30_mathematics/classical-pde-variational/theorems/convex-integral-weak-lsc|Слабая полунепрерывность выпуклого интегрального функционала]]
- [[30_mathematics/classical-pde-variational/theorems/cea-quasioptimality-lemma|Лемма Сеа о квазиоптимальности метода Галёркина]]

## Переиспользованные и расширенные узлы

- [[30_mathematics/numerical-analysis/theorems/coercive-form-existence|Теорема Лакса—Мильграма]] расширяется с симметричного случая до общей коэрцитивной формы.
- [[30_mathematics/real-analysis/theorems/sobolev-embedding|Теорема Соболева о вложении]].
- [[30_mathematics/applied-mathematics/theorems/euler-lagrange-equation|Уравнение Эйлера—Лагранжа]], [[30_mathematics/applied-mathematics/theorems/legendre-jacobi-sufficient-criterion|условия второй вариации]] и [[30_mathematics/applied-mathematics/theorems/noether-variational-symmetry|теорема Нётер]].
- [[30_mathematics/numerical-analysis/methods/galerkin-finite-elements|Метод Галёркина и конечных элементов]].

## Вычислительная и прикладная части

- [[70_labs/classical-pde-variational/pde-variational-labs|Четыре воспроизводимых эксперимента]].
- [[50_bridges/pde-inverse-neural-operators|PDE, обратные задачи и нейронные операторы]].
- [[50_bridges/variational-principles-energy-models|Вариационные принципы и энергетические модели]].
- [[50_bridges/galerkin-neural-operators|Галёркин и обучаемые пространства]].
- [[30_mathematics/operator-learning/opl-map|Прикладной курс по операторному обучению]].

## Редакционный статус

Материалы утверждены владельцем 3 сентября 2026 года и включены в публичный выпуск со статусом `canonical` и `publish: true`.
