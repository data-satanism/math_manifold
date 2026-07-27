---
id: lab-kernel-unsupervised-learning-figures
title: "Промпты иллюстраций: ядерные методы обучения без учителя"
aliases: ["Иллюстрации раздела 6 ядерных методов"]
type: lab
status: canonical
publish: true
areas: [kernel-methods, unsupervised-learning, scientific-visualization]
concepts: [kernel-pca, kernel-canonical-correlation, hsic, mmd, pre-image]
prerequisites: [km-06-unsupervised-kernel-methods]
ai_domains: [representation-learning, multimodal-learning, distribution-shift, structured-prediction]
source_refs:
  - id: hofmann-scholkopf-smola-kernel-methods-2006
    pages: "38-41"
    role: visual-source
level: advanced
created: 2026-07-21
updated: 2026-07-27
---

# Промпты иллюстраций: ядерные методы обучения без учителя

Изображения создаются встроенной GPT.Image моделью и сохраняются в новой версии `80_assets/kernel-methods/gpt-image-v5`. Текст внутри изображения служит объяснительным слоем; формулировки и доказательства находятся в Markdown.

## Общий неизменный префикс

> ICML-style scientific figure, clean academic vector infographic, white background, muted blue-gray palette with one accent color, minimal typography, precise arrows, thin lines, labeled panels, no photorealism, no 3D glossy rendering, no decorative background, conference-paper figure aesthetics, mathematically clean, visually balanced.

> Russian-first scientific labels; use English only for standard abbreviations. Clearly distinguish established result, analogy, research hypothesis, and failure mode.

## Модуль

Файл: `gpt-image-v5/unsupervised-kernel-methods-module-v5.png`

Промпт после общего префикса:

> Use case: scientific-educational. Landscape course-module figure «Ядерные методы обучения без учителя». Panel A «Общая механика»: paired and unpaired samples enter centered Gram matrices, then branch into five clearly distinct tasks: kernel PCA «вариация», KCCA «парные направления», HSIC «зависимость», MMD «два распределения», structured-output pre-image «допустимый ответ». Use only the compact exact labels Kc=HKH, ||Cxy||², ||μP−μQ||. Panel B «Понятный образ»: one scientific laboratory with instruments; operating modes of one instrument→kernel PCA, calibrating two paired instruments→KCCA, hidden coupling test→HSIC, comparing two batches→MMD, blueprint-to-valid-part→pre-image. Panel C «Перенос в ИИ»: multimodal representations, removal of nuisance information, dataset-shift monitoring and structured decoding, each connected to the correct branch and labeled «установлено» where appropriate. Warning strip «Режим отказа»: no centering, no KCCA regularization, non-characteristic kernel, nonunique pre-image. Russian labels only except PCA, KCCA, HSIC, MMD, RKHS.

## Ядерный метод главных компонент

Файл: `gpt-image-v5/kernel-pca-centered-gram-v5.png`

Промпт после общего префикса:

> Use case: scientific-educational. Landscape method figure «Ядерный метод главных компонент». Panel A «Математическая идея»: curved two-dimensional data, implicit feature map, centered Gram matrix Kc=HKH, eigenspectrum and one nonlinear coordinate; show «обычный PCA уже разобран» as a small incoming link, not repeated derivation. Panel B «Понятный образ»: an initially curved calibrated measuring tape is conceptually unfolded into a straight coordinate; explicit mapping mark similarity→kernel, remove common offset→centering, main direction→principal component. Panel C «Перенос в ИИ»: nonlinear dimensionality reduction and denoising with a held-out stability check, labeled «установлено»; dashed branch «спектральная диагностика представлений» labeled «исследовательская гипотеза». Warning strip «Режим отказа»: constant kernel gives Kc=0, missing centering, nearly tied eigenvalues, projected RKHS point has no unique pre-image. Russian-first labels; PCA and RKHS allowed; do not draw the feature map as an invertible bijection.

## Ядерная каноническая корреляция

Файл: `gpt-image-v5/kernel-canonical-correlation-v5.png`

