---
id: lab-markov-networks-graphical-kernels-figures
title: "Промпты иллюстраций: марковские сети и графические ядра"
aliases: ["Иллюстрации раздела 5.2 ядерных методов"]
type: lab
status: canonical
publish: true
areas: [kernel-methods, probabilistic-graphical-models, scientific-visualization]
concepts: [markov-network, clique-factorization, graph-compatible-kernel, junction-tree]
prerequisites: [km-05-markov-networks-graph-compatible-kernels]
ai_domains: [structured-prediction, sequence-labeling, probabilistic-modeling]
source_refs:
  - id: hofmann-scholkopf-smola-kernel-methods-2006
    pages: "36-38"
    role: visual-source
level: advanced
created: 2026-07-21
updated: 2026-07-27
---

# Промпты иллюстраций: марковские сети и графические ядра

Изображения создаются встроенной GPT.Image моделью и сохраняются в новой версии `80_assets/kernel-methods/gpt-image-v4`. Текст внутри изображения служит только объяснительным слоем; точные определения и утверждения находятся в Markdown.

## Общий неизменный префикс

> ICML-style scientific figure, clean academic vector infographic, white background, muted blue-gray palette with one accent color, minimal typography, precise arrows, thin lines, labeled panels, no photorealism, no 3D glossy rendering, no decorative background, conference-paper figure aesthetics, mathematically clean, visually balanced.

> Russian-first scientific labels; use English only for standard abbreviations. Clearly distinguish established result, analogy, research hypothesis, and failure mode.

## Модуль

Файл: `gpt-image-v4/markov-networks-graph-compatible-kernels-module-v4.png`

Промпт после общего префикса:

> Use case: scientific-educational. Landscape course-module figure «Марковские сети и совместимые с графом ядра». Panel A «Математическая идея»: show an undirected dependency graph, highlight maximal cliques, turn clique-local scores into one global score, then show a graph-compatible kernel assembled from local blocks and messages passing through small separators. Keep formulas minimal and exact: «глобальная оценка = сумма локальных». Panel B «Понятный образ»: a route through several scientific control stations; each station checks only a local segment and neighboring stations exchange a compact manifest through their shared gate. Explicit mapping: station→clique, gate→separator, manifest→message. Panel C «Перенос в ИИ»: sequence labeling with observation windows, neighboring labels, exact dynamic programming and a diagnostic «древесная ширина»; label «установлено». Warning strip «Режим отказа»: zero-probability parity pattern, nonlocal kernel interaction, wide separator. Russian labels only except RKHS; no neural-network decoration.

## Теорема Хаммерсли—Клиффорда

Файл: `gpt-image-v4/hammersley-clifford-factorization-v4.png`

Промпт после общего префикса:

> Use case: scientific-educational. Landscape theorem figure «Теорема Хаммерсли—Клиффорда». Panel A «Математическая идея»: positive probability table «p > 0», undirected graph with three highlighted maximal cliques, arrows to local positive potentials and their normalized product; show that a missing edge means conditional independence given the rest. Panel B «Понятный образ»: several overlapping expert committees coordinate a single plan; each committee sees one clique, shared members enforce consistency; clearly map committee→clique and local rule→potential. Panel C «Перенос в ИИ»: a compact conditional random field for sequence labels with local observation and transition potentials, labeled «установлено», plus check «нормировка». Warning strip «Режим отказа»: even-parity distribution with four allowed and four forbidden binary states, pairwise checks pass but global factorization over an empty graph fails because probabilities are zero. Do not claim pairwise independence implies mutual independence; no dense equations.

## Разложение совместимого ядра

Файл: `gpt-image-v4/graph-compatible-kernel-decomposition-v4.png`

Промпт после общего префикса:

> Use case: scientific-educational. Landscape theorem figure «Разложение совместимого с графом ядра». Panel A «Математическая идея»: every function is a sum of clique-local components; show a kernel section k(·,z) splitting by cliques of the first argument and, by symmetry, by cliques of the second, producing a grid of local blocks k_cd whose sum is the full kernel. Clearly note «положительно определена полная сумма», not each block. Panel B «Понятный образ»: compare two modular scientific instruments through a matrix of module-to-module interface tests; module→clique, interface test→k_cd. Panel C «Перенос в ИИ»: local observation and transition kernels for sequence labeling, full Gram matrix spectrum checked nonnegative, label «установлено». Warning strip «Режим отказа»: a global multiplicative RBF interaction spans two disconnected variables and cannot be written as the required additive local blocks; incorrect block weighting can make the full Gram matrix indefinite. Russian-first labels, RKHS and RBF allowed.

## Кликовое представление

Файл: `gpt-image-v4/clique-representer-sparse-expansion-v4.png`

Промпт после общего префикса:

