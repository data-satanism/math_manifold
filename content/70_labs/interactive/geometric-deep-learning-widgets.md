---
id: lab-geometric-deep-learning-widgets
title: "Интерактивы курса геометрического глубокого обучения"
aliases: ["Интерактивные модели GDL"]
type: lab
status: canonical
publish: true
areas: [geometric-deep-learning, visualization]
concepts: [group-action, equivariance, geodesic, connection, message-passing, group-convolution]
prerequisites: [gdl-course-map]
ai_domains: [computer-vision, graph-ml, representation-learning]
source_refs: []
level: advanced
created: 2026-08-12
updated: 2026-08-12
---

# Интерактивы курса геометрического глубокого обучения

Все шесть лабораторий работают локально в браузере, не отправляют данные наружу и имеют статическую SVG-версию. Ползунки поддерживают клавиши со стрелками; результаты изменений озвучиваются через область `aria-live`.

1. [Орбиты и инварианты](80_assets/interactive/gdl-orbits.html) — действие группы и склеивание орбиты инвариантным признаком.
2. [Коммутативная диаграмма эквивариантности](80_assets/interactive/gdl-equivariance.html) — два пути через слой и измеримый дефект.
3. [Групповая свёртка](80_assets/interactive/gdl-group-convolution.html) — согласованный сдвиг входа и выхода.
4. [Геодезическая на сфере](80_assets/interactive/gdl-geodesics.html) — собственное расстояние и евклидова хорда.
5. [Калибровки и параллельный перенос](80_assets/interactive/gdl-gauge.html) — согласование локальных систем отсчёта связностью.
6. [Передача сообщений и сверхсглаживание](80_assets/interactive/gdl-message-passing.html) — распространение признака и потеря различимости узлов.

## Проверка доступности

- у всех элементов управления есть явные подписи;
- ползунки работают с клавиатуры;
- холст снабжён текстовым описанием;
- вывод параметров обновляется в области `aria-live`;
- цвет дублируется формой, положением или текстом;
- при отключённом JavaScript показывается статическая SVG-версия;
- компоновка адаптируется к узкому экрану.
