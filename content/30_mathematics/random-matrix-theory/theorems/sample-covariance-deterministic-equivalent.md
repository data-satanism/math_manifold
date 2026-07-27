---
id: sample-covariance-deterministic-equivalent
title: "Детерминированный эквивалент выборочной ковариации"
aliases: ["Теорема Сильверстайна—Бая", "Sample covariance deterministic equivalent"]
type: theorem
status: canonical
publish: true
areas: [random-matrix-theory, covariance-estimation, spectral-analysis]
concepts: [sample-covariance, deterministic-equivalent, resolvent-stieltjes-transform]
prerequisites: [rmt-02-resolvents-deterministic-equivalents, marchenko-pastur-law]
ai_domains: [pca, covariance-estimation, spectral-diagnostics, kernel-methods]
source_refs:
  - id: rmt4ml-2022
    pages: "78-84"
    role: primary
  - id: couillet2011wirelessrmt
    pages: "137-170"
    role: secondary
level: advanced
created: 2026-07-27
updated: 2026-07-27
---

# Детерминированный эквивалент выборочной ковариации

## Зачем нужен результат

[[30_mathematics/random-matrix-theory/theorems/marchenko-pastur-law|Закон Марченко—Пастура]] предполагает единичную популяционную ковариацию. Теорема Сильверстайна—Бая сохраняет резольвентный механизм при произвольной ограниченной $C\succeq0$ и превращает её спектр в самосогласованное уравнение.

## Формулировка

Пусть

$$
X=C^{1/2}Z\in\mathbb R^{p\times n},
$$

где $C=C_p\succeq0$, $\sup_p\|C_p\|<\infty$, а элементы $Z$ независимы, центрированы, имеют единичную дисперсию и удовлетворяют условию лёгких хвостов из источника. Пусть $p/n\to c\in(0,\infty)$ и

$$
Q(z)=\left(\frac1nXX^T-zI_p\right)^{-1},\qquad
\widetilde Q(z)=\left(\frac1nX^TX-zI_n\right)^{-1}.
$$

Тогда для $z\in\mathbb C\setminus\mathbb R_+$

$$
Q(z)\ \longleftrightarrow\
\bar Q(z)=-\frac1z\left(I_p+\widetilde m_p(z)C\right)^{-1},
$$

$$
\widetilde Q(z)\ \longleftrightarrow\
\bar{\widetilde Q}(z)=\widetilde m_p(z)I_n,
$$

где пара $(z,\widetilde m_p(z))$ является единственным допустимым решением

$$
\widetilde m_p(z)
=
\left(
-z+\frac1n\operatorname{tr}
C\left(I_p+\widetilde m_p(z)C\right)^{-1}
\right)^{-1}.
$$

Символ $\longleftrightarrow$ означает детерминированную эквивалентность нормированных следов и допустимых билинейных наблюдений, а не операторно-нормовую близость матриц.

Если эмпирическая спектральная мера $C_p$ слабо сходится к $\nu$, то предельное сопряжённое преобразование удовлетворяет

$$
\widetilde m(z)
=
\left(
-z+c\int\frac{t}{1+\widetilde m(z)t}\,\nu(dt)
\right)^{-1},
$$

а преобразование спектра $XX^T/n$ связано с ним стандартным соотношением между матрицей и её матрицей Грама.

## Доказательная схема

1. Разложить $XX^T/n$ в сумму $x_ix_i^T/n$.
2. Ввести $Q_{-i}$ и выразить $Q$ через него формулой ранга один.
3. Использовать независимость $x_i$ и $Q_{-i}$.
4. Применить лемму о близости квадратичной формы к следу:

$$
\frac1n x_i^TQ_{-i}x_i
\approx \frac1n\operatorname{tr}(CQ_{-i}).
$$

5. Показать, что замена $Q_{-i}$ на $Q$ в нормированном следе асимптотически безвредна.
6. Получить самосогласованное уравнение и матричную форму $\bar Q$.
7. Доказать единственность решения в классе преобразований Штильтьеса.
8. Усилить сходимость в среднем до почти наверное с помощью концентрации и леммы Бореля—Кантелли.

## Контрпример к неверному усилению

Даже когда

$$
\frac1p\operatorname{tr}(Q-\bar Q)\to0,
$$

нельзя заключать $\|Q-\bar Q\|\to0$. Вблизи края спектра отдельные собственные значения и направления флуктуируют сильнее, чем нормированный след.

## Вычислительный алгоритм

1. Вычислить собственные значения $t_j$ матрицы $C$.
2. Для $z=x+i\eta$ инициализировать $\widetilde m^{(0)}=-1/z$.
3. Итерировать

$$
\widetilde m^{(k+1)}
=
\left(
-z+\frac1n\sum_{j=1}^p\frac{t_j}{1+\widetilde m^{(k)}t_j}
\right)^{-1}.
$$

4. Проверить $\operatorname{Im}\widetilde m(z)>0$ при $\operatorname{Im}z>0$.
5. Восстановить плотность через мнимую часть следа $\bar Q(x+i\eta)$.

## Перенос в ИИ

**Установлено.** Результат описывает шумовое и деформированное спектральное распределение выборочной ковариации при общей $C$.

**Аналогия.** Много случайных спектров колеблются около единой калибровочной кривой — как повторные измерения одного спектрометра.

**Исследовательская гипотеза.** Подгонка самосогласованного уравнения может помогать строить нулевые модели спектров внутренних представлений, если зависимость объектов и признаки корректно смоделированы.

## Визуализация

![Концепция теоремы: случайные резольвенты сходятся в наблюдаемых величинах к детерминированному эквиваленту](80_assets/random-matrix-theory/gpt-image-v3/deterministic-equivalent-resolvent-insight-v3.png)

## Самопроверка

1. Где в доказательстве используется независимость элементов $Z$?
2. Почему уравнение задаёт $\widetilde m_p$, зависящее от конечномерной $C_p$, а не только предел?
3. Как из $C=I$ получается квадратное уравнение Марченко—Пастура?
4. Почему знак мнимой части является частью формулировки?

## Источники

- [[60_sources/rmt4ml-couillet-liao|RMT4ML]], теорема 2.6, стр. 78–84.
- [[30_mathematics/random-matrix-theory/rmt-source-map|Карта источников RMT]].
