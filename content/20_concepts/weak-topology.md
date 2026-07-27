---
id: weak-topology
title: "Слабая топология и слабая сходимость"
aliases: ["Weak topology", "Слабая сходимость"]
type: concept
status: canonical
publish: true
areas: [functional-analysis]
concepts: [duality, convergence, compactness]
prerequisites: [topology, linear-functional-duality]
ai_domains: [optimization, probability]
source_refs:
  - id: boss-fa-2005
    pages: "83-84, 95-99"
    role: primary
level: advanced
created: 2026-07-10
updated: 2026-07-27
---

# Слабая топология и слабая сходимость

Последовательность $x_n$ слабо сходится к $x$ в нормированном пространстве $X$, если

$$
f(x_n)\to f(x)\quad\text{для каждого }f\in X^*.
$$

Мы наблюдаем не сами векторы, а все их непрерывные линейные измерения.

## Сильная и слабая сходимость

Сходимость по норме влечёт слабую. Обратное неверно: ортонормированная последовательность $e_n$ в $\ell^2$ слабо сходится к нулю, потому что для любого $y\in\ell^2$ коэффициент $\langle e_n,y\rangle=y_n\to0$, но $\|e_n\|=1$.

Слабая топология полезна тем, что единичный шар рефлексивного банахова пространства слабо компактен. Это часто возвращает подпоследовательности, потерянные в нормовой топологии.

## Граница

Слабая сходимость сохраняет линейные наблюдения, но не обязана сохранять норму: норма лишь слабо полунепрерывна снизу,

$$
x_n\rightharpoonup x\quad\Rightarrow\quad \|x\|\le\liminf_n\|x_n\|.
$$

## Связь с AI

> [!info] established mathematical tool
> В вариационных задачах слабая компактность позволяет доказать существование решения. Интерпретировать слабую сходимость параметров нейросети как сходимость модели можно только после отдельного анализа отображения «параметры → функция».

См. [[20_concepts/compactness]], [[20_concepts/linear-functional-duality]].

