---
id: source-qr-rank-revealing
title: 'Источники А04: QR, численный ранг и сильное RRQR'
aliases: []
type: source
status: canonical
publish: true
areas:
- numerical-linear-algebra
concepts:
- qr-factorization
- numerical-rank
- rank-revealing-factorization
prerequisites: []
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

# Источники модуля А04

## Gu–Eisenstat: сильный выбор столбцов

Ming Gu, Stanley C. Eisenstat. **Efficient Algorithms for Computing a Strong Rank-Revealing QR Factorization.** SIAM Journal on Scientific Computing 17(4), 1996, 848–869. DOI [10.1137/0917055](https://doi.org/10.1137/0917055). [Авторская PDF-копия в Berkeley](https://math.berkeley.edu/~mgu/MA273/Strong_RRQR.pdf).

Прочитаны необходимые части §§1–4: определения, Example 1, Lemma 3.1, Theorem 3.2 и различие совместного сертификата Algorithm 4 и раздельного Algorithm 5. Основной агент просмотрел PDF-страницы 4–7, журнальные 851–854; независимый редактор отдельно сверил доказательства на изображениях. Полное прочтение всех 22 страниц, воспроизведение ускоренных обновлений и полное доказательство машинной устойчивости не заявляются.

Главная используемая гарантия — Theorem 3.2 с совместным критерием и множителем $\sqrt{1+f^2k(n-k)}$. При двух раздельных ограничениях по $f$ возникает $\sqrt{1+2f^2k(n-k)}$. В А04 норма строки обратной обозначена $\omega_i$, тогда как в статье её величина вводится через обратную: это различие оговорено.

Матрица Кахана раскрыта через точные остаточные равенства и рост коэффициентов. Отсутствие перестановки относится к разрешённому выбору первого столбца при равенстве норм в точной арифметике. Фактическая перестановка SciPy/LAPACK измерена отдельно; численный график не скрывает её отличие.

## LAPACK: отражения, хранение и перестановка

Первичная документация [DGEQRF](https://netlib.org/lapack/explore-html/d0/da1/group__geqrf_gade26961283814bb4e62183d9133d8bf5.html) и [DGEQP3](https://netlib.org/lapack/explore-html/d0/dea/group__geqp3_gae96659507d789266660af28c617ef87f.html): формат экономичного/полного QR, представление Q отражениями, структура верхнетреугольного или трапециевидного блока, смысл перестановки. Документация сама по себе не доказывает, что всякая вычисленная CPQR-перестановка имеет сильный RRQR-сертификат.

## Принятые спектральные основания

Теорема Эккарта–Янга о наилучшей аппроксимации, оценка возмущения сингулярных чисел и аппроксимационная характеристика сингулярных чисел используются как стандартные результаты из [[30_mathematics/numerical-analysis/modules/02-unitary-matrices-and-svd|SVD]]. Собственные раскрытия: отражение Householder, геометрическая формула высот при обмене, точные ID-остатки, случай нулевого хвоста сильной оценки и маленькие контрпримеры.

Материалы: [[30_mathematics/computational-algebra-principles/modules/cap-a04-qr-numerical-rank|А04]], [[30_mathematics/computational-algebra-principles/theorems/cap-strong-rrqr|опорная теорема]], [[30_mathematics/computational-algebra-principles/concepts/cap-numerical-rank|понятие численного ранга]], [[70_labs/computational-algebra-principles/cap-qr-riemannion-lab|лаборатория]]. Все остаются review/publish:false.
