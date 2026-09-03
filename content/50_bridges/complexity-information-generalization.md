---
id: bridge-complexity-information-generalization
title: "Сложность и информация → аудит обобщения"
aliases: ["Сложность и информация → аудит обобщения"]
type: application
status: canonical
publish: true
areas: [statistical-learning, information-theory, mathematics-for-ai]
concepts: [cross-area-transfer, model-design, failure-analysis]
prerequisites: [slt-course-map]
ai_domains: [statistical-learning, representation-learning, model-compression]
source_refs:
  - id: shashua-ml-notes-2009
    pages: "PDF 73–100"
    role: primary
  - id: stanford-ee376a-information-theory
    pages: "PDF 9–15"
    role: supporting
level: research
created: 2026-08-12
updated: 2026-09-03
---

# Сложность и информация → аудит обобщения

## Математическая сторона

Равномерная сходимость, VC-размерность, симметризация и взаимная информация измеряют разные аспекты адаптивности модели к данным.

## Задача ИИ

Валидация машинного обучения должна связывать выбранную меру сложности с процедурой выбора модели, зависимостью данных и фактическим распределительным сдвигом.

> [!info] Установлено (established)
> Конечноклассовые и VC-границы корректны при независимых одинаково распределённых наблюдениях и ограниченной функции потерь; неравенство обработки данных ограничивает информацию, создаваемую представлением.

> [!note] Аналогия (analogy)
> Граница похожа на плату за число просмотренных объяснений шума.

> [!warning] Гипотеза исследования (research hypothesis)
> Траекторно-зависимые меры сложности могут быть точнее глобальных, но сама адаптация должна входить в анализ.

## Режим отказа

Сравнение несопоставимых границ или оценка на тесте после подбора гиперпараметров создаёт ложную уверенность.

## Минимальная проверка переноса

Перенос следует проверять тремя связанными измерениями: величиной из математического утверждения, качеством последующей задачи ИИ и стоимостью вычисления. Настройки выбираются только по обучающей и проверочной выборкам; тестовая выборка используется один раз. Обязателен отрицательный контроль, в котором нарушается ключевое условие. Если математическая диагностика улучшается, а качество задачи не меняется, фиксируется граница полезности переноса, а не положительный результат.

## Связанные модули

- [[30_mathematics/statistical-learning-information-theory/modules/slt-01-risk-erm-pac]].
- [[30_mathematics/statistical-learning-information-theory/modules/slt-04-symmetrization-double-sampling]].
- [[30_mathematics/statistical-learning-information-theory/modules/slt-08-rate-distortion-generalization]].

## Визуализация переноса

![Три пути «сложность — данные — граница», вложенная проверка и распределительный сдвиг, красная адаптация по тестовой выборке](80_assets/next-release/webp-v1/bridge-complexity-information-generalization-v1.webp)
