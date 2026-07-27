---
id: linear-algebra-gaps-figures-v3
title: "Промпты визуализаций: завершение линейной алгебры"
aliases: ["Linear algebra gap figures v3"]
type: lab
status: canonical
publish: true
areas: [linear-algebra, scientific-visualization]
concepts: [visual-prompt, conceptual-figure, ai-transfer]
prerequisites: [boss-linear-algebra-map]
ai_domains: [representation-learning, graph-learning, dynamical-models]
source_refs:
  - id: boss-linear-algebra-2005
    pages: "10-180"
    role: primary
level: intermediate
created: 2026-07-27
updated: 2026-07-27
---

# Промпты визуализаций: завершение линейной алгебры

## Неизменяемая часть стиля

> ICML-style scientific figure, clean academic vector infographic, white background, muted blue-gray palette with one accent color, minimal typography, precise arrows, thin lines, labeled panels, no photorealism, no 3D glossy rendering, no decorative background, conference-paper figure aesthetics, mathematically clean, visually balanced.

Для всех фигур дополнительно требовались русские подписи, широкий формат, схема «механизм → понятный образ → перенос в ИИ → граница применимости» и запрет на усиление математического утверждения.

## Содержательные задания

1. **Координатная геометрия.** Один вектор в двух ортонормированных базисах; длины, углы и объёмы; повёрнутая карта; сохранение расстояний между эмбеддингами.
2. **Линейное распознавание.** Объект как вектор признаков; проекция на нормаль; измерительный прибор; линейная проба и согласованная замена базиса.
3. **Кэли—Гамильтон.** Характеристическое равенство; сворачивание цепочки степеней; конечная рекуррентность; полиномиальный графовый фильтр.
4. **Матричная экспонента.** Ряд и поток; полугрупповой закон; постоянное правило руления; непрерывная глубина и переходный рост.
5. **Альтернатива Гордана.** Ровно одна из систем $Ax>0$ и $A^Ty=0$, $y\ge0$, $y\ne0$; разделение; сертификат противоречия; линеаризованные ограничения ИИ.
6. **Перрон—Фробениус.** Положительный конус; нормированное отображение симплекса; устойчивый рецепт; примитивная марковская динамика и периодический контрпример.

## Результаты

- `80_assets/linear-algebra/gpt-image-v3/coordinate-invariants-embeddings-insight-v3.png`
- `80_assets/linear-algebra/gpt-image-v3/linear-recognition-probe-insight-v3.png`
- `80_assets/linear-algebra/gpt-image-v3/cayley-hamilton-recurrence-insight-v3.png`
- `80_assets/linear-algebra/gpt-image-v3/matrix-exponential-flow-insight-v3.png`
- `80_assets/linear-algebra/gpt-image-v3/gordan-alternative-certificate-insight-v3.png`
- `80_assets/linear-algebra/gpt-image-v3/perron-frobenius-positive-dynamics-insight-v3.png`

Фигура альтернативы была отдельным проходом исправлена: зелёный цвет удалён, а знак сложения между взаимоисключающими системами заменён подписью «ИЛИ, ровно одна».
