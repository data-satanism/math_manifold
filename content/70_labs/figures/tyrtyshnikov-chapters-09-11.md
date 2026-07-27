---
id: tyrtyshnikov-chapters-09-11-figure-registry
title: Реестр визуализаций к главам 9–11 Тыртышникова
aliases:
  - Визуализации спектральных алгоритмов
type: lab
status: canonical
publish: true
areas:
  - numerical-analysis
  - numerical-linear-algebra
concepts:
  - subspace-iteration
  - qr-algorithm
  - shifted-qr
prerequisites: []
ai_domains:
  - representation-learning
  - spectral-methods
source_refs:
  - id: tyrtyshnikov-numerical-analysis
    pages: "81–112"
    role: primary
level: advanced
created: 2026-07-14
updated: 2026-07-27
---

# Реестр визуализаций к главам 9–11

Неизменяемая стилевая часть промта:

> ICML-style scientific figure, clean academic vector infographic, white background, muted blue-gray palette with one accent color, minimal typography, precise arrows, thin lines, labeled panels, no photorealism, no 3D glossy rendering, no decorative background, conference-paper figure aesthetics, mathematically clean, visually balanced.

К каждому промту добавлялись требования: русский язык подписей, четыре панели «математическая идея → понятный образ → перенос в ИИ → границы применимости», отсутствие вымышленных чисел и маркировка статуса прикладного вывода.

| Файл | Содержательная часть промта |
|---|---|
| `nla-module-10-subspace-iteration-insight.png` | Степенной метод и итерации подпространств: усиление ведущих спектральных направлений, аналогия с настройкой приёмника, PCA и низкоразмерные представления. |
| `nla-module-11-qr-eigenvalue-insight.png` | QR-алгоритм: ортогонализация без изменения спектра, сортировка направлений, спектральный анализ ковариации. |
| `nla-module-12-shifted-qr-svd-insight.png` | Сдвиги, неявная QR-итерация и двудиагональная SVD: ускорение локальной сходимости и устойчивое выделение компонент. |
| `subspace-projector-distance-insight.png` | Одностороннее расстояние и норма разности проекторов; вложенные подпространства и сравнение признаковых представлений. |
| `cs-decomposition-insight.png` | Главные углы и CS-разложение: согласованные двумерные плоскости, аналогия с тенями, сравнение подпространств признаков. |
| `subspace-iteration-convergence-insight.png` | Спектральный зазор управляет сходимостью; фильтрация сигнала и устойчивое приближение ведущего подпространства. |
| `qr-algorithm-convergence-insight.png` | Одновременная итерация и QR-разложение; постепенное затухание поддиагональных элементов, спектральная диагностика. |
| `rayleigh-shift-quadratic-insight.png` | Локальная оценка $\varepsilon_{k+1}\le C\varepsilon_k^2$, аналогия с попаданием в мишень, критерий остановки. |
| `hermitian-qr-cubic-insight.png` | Кубическая сходимость для эрмитова случая при подходящем сдвиге; ускорение у цели и условия отказа. |
| `implicit-qr-uniqueness-insight.png` | Неявность QR: первый столбец определяет дальнейшие локальные вращения; аналогия с поездом и прогон выпячивания. |
| `bridge-principal-angles-drift-insight.png` | Главные углы как мера изменения представлений; аналогия с оркестром, контроль по подвыборкам и границы интерпретации. |
| `bridge-shifted-qr-diagnostics-insight.png` | Спектральные компоненты как частотные полосы; эффективная размерность, почти вырожденные направления и выбор числа компонент PCA. |

Автоматически сгенерированные варианты с математическими ошибками, искажёнными русскими подписями или необязательными англицизмами не интегрировались.