> Use case: scientific-educational. Landscape theorem figure «Кликовое представление решения». Panel A «Математическая идея»: a huge catalog of complete label sequences of size q^T collapses by grouping identical clique restrictions into local coefficient drawers, with exact comparison «q^T → (T−1)q²» for a pairwise chain; then local kernel blocks reconstruct the score. Panel B «Понятный образ»: replace a catalog of every complete sentence with a dictionary of local fragments plus explicit stitching rules; fragment→clique configuration, stitching→graph consistency. Panel C «Перенос в ИИ»: structured SVM or CRF sequence labeling with local basis elements and dynamic programming, labeled «установлено», diagnostic «число ненулевых коэффициентов». Warning strip «Режим отказа»: compact grouping does not guarantee numerical sparsity; large cliques remain exponential; greedy reduced set needs an error estimate. No claim that coefficients are probabilities.

## Вероятностный вывод

Файл: `gpt-image-v4/graphical-kernel-probabilistic-inference-v4.png`

Промпт после общего префикса:

> Use case: scientific-educational. Landscape method figure «Вероятностный вывод в графической ядерной модели». Panel A «Математическая идея»: convert a small factor graph into a junction tree; arrows carry message tables only over separator variables; one branch uses sums for marginals and normalization, another uses maxima plus backpointers for MAP. Panel B «Понятный образ»: neighboring control stations exchange a manifest listing only states at their shared gate; narrow gate gives a short manifest, wide gate gives an exponentially large one. Explicit mapping gate→separator and manifest→message. Panel C «Перенос в ИИ»: chain labeling with forward-backward for probabilities and Viterbi for the best sequence, labeled «установлено», diagnostic «согласованность маргиналов». Warning strip «Режим отказа»: high treewidth, loopy approximate messages, MAP is not uncertainty. Russian labels only except MAP; avoid invented numerical data.

## AI-мост

Файл: `gpt-image-v4/graphical-kernels-structured-inference-bridge-v4.png`

Промпт после общего префикса:

> Use case: scientific-educational. Landscape bridge figure «Графические ядра → структурный вывод в ИИ». Use panel titles «Математическая структура», «Интуитивный перенос», «ИИ: механизм и проверка» and a warning strip «Режим отказа». First panel: local score sum, positive clique factorization, local kernel-block matrix, and message passing as one linked mechanism; show preserved invariant «локальность по кликам». Second panel: modular teams coordinate a project through shared interfaces; team→clique, interface→separator, compatibility test→kernel block, status summary→message. Third panel: two established branches—CRF probabilities through forward-backward and structured SVM competitor search through dynamic programming; one dashed research-hypothesis branch for a neural-local-potential hybrid. Diagnostics: «древесная ширина», «спектр матрицы Грама», «согласованность маргиналов», «ошибка оракула». Failure strip: zero support, nonlocal interaction, indefinite full kernel, approximate inference treated as exact. Russian-first labels; standard abbreviations CRF, SVM, RKHS allowed.

## Контрольные суммы

Встроенный режим GPT.Image; окончательные отобранные файлы:

| Файл | SHA-256 |
|---|---|
| `clique-representer-sparse-expansion-v4.png` | `6bed1cf7798e21d9d90877e103d9fadec029e8f0d7416e3bf3e3a0f5b8e12fba` |
| `graph-compatible-kernel-decomposition-v4.png` | `4ef65dac21dfd9a0d17552a6bbcbeaf5bc3b396a96768885e8433a11bd6391b8` |
| `graphical-kernel-probabilistic-inference-v4.png` | `b242c0b7a8935cb2ff1382c69d0f8fd93847000fb8946295acb27f700ce68d68` |
| `graphical-kernels-structured-inference-bridge-v4.png` | `51f03e057c9cd2fdf68d3fd03b045c28bd72e8613475c0f5d0c186523b63d8ef` |
| `hammersley-clifford-factorization-v4.png` | `deb3caade5d41bb90416f13a09a8dddfd0bc90ad2e24c2f9daef051ef6a54b6e` |
| `markov-networks-graph-compatible-kernels-module-v4.png` | `3754597dfe8713f63d422dd06b286378a2a497396a3b2348e0ef573fe02bd579` |

## Редакционные итерации

- В теореме Хаммерсли—Клиффорда все обозначения сведены к четырём переменным в основной панели; вероятности заменены на точные $1/16$, а контрпример чётности оставлен отдельным трёхмерным распределением.
- В кликовом представлении английские фрагменты заменены русскими, `inference` заменено на «вывод», а название алгоритма дано как «Витерби».
- В вероятностном выводе переведены названия алгоритма вперёд—назад, древесной ширины и циклической передачи сообщений.
- AI-мост перегенерирован после отклонения версии, ошибочно приписывавшей положительность каждому локальному блоку. В финале положительная определённость относится только к полной матрице Грама.
