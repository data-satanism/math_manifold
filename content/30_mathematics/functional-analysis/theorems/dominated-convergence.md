---
id: thm-dominated-convergence
title: "Теорема Лебега о мажорируемой сходимости"
aliases: ["Dominated convergence theorem"]
type: theorem
status: canonical
publish: true
areas: [measure-theory, functional-analysis]
concepts: [integration, almost-everywhere-convergence]
prerequisites: [lebesgue-integral, fatou-lemma]
ai_domains: [statistical-learning, monte-carlo]
source_refs:
  - id: boss-fa-2005
    pages: "54-61"
    role: primary
level: advanced
created: 2026-07-10
updated: 2026-08-12
---

# Теорема Лебега о мажорируемой сходимости

## Формулировка

Пусть $f_n\to f$ почти всюду и существует интегрируемая функция $g\in L^1$, такая что $|f_n|\le g$ почти всюду для всех $n$. Тогда $f\in L^1$,

$$
\int |f_n-f|\,d\mu\to0,
\qquad
\int f_n\,d\mu\to\int f\,d\mu.
$$

## Доказательство через лемму Фату

1. Из $|f_n|\le g$ и поточечного предела следует $|f|\le g$, значит $f\in L^1$.
2. Рассмотрим неотрицательные функции $2g-|f_n-f|$. Они сходятся почти всюду к $2g$.
3. По лемме Фату
   $$
   \int 2g\le\liminf_n\int(2g-|f_n-f|)
   =\int2g-\limsup_n\int|f_n-f|.
   $$
4. Отсюда $\limsup_n\int|f_n-f|\le0$, то есть $L^1$-сходимость.
5. Наконец,
   $$
   \left|\int f_n-\int f\right|\le\int|f_n-f|\to0.
   $$

## Что ломается без мажоранты

Пусть $f_n=n\mathbf1_{(0,1/n)}$ на $(0,1)$. Тогда $f_n\to0$ почти всюду, но $\int f_n=1$. Масса концентрируется на всё меньшем множестве, и общей $L^1$-мажоранты нет.

## Связь с ИИ

> [!info] established
> Перенос предела через математическое ожидание требует доминирования, равномерной интегрируемости или другого условия. Поточечная сходимость моделей сама по себе не оправдывает предел популяционного риска или градиента ожидания.

## Визуальная схема

![Последовательность функций остаётся под общей интегрируемой мажорантой, поэтому площадь разности исчезает; без мажоранты узкий пик сохраняет единичную массу](80_assets/theorems/gpt-image-v3/dominated-convergence-envelope-v3.png)

> Общая мажоранта запрещает массе «убегать» в узкие пики. Тот же механизм обосновывает перенос предела через математическое ожидание при выполнении условий теоремы.
