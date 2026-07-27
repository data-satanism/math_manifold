---
id: generalized-linear-classifier-asymptotics
title: "Асимптотика обобщённого линейного классификатора"
aliases: ["Теорема Мая—Ляо", "Generalized linear classifier asymptotics"]
type: theorem
status: canonical
publish: true
areas: [random-matrix-theory, convex-optimization, statistical-learning]
concepts: [generalized-linear-classifier, proximal-map, leave-one-out]
prerequisites: [rmt-06-high-dimensional-convex-classifiers, sample-covariance-deterministic-equivalent]
ai_domains: [logistic-regression, classification, robust-learning]
source_refs:
  - id: rmt4ml-2022
    pages: "341-352"
    role: primary
level: advanced
created: 2026-07-27
updated: 2026-07-27
---

# Асимптотика обобщённого линейного классификатора

## Формулировка

Рассмотрим симметричную двухклассовую гауссову модель после умножения признаков на метку:

$$
\widetilde x_i=y_ix_i\sim\mathcal N(\mu,C),
$$

где $\max\{\|\mu\|,\|C\|,\|C^{-1}\|\}=O(1)$. Пусть $L$ выпукла и трижды непрерывно дифференцируема, $\gamma>0$, а $\widehat\beta$ — единственное решение

$$
\min_\beta
\frac1n\sum_iL(\widetilde x_i^T\beta)
+\frac\gamma2\|\beta\|^2.
$$

При $n,p\to\infty$, $p/n\to c\in(0,\infty)$ существует гауссов эквивалент $\widetilde\beta$, для которого

$$
\|\widehat\beta-\widetilde\beta\|\to0
$$

и

$$
\left(\gamma I_p-\mathbb E[f'(r)]C\right)\widetilde\beta
\sim
\mathcal N\!\left(
\mathbb E[f(r)]\mu,\,
\frac{\mathbb E[f(r)^2]}nC
\right),
$$

где

$$
f(r)=-L'(\operatorname{prox}_{\delta L}(r)),
\qquad r\sim\mathcal N(M,\sigma^2).
$$

Параметры $M,\sigma^2,\delta$ являются решением самосогласованной системы:

$$
M
=\mathbb E[f(r)]\,
\mu^T\left(\gamma I-\mathbb E[f'(r)]C\right)^{-1}\mu,
$$

$$
\begin{aligned}
\sigma^2
={}&\mathbb E[f(r)]^2
\mu^T RCR\mu\\
&+\frac{\mathbb E[f(r)^2]}n
\operatorname{tr}(R^2C^2),
\end{aligned}
$$

где $R=(\gamma I-\mathbb E[f'(r)]C)^{-1}$, а $\delta>0$ удовлетворяет

$$
\delta
=\frac1n\operatorname{tr}
C\left[
\mathbb E\frac{L''(\operatorname{prox}_{\delta L}(r))}
{1+\delta L''(\operatorname{prox}_{\delta L}(r))}C
+\gamma I
\right]^{-1}.
$$

Следовательно, для нового $\widetilde x\sim\mathcal N(\mu,C)$

$$
\mathbb P(\widehat\beta^T\widetilde x<0)
\longrightarrow
\Phi\!\left(-\frac M\sigma\right).
$$

## Схема доказательства

1. Записать условие оптимальности для $\widehat\beta$.
2. Исключить объект $i$ и линеаризовать изменение решения через гессиан эмпирического риска.
3. Выразить полный зазор через $\operatorname{prox}_{\delta L}$ от исключённого зазора.
4. Применить детерминированный эквивалент взвешенной выборочной ковариации к обратному гессиану.
5. Поскольку $\widehat\beta^{(-i)}$ не зависит от $\widetilde x_i$, получить гауссов предел $r_i$.
6. Согласовать его среднее и дисперсию с моментами $f(r)$.
7. Использовать сильную выпуклость от $\gamma>0$ для единственности и устойчивости.

## Контрпример при нарушении условий

Для логистической потери и $\gamma=0$ на линейно разделимых данных значение целевой функции убывает вдоль луча $\alpha b$, $\alpha\to\infty$. Конечного минимизатора нет, поэтому нормальный эквивалент ограниченной нормы не существует.

## Вычислительная форма

Систему решают вложенной итерацией:

1. задать $M,\sigma,\delta$;
2. вычислить одномерные гауссовы ожидания квадратурой;
3. обновить $R,M,\sigma,\delta$;
4. использовать демпфирование;
5. сравнить несколько инициализаций.

## Перенос в ИИ

**Установлено.** Теорема предсказывает распределение классификатора и ошибку в гауссовой смеси с гладкой выпуклой потерей.

**Аналогия.** Каждый объект создаёт ограниченную силу на упругой разделяющей плоскости; равновесие описывается несколькими макроскопическими параметрами.

**Исследовательская гипотеза.** Гауссов эквивалент последнего слоя может быть полезен для калибровки уверенности, если предварительно проверить геометрию обученных признаков.

## Визуализация

![Концепция теоремы: исключение одного объекта разрывает зависимость, проксимальное отображение ограничивает его влияние, а фиксированная точка предсказывает ошибку](80_assets/random-matrix-theory/gpt-image-v3/high-dimensional-convex-classifier-insight-v3.png)

## Самопроверка

1. Где используется гауссовость $\widetilde x_i$?
2. Какую роль играет проксимальное отображение?
3. Почему $\widehat\beta$ не обязана сходиться к детерминированному вектору?
4. Что препятствует прямой подстановке шарнирной потери?

## Источники

- [[60_sources/rmt4ml-couillet-liao|RMT4ML]], теорема 6.1, стр. 341–352.
