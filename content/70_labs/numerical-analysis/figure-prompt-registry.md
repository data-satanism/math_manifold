---
id: nla-figure-prompt-registry
title: "Реестр визуализаций курса численной линейной алгебры"
aliases: ["Промты фигур Тыртышникова", "NLA figure registry"]
type: lab
status: canonical
publish: true
areas: [numerical-analysis, scientific-visualization]
concepts: [visual-explanation, prompt-registry, reproducibility]
prerequisites: [numerical-linear-algebra-map]
ai_domains: [scientific-communication]
source_refs:
  - id: tyrtyshnikov-numerical-analysis
    pages: "3-78, 191-224"
    role: primary
level: intermediate
created: 2026-07-13
updated: 2026-07-27
---

# Реестр визуализаций курса численной линейной алгебры

## Неизменяемая стилевая часть промта

> ICML-style scientific figure, clean academic vector infographic, white background, muted blue-gray palette with one accent color, minimal typography, precise arrows, thin lines, labeled panels, no photorealism, no 3D glossy rendering, no decorative background, conference-paper figure aesthetics, mathematically clean, visually balanced.

К стилевой части всегда добавляются требования: формат 16:10, четыре панели, русские подписи, крупная типографика, отсутствие водяных знаков, логотипов, теней и декоративных элементов.

## Содержательная конструкция

Каждая фигура должна содержать четыре слоя:

1. точный математический механизм;
2. ключевое следствие или границу;
3. понятную аналогию, не подменяющую утверждение;
4. перенос в ИИ с маркировкой установленного результата, аналогии или гипотезы.

## Реестр файлов

| Файл | Страница | Краткая содержательная часть промта |
|---|---|---|
| `nla-module-01-insight.png` | [[30_mathematics/numerical-analysis/modules/01-spaces-and-norms]] | единичные шары, операторное растяжение, измерительная линза, геометрия потерь |
| `nla-module-02-insight.png` | [[30_mathematics/numerical-analysis/modules/02-unitary-matrices-and-svd]] | поворот–масштаб–поворот, сингулярный хвост, независимые каналы, PCA/LoRA |
| `nla-module-03-insight.png` | [[30_mathematics/numerical-analysis/modules/03-conditioning-and-matrix-series]] | эллипс чувствительности, сжатие итерации, узкая долина, переходный рост |
| `nla-module-04-insight.png` | [[30_mathematics/numerical-analysis/modules/04-spectral-localization-and-perturbation]] | круги Гершгорина, кластер, устойчивая группа, PCA и ненормальность |
| `nla-module-05-insight.png` | [[30_mathematics/numerical-analysis/modules/05-spectral-distances-and-clusters]] | назначение спектров, чередование, аккорд-кластер, устойчивое подпространство |
| `nla-module-06-insight.png` | [[30_mathematics/numerical-analysis/modules/06-floating-point-and-rounding-errors]] | машинная сетка, уничтожение цифр, соседняя задача, смешанная точность |
| `nla-module-07-insight.png` | [[30_mathematics/numerical-analysis/modules/07-lu-cholesky-and-refinement]] | выбор опоры, Холецкий, повторное использование маршрута, уточнение |
| `nla-module-08-insight.png` | [[30_mathematics/numerical-analysis/modules/08-qr-and-orthogonalization]] | базис и координаты, отражение, вращение, независимые роли |
| `nla-module-09-insight.png` | [[30_mathematics/numerical-analysis/modules/09-iterative-solvers-and-preconditioning]] | итерация, пространства Крылова, выпрямление долины, линейная подзадача |
| `eckart-young-insight.png` | [[30_mathematics/numerical-analysis/theorems/eckart-young-theorem]] | сильнейшие каналы, две нормы хвоста, бюджет связи, PCA/сжатие/LoRA |
| `gershgorin-circles-insight.png` | [[30_mathematics/numerical-analysis/theorems/gershgorin-circles]] | максимальная компонента, круги, зоны влияния, быстрый спектральный фильтр |
| `wielandt-hoffman-insight.png` | [[30_mathematics/numerical-analysis/theorems/wielandt-hoffman-theorem]] | оптимальное согласование, бюджет Фробениуса, назначение ролей, дрейф спектра |
| `weyl-perturbation-insight.png` | [[30_mathematics/numerical-analysis/theorems/weyl-eigenvalue-perturbation]] | полосы допуска, минимакс, сохранение зазора, устойчивость PCA |
| `cholesky-factorization-insight.png` | [[30_mathematics/numerical-analysis/theorems/cholesky-factorization]] | треугольный квадрат, дополнение Шура, слои энергии, ковариации |
| `qr-factorization-insight.png` | [[30_mathematics/numerical-analysis/theorems/qr-factorization]] | ортонормированный словарь, треугольный рецепт, единственность, приложения |
| `bridge-conditioning-optimization-insight.png` | [[50_bridges/conditioning-optimization-geometry]] | квадратичная долина, смена координат, граница нелинейного переноса |
| `bridge-svd-pca-lora-insight.png` | [[50_bridges/svd-pca-compression-lora]] | SVD, центрированная PCA, сжатие, отделение теоремы от LoRA-гипотезы |
| `bridge-spectral-perturbation-rmt-insight.png` | [[50_bridges/spectral-perturbation-rmt]] | детерминированный допуск, шумовой массив, двойная проверка, выравнивание |
| `bridge-krylov-preconditioning-insight.png` | [[50_bridges/krylov-preconditioning-ml]] | матрично-свободные произведения, согласованные направления, лабиринт, стоимость |
| `bridge-mixed-precision-insight.png` | [[50_bridges/backward-stability-mixed-precision]] | FP16/BF16, накопление FP32, масштабирование, точная невязка |
| `bridge-qr-subspace-insight.png` | [[50_bridges/qr-subspace-low-rank]] | случайный набросок, умножение+QR, независимые партии, эффективный ранг |

## Проверка перед публикацией

- формулы и геометрия сверены с соответствующей заметкой;
- основной текст изображения — русский;
- англоязычные аббревиатуры допускаются только для общепринятых имён методов и форматов;
- аналогия визуально отделена от теоремы;
- гипотеза не оформлена как доказанный результат;
- исходный PNG имеет ширину не меньше 1500 пикселей;
- альтернативная подпись в Markdown объясняет смысл, а не повторяет имя файла.

Все изображения созданы отдельными запросами встроенной модели генерации изображений и сохранены в `80_assets/numerical-analysis/gpt-image-v1`.
