---
id: bridge-hilbert-rkhs
title: "Гильбертовы пространства → RKHS, ядра и гауссовские процессы"
aliases: ["Гильбертовы пространства и ядра", "Мост к RKHS"]
type: application
status: canonical
publish: true
areas: [functional-analysis, kernel-methods]
concepts: [hilbert-space, riesz-representation, reproducing-kernel]
prerequisites: [hilbert-space, thm-riesz-representation]
ai_domains: [kernels, gaussian-processes, representation-learning]
source_refs:
  - id: boss-fa-2005
    pages: "37-39, 112-122"
    role: primary
  - id: hofmann-scholkopf-smola-kernel-methods-2006
    pages: "4-19"
    role: extension
level: advanced
created: 2026-07-10
updated: 2026-07-27
---

# Гильбертовы пространства → воспроизводящие ядра и гауссовские процессы

## Воспроизводящее свойство

Воспроизводящее ядерное гильбертово пространство (reproducing kernel Hilbert space, RKHS) $\mathcal H$ — гильбертово пространство функций, в котором вычисление значения $f\mapsto f(x)$ непрерывно. По [[30_mathematics/functional-analysis/theorems/riesz-representation|теореме Рисса]] существует $k_x\in\mathcal H$:

$$
f(x)=\langle f,k_x\rangle_\mathcal H.
$$

Ядро определяется формулой $k(x,y)=\langle k_y,k_x\rangle$, поэтому матрица Грама положительно полуопределена. Обратное построение подробно разобрано в [[30_mathematics/kernel-methods/theorems/moore-aronszajn-rkhs-correspondence|теореме Мура—Ароншайна]].

## Установленный результат: ядерный трюк

Если $k(x,y)=\langle\phi(x),\phi(y)\rangle$, алгоритм может работать со скалярными произведениями без явного построения $\phi$. Геометрия пространства признаков полностью задаётся ядром.

Не всякая мера сходства является ядром: для любой конечной выборки матрица Грама должна быть положительно полуопределённой.

## Установленный результат: теорема о представителе

Для функционала качества

$$
\min_{f\in\mathcal H}
L(f(x_1),\ldots,f(x_n))+\lambda\|f\|_\mathcal H^2
$$

существует минимум вида

$$
f^*(\cdot)=\sum_{i=1}^n\alpha_i k(x_i,\cdot).
$$

Доказательство: разложим $f=f_\parallel+f_\perp$, где $f_\parallel$ лежит в линейной оболочке $k_{x_i}$. Вычисление значений не видит $f_\perp$, а норма только увеличивается. Полная формулировка с условиями: [[30_mathematics/kernel-methods/theorems/representer-theorem-kernel-expansion|теорема о представителе]].

## Гауссовские процессы

Ядро задаёт ковариацию гауссовского процесса. Связанное с ядром пространство RKHS описывает направления Камерона—Мартина и гладкость апостериорного среднего, но типичная выборка процесса почти наверное не лежит в RKHS. Это важная граница между выборками априорного процесса и пространством оптимизации.

## Глубокие ядра

Ядро $k_\theta(x,y)=k_0(g_\theta(x),g_\theta(y))$ остаётся положительно полуопределённым, если базовое ядро обладает этим свойством для любых признаков. Однако обучение $\theta$ делает функционал качества невыпуклым; теорема о представителе относится к внешней задаче в RKHS при фиксированном ядре.

## Типичные сбои

- Неопределённое по знаку сходство разрушает гильбертову интерпретацию.
- Матрица ядра может быть плохо обусловлена.
- Большая ширина ядра схлопывает расстояния, а малая ширина переобучает локальный шум.
- Точная гауссовская процедура требует $O(n^3)$ операций, поэтому применяют приближения Нюстрёма и случайные признаки с контролируемой ошибкой.

## Визуализация

![Математическая структура, интуитивный перенос и проверка связи с ИИ](80_assets/bridges/gpt-image-v2/hilbert-rkhs-insight.png)

Интерактив: `interactive/hilbert-projection.html`.

## Связи

[[30_mathematics/functional-analysis/modules/07-hilbert-operators]], [[20_concepts/adjoint-operator]], [[50_bridges/operators-spectrum]], [[30_mathematics/kernel-methods/modules/01-positive-definite-kernels-rkhs]], [[30_mathematics/kernel-methods/methods/kernel-construction-closure-rules]].
