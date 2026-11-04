---
id: deim-primary-sources
title: "Источники DEIM: координатный проектор и выбор индексов"
aliases: []
type: source
status: canonical
publish: true
areas: [numerical-analysis, numerical-linear-algebra]
concepts: [interpolation, projection]
prerequisites: []
ai_domains: [scientific-ml, compression]
source_refs:
  - id: deim-primary-sources
    pages: "Sorensen–Embree: с. 5–8 авторской редакции 21.06.2018"
    role: primary
level: advanced
created: 2026-11-04
updated: 2026-11-04
---

# DEIM: что прочитано и использовано

D. C. Sorensen, M. Embree. *A DEIM Induced CUR Factorization*. SIAM Journal on Scientific Computing 38(3), A1454–A1482 (2016). [DOI 10.1137/140978430](https://doi.org/10.1137/140978430), [авторский PDF arXiv:1407.5516v2](https://arxiv.org/pdf/1407.5516v2).

Использована доступная авторская редакция v2 с датой 21 июня 2018 года на титуле и пометкой arXiv от 18 сентября 2015 года, 30 страниц; обе даты буквально присутствуют в PDF. Прочитаны с. 5–8: определение 3.1 косого интерполяционного проектора, алгоритм 1, лемма 3.1 о невырожденности выбранного блока, лемма 4.1 об ошибке проекции. Страница 7 отрисована для проверки дополнения Шура и формулировки леммы 4.1. Страницы относятся к авторскому PDF, не к журнальной пагинации A1454–A1482.

S. Chaturantabut, D. C. Sorensen. *Nonlinear Model Reduction via Discrete Empirical Interpolation*. SIAM Journal on Scientific Computing 32(5), 2737–2764 (2010). [Официальная карточка и DOI 10.1137/090766498](https://epubs.siam.org/doi/10.1137/090766498).

Библиография и назначение метода подтверждены по официальной карточке. Попытки получить исходный технический отчёт Rice TR09-05 не дали полного PDF. Поэтому доказательства модуля опираются на доступный полный первичный текст Sorensen–Embree и самостоятельную алгебру. Мы не заявляем полного чтения статьи 2010 года.

В [[30_mathematics/computational-algebra-principles/modules/cap-06-deim|модуле DEIM]] доказательство равенства норм косого проектора и его дополнения раскрыто через ортогональные блоки. Двумерный пример достижения границы, шумовая оценка и разбор стоимости покоординатной нелинейности — самостоятельные учебные выводы. Эксперименты с PDE и сравнения CUR из статьи не воспроизводились.
