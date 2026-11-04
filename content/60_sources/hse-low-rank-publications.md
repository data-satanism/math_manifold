---
id: source-hse-low-rank-publications
title: 'Десять публикаций ИВМ РАН и ВШЭ: первоисточники и границы чтения'
aliases: []
type: source
status: canonical
publish: true
areas:
- numerical-linear-algebra
- differential-geometry
concepts:
- fixed-rank-manifold
- gauge-invariance
- riemannian-optimization
prerequisites: []
ai_domains:
- parameter-efficient-fine-tuning
- compression
source_refs:
- id: source-fixed-rank-geometry
  pages: Точные границы чтения и привязки указаны в тексте
  role: primary
level: advanced
created: '2026-11-03'
updated: '2026-11-03'
---

# Первичные источники новой ветки

Исходная точка — [публикации базовой кафедры ИВМ РАН в ВШЭ](https://cs.hse.ru/big-data/icm/publications/). В текстовом представлении списка не раскрылось содержимое динамического блока; конкретные работы проверены по первичным площадкам. Это подборка десяти работ пользователя, а не полный архив кафедры.

Даты и нумерация относятся к указанным версиям. Препринт, окончательная конференционная статья и журнальная версия не считаются одним и тем же прочитанным файлом. Локальные PDF и подробный служебный реестр находятся вне публичного экспорта; ниже — доступные первичные адреса.

1. **LoRA meets Riemannion: Muon Optimizer for Parametrization-independent Low-Rank Adapters.** [arXiv:2507.12142v2](https://arxiv.org/abs/2507.12142v2), 01.10.2025; первая версия 16.07.2025; [ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8505a7e1da40320bf5692d7edec5aa45-Abstract-Conference.html). Прочитан основной текст препринта, приложения выборочно; финальный PDF сверен на выбранных страницах. [Код](https://github.com/Bogachevv/RiemanianFinetune). Репозиторий не запускался.
2. **OrthoFuse: Training-free Riemannian Fusion of Orthogonal Style-Concept Adapters for Diffusion Models.** [arXiv:2604.05183v1](https://arxiv.org/abs/2604.05183v1), 06.04.2026. CVPR 2026 указан кафедрой и авторским репозиторием. Прочитаны основной механизм, результаты и выбранные приложения; существенные формулы просмотрены на PDF. [Код](https://github.com/ControlGenAI/OrthoFuse). Версионные несогласованности требуют проверки реализации перед учебным воспроизведением.
3. **А. Б. Богатырёв. Вариационная формула в модели Шоттки римановых поверхностей.** [MathNet](https://www.mathnet.ru/rus/rm10316), УМН 81:3(489), 2026, 159–160; DOI [10.4213/rm10316](https://doi.org/10.4213/rm10316). Полностью прочитан открытый английский [препринт arXiv:2509.22702v1](https://arxiv.org/abs/2509.22702v1), 22.09.2025, 3 страницы. Журнальный полный текст не прочитан: доступ на MathNet отложен до 01.07.2027. Совпадение всех формул версий не заявляется.
4. **Optimization on the Extended Tensor-Train Manifold with Shared Factors.** [arXiv:2508.20928v1](https://arxiv.org/abs/2508.20928v1), 28.08.2025; Computational and Applied Mathematics 45, 221 (2026), DOI [10.1007/s40314-025-03605-0](https://doi.org/10.1007/s40314-025-03605-0). Разобраны определения, геометрия, алгоритмы и часть экспериментов препринта; приложения не полностью. Закрытая журнальная версия не прочитана. [Код](https://github.com/SuperCrabLover/SF-ETT-Manifold). Отдельно требуется аудит предпосылок общего и индивидуальных рангов.
5. **COALA: Numerically Stable and Efficient Framework for Context-Aware Low-Rank Approximation.** [arXiv:2507.07580v3](https://arxiv.org/abs/2507.07580v3), 25.03.2026; первая версия 10.07.2025. NeurIPS 2025 указан авторским репозиторием. Прочитаны §§3–6, приложения не полностью; формулы целевой ошибки и регуляризации сверены на PDF. [Код](https://github.com/urparkina/COALA).
6. **ProcrustesGPT: Compressing LLMs with Structured Matrices and Orthogonal Transformations.** [Findings ACL 2025](https://aclanthology.org/2025.findings-acl.1381/), 26937–26949, DOI [10.18653/v1/2025.findings-acl.1381](https://doi.org/10.18653/v1/2025.findings-acl.1381). Прочитаны постановка, алгоритмы и основные таблицы препринта; финальный PDF сохранён, полная постраничная сверка приложения не выполнена. [Код](https://github.com/GrishKate/ProcrustesGPT).
7. **Dimension-free Structured Covariance Estimation.** [PMLR 247, COLT 2024](https://proceedings.mlr.press/v247/puchkin24a.html), 4276–4306. Прочитаны первые восемь страниц: определение оценивателя, Assumption 2.3, Theorem 2.5; полные технические доказательства ещё не разобраны. Применимость ограничена моделью и условиями концентрации; эффективные ранги факторов остаются в оценках.
8. **Training a Tucker Model With Shared Factors: a Riemannian Optimization Approach.** [PMLR 238, AISTATS 2024](https://proceedings.mlr.press/v238/peshekhonov24a.html), 3304–3312; [исходная карточка ВШЭ 992233214](https://publications.hse.ru/chapters/992233214). Прочитан основной текст, приложения A.1–A.3 и B.1, остальные выборочно. [Код](https://github.com/johanDDC/tucker_riemopt). Ранговые условия и общие факторы не отождествляются с симметрией тензора.
9. **Quantized Tensor FEM for Multiscale Problems: Diffusion Problems in Two and Three Dimensions.** Multiscale Modeling & Simulation 20(3), 2022, 893–935; DOI [10.1137/20M1341659](https://doi.org/10.1137/20M1341659). Разобраны выбранные разделы [расширенной авторской версии ETH](https://www.sam.math.ethz.ch/sam_reports/reports_final/reports2020/2020-33_rev1.pdf), не все 41 страница. Предпосылки теории и численные примеры с разрывными коэффициентами разделены. Это QTT-переиндексация, а не квантование точности чисел.
10. **Cherry-Picking Gradients: Learning Low-Rank Embeddings of Visual Data via Differentiable Cross-Approximation.** [ICCV 2021, CVF](https://openaccess.thecvf.com/content/ICCV2021/html/Usvyatsov_Cherry-Picking_Gradients_Learning_Low-Rank_Embeddings_of_Visual_Data_via_Differentiable_ICCV_2021_paper.html), 11426–11435. Прочитаны механизм и основные эксперименты финального PDF; отдельное приложение не прочитано. [Код](https://github.com/prs-eth/c-pic). Дифференцируются вычисления при фиксированных индексах, не дискретный выбор maxvol.

## Как использовать подборку

[[30_mathematics/computational-algebra-principles/cap-hse-research-map|Карта направлений]] показывает место каждой работы и учебную очередь. Первый новый модуль [[30_mathematics/computational-algebra-principles/modules/cap-g01-fixed-rank-geometry|Г01]] разбирает математическое основание, а не все алгоритмы перечисленных статей. Содержательные результаты авторов, самостоятельные доказательства и наши конечные численные проверки различены. Наличие публичного кода не означает его аудит, запуск или воспроизведение опубликованных метрик.

Все страницы этой подборки имеют review и publish:false; разрешения на публикацию нет.
