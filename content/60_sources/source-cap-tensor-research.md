---
id: source-cap-tensor-research
title: TT, SF-ETT и Cherry-Picking — первичные источники
aliases: []
type: source
status: canonical
publish: true
areas:
- numerical-linear-algebra
concepts: []
prerequisites: []
ai_domains:
- compression
- scientific-ml
source_refs: []
level: advanced
created: '2026-11-04'
updated: '2026-11-04'
---

# Прочитанные результаты

- I. Oseledets. Tensor-Train Decomposition. SIAM J. Sci. Comput. 33(5), 2011, 2295–2317, [DOI](https://doi.org/10.1137/090752286). Веб-PDF изучен по §2 и §3, теоремам 2.1–2.2 и алгоритмам TT-SVD и округления. [[30_mathematics/computational-algebra-principles/modules/cap-t01-tt]] раскрывает собственное пошаговое доказательство этих свойств.
- A. Molozhavenko, M. Rakhuba. Optimization on the Extended Tensor-Train Manifold with Shared Factors. [arXiv:2508.20928v1](https://arxiv.org/abs/2508.20928v1). Изучены §§4–5, теоремы 1, 2, 5, координатные формулы касательной проекции. В [[30_mathematics/computational-algebra-principles/modules/cap-t02-sf-ett]] разобран пробел перехода к окружающему Tucker-многообразию и дан альтернативный локальный аргумент. Базовая гладкость TT-страты используется как известный результат. Собственная оценка усечения относится к порядку SF-HOSVD → TT-SVD.
- S. Holtz, T. Rohwedder, R. Schneider. On manifolds of tensors of fixed TT-rank. Numerische Mathematik 120, 2012, 701–731, [DOI](https://doi.org/10.1007/s00211-011-0419-7). Базовая теорема гладкости импортирована, полный текст её доказательства в текущем этапе не воспроизводился.
- M. Usvyatsov et al. Cherry-Picking Gradients. ICCV 2021, 11426–11435, [PDF](https://openaccess.thecvf.com/content/ICCV2021/papers/Usvyatsov_Cherry-Picking_Gradients_Learning_Low-Rank_Embeddings_of_Visual_Data_via_Differentiable_ICCV_2021_paper.pdf). Прочитаны §§3.1–3.4 и алгоритм 1, проверены схемы на PDF с. 4–5. Приложение не разобрано полностью. В [[30_mathematics/computational-algebra-principles/modules/cap-t03-cherry-picking]] доказаны производная матричного креста, граница смены индексов и инвариантность признаков при фиксированном общем базисе.

Численные иллюстрации относятся к малым матрицам и тензорам. Утверждения о времени обучения и качестве моделей приводятся только как результаты авторов.
