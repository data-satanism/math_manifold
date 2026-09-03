---
id: pde-variational-source-map
title: "Карта источников курса по PDE и вариационным методам"
aliases: ["PDE source map"]
type: map
status: canonical
publish: true
areas: ["partial-differential-equations", "calculus-of-variations"]
concepts: ["source-map", "page-coverage", "deduplication"]
prerequisites: ["classical-pde-variational-map"]
ai_domains: ["scientific-communication"]
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
level: research
created: 2026-08-31
updated: 2026-09-03
---
# Карта источников курса по PDE и вариационным методам

Каждый модуль имеет постраничную атрибуцию. Учебный маршрут не дублирует существующие заметки по функциональному анализу, вариационному исчислению, Галёркину и операторному обучению: совпадающие результаты расширяются или переиспользуются ссылками.

| № | Источник | Страницы | Целевой модуль | Статус |
|---:|---|---|---|---|
| 01 | Джон Хантер: конспект по уравнениям в частных производных | 1–18; 91–116; 177–225 | [[30_mathematics/classical-pde-variational/modules/pde-01-operator-data-well-posedness|Оператор, данные, тип уравнения и корректность задачи]] | canonical |
| 02 | Джон Хантер: конспект по уравнениям в частных производных | 19–46 | [[30_mathematics/classical-pde-variational/modules/pde-02-harmonic-functions-maximum-green|Гармонические функции, принцип максимума и функции Грина]] | canonical |
| 03 | Джон Хантер: конспект по уравнениям в частных производных; Кристиан Класон: введение в метод конечных элементов | 47–90; 13–24 | [[30_mathematics/classical-pde-variational/modules/pde-03-sobolev-weak-compactness|Слабые производные, пространства Соболева, след и компактность]] | canonical |
| 04 | Джон Хантер: конспект по уравнениям в частных производных; Кристиан Класон: введение в метод конечных элементов | 91–105; 13–28 | [[30_mathematics/classical-pde-variational/modules/pde-04-elliptic-weak-lax-milgram|Слабая эллиптическая задача и теорема Лакса—Мильграма]] | canonical |
| 05 | Джон Хантер: конспект по уравнениям в частных производных | 105–126 | [[30_mathematics/classical-pde-variational/modules/pde-05-elliptic-regularity-spectrum|Эллиптическая регулярность, компактная резольвента и спектр]] | canonical |
| 06 | Джон Хантер: конспект по уравнениям в частных производных | 127–176 | [[30_mathematics/classical-pde-variational/modules/pde-06-heat-kernel-energy-smoothing|Уравнение теплопроводности, ядро, энергия и сглаживание]] | canonical |
| 07 | Джон Хантер: конспект по уравнениям в частных производных; Кристиан Класон: введение в метод конечных элементов | 177–210; 96–112 | [[30_mathematics/classical-pde-variational/modules/pde-07-parabolic-weak-galerkin|Слабые параболические решения и метод Галёркина]] | canonical |
| 08 | Джон Хантер: конспект по уравнениям в частных производных | 211–234 | [[30_mathematics/classical-pde-variational/modules/pde-08-wave-energy-domain-dependence|Волновое уравнение, энергия и конечная область зависимости]] | canonical |
| 09 | Филип Риндлер: современное вариационное исчисление | 11–24; 68–73 | [[30_mathematics/classical-pde-variational/modules/pde-09-direct-method-lower-semicontinuity|Прямой метод, коэрцитивность и слабая полунепрерывность]] | canonical |
| 10 | Филип Риндлер: современное вариационное исчисление | 19–41 | [[30_mathematics/classical-pde-variational/modules/pde-10-euler-lagrange-constraints-noether|Уравнение Эйлера—Лагранжа, ограничения и симметрии]] | canonical |
| 11 | Кристиан Класон: введение в метод конечных элементов; Джон Хантер: конспект по уравнениям в частных производных | 3–57; 91–105 | [[30_mathematics/classical-pde-variational/modules/pde-11-galerkin-fem-cea-adaptivity|Метод Галёркина, конечные элементы, лемма Сеа и адаптивность]] | canonical |
| 12 | Ковачки и соавторы: нейронные операторы; Ли и соавторы: Фурье-нейронный оператор; Лу и соавторы: DeepONet; Джон Хантер: конспект по уравнениям в частных производных | 6–59; 1–16; 1–22; 91–225 | [[30_mathematics/classical-pde-variational/modules/pde-12-ai-solver-validation-protocol|Протокол проверки нейронного решателя и оператора решения]] | canonical |

## Покрытие источников

- Хантер, гл. 1–8: предварительные сведения, Лаплас, Соболев, эллиптические, параболические и гиперболические задачи.
- Класон, гл. 1–12: вариационная постановка, Галёркин, конечные элементы, оценки и параболические схемы.
- Риндлер, гл. 2–3: прямой метод, выпуклость, уравнение Эйлера—Лагранжа и слабая полунепрерывность.
- Прикладные статьи по нейронным операторам используются только в модуле 12 и существующих связующих страницах.

## Контроль границ

Формулы и номера страниц сверяются по визуальному рендеру исходного PDF. Частные утверждения не распространяются на негладкие области, вырожденные коэффициенты или нелинейные системы без отдельного источника.