Промпт после общего префикса:

> Use case: scientific-educational. Landscape method figure «Ядерная каноническая корреляция». Panel A «Математическая идея»: paired observations (xi,yi), two centered Gram matrices, two regularized whitening blocks, then maximally aligned canonical coordinates; emphasize «регуляризация обязательна». Panel B «Понятный образ»: two scientific instruments observe the same process with nonlinear scales; calibration aligns shared fluctuations, while a smoothness clamp prevents carving one tick per training pair. Explicit mapping instrument→view, calibration curve→RKHS function, clamp→regularization. Panel C «Перенос в ИИ»: image-text or sensor-signal representation alignment with train versus held-out correlation and a permutation baseline; established label on KCCA, dashed research-hypothesis label on neural representation diagnosis. Warning strip «Режим отказа»: shuffled pairs, no centering, zero regularization gives near-one training correlation, causal claim from symmetric correlation. Russian labels only except KCCA and RKHS.

## Независимость через оператор перекрёстной ковариации

Файл: `gpt-image-v5/rkhs-cross-covariance-independence-v5.png`

Промпт после общего префикса:

> Use case: scientific-educational. Landscape theorem figure «Независимость через оператор перекрёстной ковариации RKHS». Panel A «Математическая идея»: show X symmetric and Y=X² as a clear nonlinear dependent pattern with ordinary covariance zero, then a rich panel of RKHS test functions feeding Cxy and HSIC=||Cxy||²; under a characteristic product kernel mark «HSIC=0 ⇔ независимость». Panel B «Понятный образ»: one linear motion sensor misses a curved coupling, while a calibrated panel of diverse nonlinear sensors detects it; sensor panel richness→characteristic kernel. Panel C «Перенос в ИИ»: representation Z and nuisance attribute A, HSIC diagnostic, permutation null distribution and held-out check; established label on the population criterion, dashed research-hypothesis label on fairness regularization. Warning strip «Режим отказа»: constant kernel is a blind sensor, wrong row pairing, bandwidth selected by final p-value, temporal dependence invalidates naive permutation. Russian-first labels; HSIC and RKHS allowed; do not claim small empirical HSIC proves independence.

## Среднее вложение и MMD

Файл: `gpt-image-v5/kernel-mean-embedding-mmd-v5.png`

Промпт после общего префикса:

> Use case: scientific-educational. Landscape theorem figure «Среднее вложение распределения и MMD». Panel A «Математическая идея»: distributions P and Q map to mean elements μP and μQ in RKHS; show MMD² as within-P similarity plus within-Q similarity minus twice cross-similarity; characteristic kernel gives «MMD=0 ⇔ P=Q». Panel B «Понятный образ»: each data batch produces an average similarity fingerprint measured against many probes; characteristic probe set means different batches cannot share the same population fingerprint. Panel C «Перенос в ИИ»: baseline versus current representation stream, calibrated threshold, block-aware resampling and effect-size panel; established label on the two-sample criterion, dashed hypothesis on multi-kernel monitoring. Warning strip «Режим отказа»: constant kernel gives the same fingerprint, bad bandwidth, dependent time samples, statistical significance confused with practical importance. Russian labels only except MMD and RKHS; show two unpaired samples, not paired variables.

## Оценивание зависимости и прообраз

Файл: `gpt-image-v5/kernel-dependency-estimation-preimage-v5.png`

Промпт после общего префикса:

> Use case: scientific-educational. Landscape method figure «Ядерное оценивание зависимости и задача прообраза». Panel A «Математическая идея»: structured outputs are embedded by an output kernel, centered kernel PCA keeps r output coordinates, regularized regressors predict the coordinates from x, then a separate argmin searches the nearest valid y; label three errors «усечение», «регрессия», «декодирование». Panel B «Понятный образ»: a continuous engineering blueprint is predicted in a design space, but the workshop must choose a manufacturable part from a discrete catalog; two parts may be equally close. Explicit mapping blueprint→predicted RKHS element, catalog→valid output set, manufacturing choice→pre-image. Panel C «Перенос в ИИ»: sequence or graph output with structured-kernel similarity and a decoding oracle, labeled «установлено»; dashed hypothesis on using the method as a small neural-decoder benchmark. Warning strip «Режим отказа»: rare structure removed by truncation, no exact pre-image, nonunique nearest output, output kernel disagrees with task loss. Russian-first labels; PCA and RKHS allowed.

