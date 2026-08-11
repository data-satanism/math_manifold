---
id: vc-uniform-law-large-numbers
title: "Равномерный закон больших чисел для VC-класса"
aliases: ["VC-закон больших чисел", "VC uniform law of large numbers"]
type: theorem
status: canonical
publish: true
areas: [probability, empirical-processes, statistical-learning-theory]
concepts: [vc-dimension, uniform-convergence, rademacher-complexity, symmetrization]
prerequisites: [dudley-integral-inequality, symmetrization, covering-number]
ai_domains: [statistical-learning, generalization, model-selection]
source_refs:
  - id: vershynin-hdp-2026
    pages: "239-241"
    role: primary
level: advanced
created: 2026-07-27
updated: 2026-08-12
---

# Равномерный закон больших чисел для VC-класса

## Зачем это нужно

Обычный закон больших чисел работает для одной фиксированной функции. В обучении функция выбирается из класса после просмотра данных. Теорема показывает, когда одна выборка одновременно хорошо оценивает ожидания всех булевых функций класса.

## Формулировка

Пусть $\mathcal F$ — класс функций

$$
f\colon\Omega\to\{0,1\}
$$

с конечной VC-размерностью $d=\operatorname{vc}(\mathcal F)$. Пусть

$$
X,X_1,\ldots,X_n
$$

независимы и одинаково распределены. Тогда

$$
\boxed{
\mathbb E
\sup_{f\in\mathcal F}
\left|
\frac1n\sum_{i=1}^nf(X_i)
-
\mathbb Ef(X)
\right|
\le
C\sqrt{\frac dn}.
}
$$

Это оценка в ожидании. Высоковероятностная форма требует дополнительного концентрационного шага.

## Карта доказательства

```mermaid
flowchart LR
  A["Равномерное отклонение"] --> B["Симметризация"]
  B --> C["Радемахеровский процесс"]
  C --> D["Субгауссовские приращения"]
  D --> E["Неравенство Дадли"]
  E --> F["Покрытия через VC-размерность"]
  F --> G["Масштаб √(d/n)"]
```

## Доказательство

### Шаг 1. Симметризация

Пусть $\varepsilon_i$ — независимые знаки Радемахера. Тогда

$$
\mathbb E
\sup_{f\in\mathcal F}
\left|
\frac1n\sum_i f(X_i)-\mathbb Ef(X)
\right|
\le
\frac{2}{\sqrt n}
\mathbb E
\sup_{f\in\mathcal F}|Z_f|,
$$

где

$$
Z_f
=
\frac1{\sqrt n}
\sum_{i=1}^n\varepsilon_if(X_i).
$$

### Шаг 2. Условный процесс

Зафиксируем данные $(X_i)$. Тогда вся случайность заключена в $\varepsilon_i$. Для $f,g\in\mathcal F$:

$$
Z_f-Z_g
=
\frac1{\sqrt n}
\sum_i\varepsilon_i(f-g)(X_i).
$$

Субгауссовская норма приращения ограничена эмпирической метрикой:

$$
\|Z_f-Z_g\|_{\psi_2}
\le
C
\left[
\frac1n\sum_i(f-g)(X_i)^2
\right]^{1/2}
=
C\|f-g\|_{L^2(\mu_n)}.
$$

### Шаг 3. Неравенство Дадли

Условно на данных:

$$
\mathbb E_\varepsilon
\sup_{f\in\mathcal F}Z_f
\le
C
\int_0^1
\sqrt{
\log N(
\mathcal F,
L^2(\mu_n),
\varepsilon
)}
\,d\varepsilon.
$$

Верхний предел равен единице, потому что функции булевы.

### Шаг 4. Покрытия через VC-размерность

Энтропийная оценка VC-класса даёт

$$
\log N(
\mathcal F,
L^2(\mu_n),
\varepsilon
)
\le
Cd\log(2/\varepsilon).
$$

Следовательно,

$$
\mathbb E_\varepsilon
\sup_fZ_f
\le
C\sqrt d
\int_0^1
\sqrt{\log(2/\varepsilon)}
\,d\varepsilon.
$$

Интеграл — абсолютная константа, поэтому

$$
\mathbb E_\varepsilon\sup_fZ_f
\le
C\sqrt d.
$$

### Шаг 5. Возврат к исходной шкале

Множитель $2/\sqrt n$ из симметризации даёт

$$
\mathbb E
\sup_f
\left|
\frac1n\sum_i f(X_i)-\mathbb Ef(X)
\right|
\le
C\sqrt{\frac dn}.
$$

## Контрпример при бесконечной VC-размерности

Пусть $\Omega=[0,1]$ с непрерывным распределением, а $\mathcal F$ содержит индикаторы всех конечных подмножеств. После наблюдения выборки выберем

$$
f=\mathbf1_{\{X_1,\ldots,X_n\}}.
$$

Тогда

$$
\frac1n\sum_if(X_i)=1,
\qquad
\mathbb Ef(X)=0.
$$

Равномерное отклонение равно единице для любого $n$. Неограниченная способность «запомнить» выборку разрушает равномерный закон больших чисел.

## Вычислительная форма

Ориентир для размера выборки при ожидаемой равномерной ошибке $\varepsilon$:

$$
n
\gtrsim
\frac{d}{\varepsilon^2}.
$$

Это не готовая производственная формула: абсолютная константа, доверительная вероятность, шум разметки и адаптивный выбор класса требуют дополнительных членов.

## Перенос в ИИ

- **`established`**: конечная VC-размерность контролирует равномерную ошибку булевого класса при независимой одинаково распределённой выборке.
- **`analogy`**: VC-размерность измеряет способность класса реализовывать независимые двоичные решения на точках.
- **`research hypothesis`**: эффективная локальная VC-подобная сложность найденной модели может быть существенно ниже глобальной, но её корректное определение для глубоких сетей нетривиально.

## Режим отказа

Повторный выбор архитектуры, порогов и признаков по одной проверочной выборке фактически расширяет класс $\mathcal F$. Граница для исходного класса больше не учитывает полный перебор.

## Визуализация

![VC-закон больших чисел: разбиение конечного набора, симметризация, равномерная ошибка класса, аналогия с набором шаблонов и отказ через запоминание выборки](80_assets/probability/gpt-image-v3/vc-uniform-law-large-numbers-insight-v3.png)

## Упражнения

1. Найдите VC-размерность порогов на прямой.
2. Почему функции со значениями $0/1$ имеют диаметр не больше единицы в $L^2(\mu_n)$?
3. Где используется независимость выборки?
4. Объясните контрпример с индикатором наблюдённых точек.

## Источники

- [[60_sources/vershynin-high-dimensional-probability|Роман Вершинин, High-Dimensional Probability]], теорема 8.3.15, с. 239–241.
- [[30_mathematics/probability/modules/08-chaining-empirical-processes|Модуль о цепочках и VC-размерности]].
