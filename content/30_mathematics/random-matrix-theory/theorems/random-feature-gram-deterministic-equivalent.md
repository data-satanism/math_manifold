---
id: random-feature-gram-deterministic-equivalent
title: "Детерминированный эквивалент нелинейной матрицы Грама"
aliases: ["Теорема Луара—Ляо—Куйе", "Nonlinear Gram matrix deterministic equivalent"]
type: theorem
status: canonical
publish: true
areas: [random-matrix-theory, random-features, neural-networks]
concepts: [random-feature-gram-matrix, effective-kernel, deterministic-equivalent]
prerequisites: [rmt-05-random-neural-networks, sample-covariance-deterministic-equivalent]
ai_domains: [random-features, regression, neural-networks]
source_refs:
  - id: rmt4ml-2022
    pages: "301-310"
    role: primary
  - id: louart2018randomnn
    pages: "1-19, 20-53"
    role: primary
level: advanced
created: 2026-07-27
updated: 2026-07-27
---

# Детерминированный эквивалент нелинейной матрицы Грама

## Формулировка

Пусть $W\in\mathbb R^{N\times p}$ имеет независимые стандартные гауссовы элементы, $\sigma\colon\mathbb R\to\mathbb R$ является 1-липшицевой, а детерминированная $X\in\mathbb R^{p\times n}$ имеет равномерно ограниченную операторную норму.

Пусть $n,p,N\to\infty$, причём отношения $p/n$ и $N/n$ отделены от нуля и бесконечности. Для $\gamma>0$ определим

$$
Q
=\left(
\frac1n\sigma(X^TW^T)\sigma(WX)+\gamma I_n
\right)^{-1}
$$

и ядро

$$
K
=
\mathbb E_{w\sim\mathcal N(0,I_p)}
\left[\sigma(X^Tw)\sigma(w^TX)\right].
$$

Тогда

$$
Q\ \longleftrightarrow\
\bar Q
=
\left(
\frac Nn\frac{K}{1+\delta}
+\gamma I_n
\right)^{-1},
$$

где $\delta>0$ — единственное решение

$$
\delta=\frac1n\operatorname{tr}(\bar QK).
$$

Эквивалентность понимается в смысле нормированных следов и билинейных наблюдений.

## Схема доказательства

1. Представить матрицу Грама как сумму по независимым строкам $w_a$:

$$
\frac1n\Sigma^T\Sigma
=\frac1n\sum_{a=1}^N
\sigma(X^Tw_a)\sigma(w_a^TX).
$$

2. Исключить один нейрон и применить формулу Шермана—Моррисона.
3. Использовать концентрацию нелинейной квадратичной формы:

$$
\frac1n\sigma(w^TX)A\sigma(X^Tw)
\approx\frac1n\operatorname{tr}(AK).
$$

4. Заменить резольвенту без одного нейрона полной резольвентой в нормированном следе.
5. Получить самосогласование для $\delta$.
6. Доказать единственность положительного решения и концентрацию наблюдаемых величин.

## Следствие для ошибок

Детерминированные эквиваленты более высокого порядка для $\bar QA\bar Q$ дают почти-верные пределы ошибок обучения и теста однослойной случайной сети. Формулы зависят от $K$, $\delta$, $\gamma$ и перекрёстных ядер между обучающими и тестовыми объектами.

## Что теорема не утверждает

- $W$ не обучается.
- Скрытый слой один.
- $X$ может быть произвольной детерминированной матрицей ограниченной нормы, но зависимость $X$ от $W$ исключена.
- Формула не является теоремой о произвольной глубокой сети или нейронном касательном ядре.

## Контрпример к переносу

Если обучать $W$ на тех же $X,y$, то строки признаковой матрицы перестают быть независимыми одинаково распределёнными случайными признаками. Исключение одного нейрона больше не восстанавливает модель теоремы.

## Вычислительная форма

```python
delta = 1.0
for _ in range(500):
    K_eff = (N / n) * K / (1 + delta)
    Q_bar = np.linalg.inv(K_eff + gamma * np.eye(n))
    delta_next = np.trace(Q_bar @ K) / n
    if abs(delta_next - delta) < 1e-10:
        break
    delta = delta_next
```

## Перенос в ИИ

**Установлено.** Эффективное ядро предсказывает спектральные наблюдения и ошибки для однослойной случайной сети.

**Аналогия.** Нелинейные случайные признаки действуют как спектральная призма: множество случайных лучей сводится к одному калиброванному ядру.

**Исследовательская гипотеза.** Замороженные блоки больших моделей могут допускать похожее приближение после эмпирической проверки независимости и концентрации.

## Визуализация

![Концепция теоремы: случайная матрица Грама заменяется эффективным ядром, а регуляризация управляет критической областью](80_assets/random-matrix-theory/gpt-image-v3/random-feature-gram-insight-v3.webp)

## Самопроверка

1. Почему $K$ — это ядро признакового отображения?
2. Откуда возникает знаменатель $1+\delta$?
3. Для чего нужна $\gamma>0$?
4. Почему предел $N\to\infty$ при фиксированном $n$ не совпадает с совместным пределом?

## Источники

- [[60_sources/rmt4ml-couillet-liao|RMT4ML]], теорема 5.1 и следствие 5.1, стр. 301–310.
- [[60_sources/louart-liao-couillet-random-neural-networks|Louart, Liao, Couillet]], стр. 1–53.
