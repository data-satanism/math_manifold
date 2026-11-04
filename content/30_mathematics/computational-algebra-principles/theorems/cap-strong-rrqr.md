---
id: cap-strong-rrqr-theorem
title: Совместный сертификат обмена и сильное ранговыявляющее QR
aliases: []
type: theorem
status: canonical
publish: true
areas:
- numerical-linear-algebra
concepts:
- qr-factorization
- numerical-rank
- rank-revealing-factorization
prerequisites:
- cap-a04-qr-numerical-rank
ai_domains:
- compression
- parameter-efficient-fine-tuning
source_refs:
- id: source-qr-rank-revealing
  pages: Точные разделы и границы чтения приведены в тексте
  role: primary
level: advanced
created: '2026-11-03'
updated: '2026-11-03'
---

# Сильное RRQR: остаток и коэффициенты вместе

Теорема превращает локальную проверку обменов столбцов в спектральную гарантию. Одного малого коэффициента восстановления недостаточно: выбранный базис может быть слабым относительно ещё не выбранного направления.

## Условия и результат

Пусть $A\in\mathbb R^{m\times n}$, $m\ge n$, $1\le k<n$, и

$$

A\Pi=Q\begin{pmatrix}B&F\\0&D\end{pmatrix},\qquad\det B\ne0.

$$

Здесь $Q\in\mathbb R^{m\times m}$ ортогональна, а $\Pi\in\mathbb R^{n\times n}$ — матрица перестановки. Определим $T$ из $BT=F$, $\gamma_j=\|D[:,j]\|_2$ и $\omega_i=\|\text{строка }i\text{ матрицы }B^{-1}\|_2$. Предположим совместный сертификат

$$

\max_{i,j}\sqrt{T_{ij}^2+\gamma_j^2\omega_i^2}\le f,\qquad f\ge1.

$$

При $\mu=\sqrt{1+f^2k(n-k)}$ получаем

$$

\sigma_i(A)/\mu\le\sigma_i(B)\le\sigma_i(A),\quad1\le i\le k,

$$

$$

\sigma_{k+j}(A)\le\sigma_j(D)\le\mu\sigma_{k+j}(A),\quad1\le j\le n-k,

$$

а также $|T_{ij}|\le f$. Соответствующее интерполяционное разложение $\widehat A=C[I\ T]\Pi^T$ имеет ошибку $\|D\|_2\le\mu\sigma_{k+1}(A)$, где $C$ — выбранные исходные столбцы.

## Доказательство

Суммирование сертификатов даёт $\|T\|_F^2+\|D\|_F^2\|B^{-1}\|_F^2\le f^2k(n-k)$. Если $D\ne0$, положим $\alpha=\|D\|_2\|B^{-1}\|_2$. Обозначив треугольную матрицу через $\mathcal R$, имеем две факторизации:

$$

\mathcal R=\operatorname{diag}(B,D/\alpha)
\begin{pmatrix}I&T\\0&\alpha I\end{pmatrix},

$$

$$

\operatorname{diag}(\alpha B,D)=\mathcal R
\begin{pmatrix}\alpha I&-T\\0&I\end{pmatrix}.

$$

Нормы обеих правых матриц не превосходят $\sqrt{1+\|T\|_2^2+\alpha^2}\le\mu$: для разбиения вектора на $x,y$ достаточно оценить действие двумерной матрицы с элементами $1,\|T\|_2,\alpha$ и использовать её норму Фробениуса.

У первой левой блочно-диагональной матрицы первые $k$ сингулярных значений совпадают с таковыми $B$, поскольку $\|D/\alpha\|_2=\sigma_{\min}(B)$. У второй после первых $k$ идут значения $D$, поскольку $\sigma_{\min}(\alpha B)=\|D\|_2$. Неравенство $\sigma_i(SW)\le\sigma_i(S)\|W\|_2$ завершает обе сильные оценки.

При $D=0$ делить на $\alpha$ нельзя. Используется $\mathcal R=[B\ BT;0\ 0]$ и $\|[I\ T]\|_2\le\mu$; хвостовые утверждения нулевые. Обратные неравенства следуют из сжатия оператора и аппроксимационного принципа сингулярных значений. Все промежуточные шаги раскрыты в [[30_mathematics/computational-algebra-principles/modules/cap-a04-qr-numerical-rank|А04]].

![Жадный выбор высоты столбца и сертификат качества всего выбранного набора решают разные задачи](80_assets/computational-algebra-principles/qr-riemannion-gpt-v1/cap-a04-qr-insight.webp)

<a href="80_assets/computational-algebra-principles/qr-riemannion-gpt-v1/cap-a04-qr-insight.png" target="_blank" rel="noopener" data-router-ignore>Открыть рисунок в полном размере</a>

## Почему это связано с объёмом

Квадрат отношения прямоугольных объёмов при обмене выбранного столбца $i$ на невыбранный $j$ равен $T_{ij}^2+\gamma_j^2\omega_i^2$. Доказательство через высоту над пространством остальных столбцов дано в А04. Глобальный максимум объёма достаточен с $f=1$, но достаточно и указанной локальной проверки.

**Контрпример к неполной предпосылке.** Для $A=\operatorname{diag}(1,L)$ и первого выбранного столбца $T=0$, но ошибка $L$ против оптимальной 1. Совместный сертификат равен $L$ и замечает проблему.

**Самопроверка.** Если отдельно $|T_{ij}|\le f$ и $\gamma_j\omega_i\le f$, какая константа? Совместная граница $\sqrt2 f$, значит $\mu=\sqrt{1+2f^2k(n-k)}$. Нельзя забыть двойку при переходе к раздельному алгоритму.

> [!established] Прикладной смысл
> Для самого признакового массива контролируются ошибка ID и усиление погрешностей выбранных столбцов. Это не гарантия качества нейросети после произвольного сжатия.

Первоисточник: Gu–Eisenstat, 1996, Lemma 3.1 и Theorem 3.2, журнальные с. 853–854; [[60_sources/qr-rank-revealing-primary-sources|карточка]]. Численные проверки — [[70_labs/computational-algebra-principles/cap-qr-riemannion-lab|лаборатория]].