## AI-мост

Файл: `gpt-image-v5/kernel-independence-representation-learning-bridge-v5.png`

Промпт после общего префикса:

> Use case: scientific-educational. Landscape bridge figure «Ядерные меры зависимости → обучение и диагностика представлений». Use panels «Математическая структура», «Понятный перенос», «ИИ: механизм и проверка» and a bottom warning strip. First panel must separate four questions with no conflation: spectrum of Cxx→variation, regularized whitened Cxy→paired alignment, ||Cxy||²→independence, ||μP−μQ||→two-distribution shift. Second panel: laboratory table mapping one-instrument modes, two-instrument calibration, hidden coupling test and two-batch fingerprint comparison to PCA, KCCA, HSIC and MMD. Third panel: image-text alignment, nuisance-information diagnostic and data-drift monitoring; show held-out correlation, permutation test, calibrated threshold and RMT spectrum check. Use solid arrows for established mechanisms, dotted arrows for analogy and dashed arrows for research hypothesis. Warning strip: wrong question/statistic, double use of data, blind kernel, temporal dependence, causal overclaim. Russian labels only except PCA, KCCA, HSIC, MMD, RMT.

## Контрольные суммы

Встроенный режим GPT.Image; окончательные отобранные файлы:

| Файл | SHA-256 |
|---|---|
| `kernel-canonical-correlation-v5.png` | `bd31846adf6e6bf875eda317112e55b702cdb0018ade10f2063f1a35c5dab36f` |
| `kernel-dependency-estimation-preimage-v5.png` | `3fd62b74638d282ed6d601733427a581c025045d86a84cbcfaf4f0b44b23154d` |
| `kernel-independence-representation-learning-bridge-v5.png` | `6d02d6b801c4400c44b4e23157bb66e472dbc1f9bcf735d52b8999891cc9c137` |
| `kernel-mean-embedding-mmd-v5.png` | `09cb097bdf32d38cee8435b1b26749b0ed9a4af89445448aa631efc5ecafea8f` |
| `kernel-pca-centered-gram-v5.png` | `a744d16d4bdb362e69b9c1c391d296c4b1cba514f3b583c27e20f533b79794c9` |
| `rkhs-cross-covariance-independence-v5.png` | `d0e1efa343e74cf266dad165030a7993819d2b548afb790c1c82c2acfed6ff50` |
| `unsupervised-kernel-methods-module-v5.png` | `635f76327dc8ead5471c2a7dad512ad19ff25ec27490e246e6f28cb10f43d526` |

## Редакционные итерации

- В модульной фигуре `Pre-image`, «сдвиг датасета» и «эмбеддинги» заменены на «поиск прообраза», «сдвиг данных» и «средние элементы RKHS».
- В фигуре ядерного PCA заменены `Kernel PCA`, `train`, `held-out` и «денойзинг»; сохранено предупреждение о неединственном прообразе.
- В KCCA удалены англоязычные подписи обучающей и проверочной выборок; математическое обозначение $\operatorname{corr}$ оставлено как часть формулы.
- В HSIC заменены `nuisance`, `p-value`, `train`, `held-out` и `data snooping`; популяционная эквивалентность отделена от эмпирического теста.
- В MMD «дрейф», «мульти-ядра» и сокращение ФДР заменены на «сдвиг данных», «несколько ядер» и «контроль множественных проверок».
- В задаче прообраза `benchmark` и `neural-decoder` заменены на «контролируемый эталон» и «нейронный декодер».
- В AI-мосте `nuisance`, `data drift` и `reference` заменены русскими научными терминами; четыре статистических вопроса оставлены раздельными.
