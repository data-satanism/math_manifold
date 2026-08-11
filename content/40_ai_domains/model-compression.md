---
id: ai-domain-model-compression
title: "Сжатие и эффективные модели: математическая карта"
aliases: ["Математика сжатия моделей", "Model compression map"]
type: map
status: canonical
publish: true
areas: [artificial-intelligence, model-compression, knowledge-navigation]
concepts: [low-rank-approximation, conditioning, quantization, structured-matrices]
prerequisites: [mathematics-integration-map]
ai_domains: [model-compression, efficient-ai, large-language-models]
source_refs: []
level: advanced
created: 2026-07-27
updated: 2026-08-12
description: "Математические основания низкого ранга, структурных матриц и устойчивого снижения точности."
---

# Сжатие и эффективные модели: математическая карта

## 1. Низкоранговое приближение

- [[50_bridges/svd-pca-compression-lora|SVD, PCA, сжатие и LoRA]] связывает сингулярные числа с оптимальной ошибкой аппроксимации.
- [[50_bridges/qr-subspace-low-rank|QR-разложение и низкоранговые подпространства]] показывает устойчивый поиск базиса.
- [[30_mathematics/numerical-analysis/theorems/eckart-young-theorem|Теорема Эккарта—Янга]] задаёт эталон ошибки.

**Установленный результат:** усечённое SVD оптимально в спектральной и фробениусовой нормах.
**Граница:** минимальная матричная ошибка не гарантирует минимальную деградацию качества модели.

## 2. Выбор ранга

- [[50_bridges/rmt-spectral-diagnostics|RMT и спектральная диагностика]] отделяет устойчивые выбросы от шумового объёма.
- [[50_bridges/spectral-perturbation-rmt|Спектральные возмущения и RMT]] оценивает стабильность найденного подпространства.
- [[50_bridges/principal-angles-representation-drift|Главные углы]] измеряют изменение представлений.

Выбор ранга по RMT для LoRA остаётся **исследовательской гипотезой**, пока не задана вероятностная модель обновлений и проверка на независимых данных.

## 3. Структурное ускорение

- [[50_bridges/hierarchical-matrices-kernel-attention|Иерархические матрицы и быстрое внимание]].
- [[30_mathematics/numerical-analysis/modules/25-structured-toeplitz-circulant|Тёплицевы и циркулянтные операторы]].
- [[30_mathematics/numerical-analysis/modules/26-hierarchical-low-rank-wavelets|Иерархический низкий ранг]].

## 4. Низкая точность и обусловленность

- [[50_bridges/backward-stability-mixed-precision|Обратная устойчивость и смешанная точность]] объясняет, когда округлённый результат остаётся решением близкой задачи.
- [[50_bridges/conditioning-optimization-geometry|Обусловленность]] определяет, насколько близкая задача имеет близкий ответ.

## Проверяемые метрики

1. Ошибка аппроксимации в норме, согласованной с оператором.
2. Изменение функции потерь на контрольных данных.
3. Угол между исходным и сжатым подпространствами.
4. Остаток, обратная ошибка и чувствительность к точности.
