---
id: lab-myshkis-applied-mathematics-ch01-figures
title: "Промпты иллюстраций: теория поля Мышкиса"
aliases: ["Field theory figure prompts", "Иллюстрации главы 1 Мышкиса"]
type: lab
status: canonical
publish: true
areas: [applied-mathematics, scientific-visualization]
concepts: [vector-field, divergence, curl, conservation-law]
prerequisites: [apm-01-field-theory]
ai_domains: [scientific-machine-learning, neural-operators]
source_refs:
  - id: myshkis-applied-mathematics-engineers-2006
    pages: "11-36"
    role: primary
level: advanced
created: 2026-07-16
updated: 2026-07-27
---

# Промпты иллюстраций: теория поля

## Общая неизменяемая часть

> ICML-style scientific figure, clean academic vector infographic, white background, muted blue-gray palette with one accent color, minimal typography, precise arrows, thin lines, labeled panels, no photorealism, no 3D glossy rendering, no decorative background, conference-paper figure aesthetics, mathematically clean, visually balanced. Russian-first scientific labels; use English only for standard abbreviations. Clearly distinguish established result, analogy, research hypothesis, and failure mode.

## Модуль

Фигура `apm-ch01-field-theory-insight.png`: три панели «Математическая идея», «Понятный образ», «Перенос в ИИ». Показать градиент скалярного поля, источники и стоки дивергенции, вихри ротора; сопоставить их с насосом, сливом, колесом и расходомером; затем показать нейронный оператор, локальные остатки и глобальные интегральные проверки. В полосе отказа показать малую поточечную ошибку со скрытым источником или вихрем.

## Формула Остроградского

Фигура `gauss-ostrogradsky-insight.png`: замкнутая область, внешние нормали, источники и формула $\int_{\partial\Omega}A\cdot n\,dS=\int_\Omega\operatorname{div}A\,dV$. Аналогия — склад, где производство и поступление определяют чистый выход. Перенос — конечно-объёмная нейросетевая модель и остаток закона сохранения. Отказы — незамкнутая поверхность, неверная ориентация и неучтённый сингулярный источник.

## Формула Стокса

Фигура `stokes-theorem-insight.png`: ориентированная поверхность, согласованный контур, локальные колёса и формула $\int_{\partial S}A\cdot dr=\int_S\operatorname{rot}A\cdot n\,dS$. Внутренние рёбра сокращаются. Перенос — сравнение потока ротора и циркуляции на участке сетки. Все прозаические подписи строго на русском; запрещены английские слова `curl`, `flux`, `loop`, `circulation`, `patch`, `field`, `loss`, `training`.

## AI-мост

Фигура `field-invariants-ai-insight.png`: локальные невязки `div` и `rot`, глобальные проверки потока и циркуляции, сеть шумных датчиков и нейронный оператор с локальным и глобальным контролем. Явно отметить установленный результат, аналогию и исследовательскую гипотезу. В полосе отказа показать, что ошибка обучения убывает, а ошибка баланса остаётся; точная квадратура обнаруживает утечку, грубая скрывает её. Английская проза запрещена; допустимы только стандартные аббревиатуры AI, PDE, GNO и FNO.

## Принятые файлы

- `80_assets/applied-mathematics/gpt-image-v1/apm-ch01-field-theory-insight.png`;
- `80_assets/applied-mathematics/gpt-image-v1/gauss-ostrogradsky-insight.png`;
- `80_assets/applied-mathematics/gpt-image-v1/stokes-theorem-insight.png`;
- `80_assets/applied-mathematics/gpt-image-v1/field-invariants-ai-insight.png`.

Два ранних варианта не подключены: в них присутствовала английская проза внутри русских панелей.
