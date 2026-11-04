---
id: cap-branches456-lab
title: 'Лабораторная работа: перестановка ковариации, QTT-ранги и локальная вариация
  Мёбиуса'
aliases: []
type: lab
status: canonical
publish: true
areas:
- numerical-linear-algebra
- complex-analysis
concepts:
- kronecker-product
- tensor-train
- mobius-transformation
prerequisites: []
ai_domains:
- scientific-machine-learning
source_refs:
- id: source-puchkin-rakhuba-structured-covariance
  pages: PDF 4–9
  role: primary
- id: source-kazeev-qtt-fem-multiscale
  pages: §2.1, §4.3
  role: primary
- id: source-bogatyrev-schottky-variation
  pages: PDF 2
  role: primary
level: advanced
created: '2026-11-04'
updated: '2026-11-04'
---

# Воспроизводимые малые проверки

Скрипт build_figures.py (скрипт build_figures.py в каталоге лаборатории) запускается из корня хранилища командой `python 70_labs/figures/branches456-v1/build_figures.py`. Зависимости: Python, NumPy, Matplotlib. Он создаёт 6 SVG, 6 PNG и 6 PDF в версии `branches456-v1`, а также численный служебный отчёт. Сохранённые числа — один полностью заданный опыт, а не опубликованные результаты статей.

## 1. Ковариация

Проверяются точное тождество $\mathcal R(A\otimes B)=\operatorname{vec}A(\operatorname{vec}B)^T$, обратная перестановка и изометрия Фробениуса для двух явно заданных матриц $2\times2$. Во всех трёх проверках ошибка равна 0 в использованной арифметике.

Далее $p=q=4$, $\Phi=\operatorname{diag}(1,0.5,0.25,0.125)$, $\Psi=\operatorname{diag}(1,0.6,0.3,0.1)$. Для точной модели $\Sigma=\Phi\otimes\Psi$ и нарушенной модели $\Sigma+0.6ww^T$ берутся гауссовские наблюдения. $w$ — фиксированное случайное единичное направление. Используется генератор NumPy `default_rng(456)`, последовательно 12 повторов для каждого $n\in\{32,128,512,2048,8192\}$. Сравниваются средние абсолютные ошибки Фробениуса выборочной ковариации и жёсткого ранга 1 её перестановки.

При $n=8192$ точная модель даёт примерно 0.04489 против 0.02936; нарушенная — 0.05414 против 0.55159. Это свидетельство смещения конкретного структурного ограничителя. Интервалы неопределённости не строились, вероятность теоремы не проверялась, мягкий оцениватель статьи в опыте не используется. Сравнение полностью задано; подбора порога по этим числам нет.

![Результаты собственного опыта с точной и нарушенной моделью ковариации](80_assets/computational-algebra-principles/branches456-v1/covariance-misspecification.svg)

[Открыть рисунок в полном размере](80_assets/computational-algebra-principles/branches456-v1/covariance-misspecification.svg)

## 2. QTT

Для $L=10$, $N=1024$ вычисляются SVD всех двоичных развёрток векторов $e^{-k/200}$, $\sin(2\pi k/N)$ и гауссовского случайного массива. Численный ранг считает сингулярные числа больше $10^{-10}s_1$. Экспонента имеет ранги 1; синус — не выше 2; случайный массив достигает 32 на среднем разрезе. Скрипт проверяет эти условия через `assert`.

![Измеренные ранги двоичных развёрток](80_assets/computational-algebra-principles/branches456-v1/qtt-binary-ranks.svg)

[Открыть рисунок в полном размере](80_assets/computational-algebra-principles/branches456-v1/qtt-binary-ranks.svg)

Второй QTT-рисунок использует заданные функции $2^{-0.8\Lambda}$ и $2^{-0.8\Lambda}+2^{-8}$. Это иллюстрация верхней оценки и области $\Lambda\le\lambda_1/0.8$, а не численное решение PDE. Решатель FEM, гомогенизация и тензорный алгоритм статьи не реализованы.

## 3. Мёбиус

При $u=0.4+0.3i$ и матрице $A=\begin{pmatrix}0.3&0.7\\-0.2&0.1\end{pmatrix}$ аналитическое поле $-\operatorname{tr}(M(u)A)$ сравнивается с центральной разностью при $h=10^{-6}$. Абсолютная ошибка около $3.72\cdot10^{-11}$; след для скалярного направления ровно 0.

Для семейства $T_h(u)=(u+h)/(hu+1)$ измеряется остаток после линейного члена при 30 значениях $h$ от $10^{-5}$ до $10^{-1}$. Наклон логарифма остатка по логарифму $h$ на первых 18 точках равен 1.99988. Это согласуется с точным остатком второго порядка. Ни периоды, ни общая граничная формула Шоттки здесь численно не вычисляются.

![Локальное поле Мёбиуса и квадратичный остаток](80_assets/computational-algebra-principles/branches456-v1/schottky-mobius-variation.svg)

[Открыть рисунок в полном размере](80_assets/computational-algebra-principles/branches456-v1/schottky-mobius-variation.svg)

## Границы выводов

Проверки подтверждают реализацию конечных тождеств и выбранных иллюстраций. Они не заменяют вероятностную теорему, результат гомогенизации или формулу Рауха. Соответствующие уровни импорта отмечены в [[30_mathematics/computational-algebra-principles/modules/cap-s01-structured-covariance]], [[30_mathematics/computational-algebra-principles/modules/cap-q01-qtt-fem]], [[30_mathematics/computational-algebra-principles/modules/cap-s02-schottky-variation]]. Полный код воспроизводит все рисунки и числа; машинные расхождения в последних знаках допустимы.
