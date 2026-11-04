---
id: branches17-selection-and-greedy-lab
title: "Лаборатория: объём, DEIM, несмещённость и два жадных механизма"
aliases: []
type: lab
status: canonical
publish: true
areas: [numerical-analysis, numerical-linear-algebra]
concepts: [max-volume, interpolation, greedy-approximation]
prerequisites: [cap-05-rectangular-d-optimal, cap-06-deim, cap-07-volume-sampling]
ai_domains: [compression, scientific-ml]
source_refs:
  - id: selection-regression-primary-sources
    pages: "Собственные малые примеры к теоремам"
    role: primary
  - id: kashin-two-bases-primary-sources
    pages: "Алгоритмическая формула; эксперимент авторов не воспроизводится"
    role: primary
level: advanced
created: 2026-11-04
updated: 2026-11-04
---

# Воспроизводимая проверка формул

Сценарий `70_labs/figures/branches17_scientific_v1.py` использует NumPy, SciPy и Matplotlib; случайное начальное состояние — 20261104. Запуск из корня хранилища:

```powershell
py -3.11 70_labs/figures/branches17_scientific_v1.py
```

Он создаёт десять пар SVG/PNG в `80_assets/computational-algebra-principles/plots-v2-branches17` и `numerical-qa.json` в `90_admin/reports/full-plan-2026-11-04/branches17`. Проверки останавливают сценарий при нарушении ожидаемых тождеств. Сравнение времени не проводится.

| Опыт | Что проверяется | Результат контрольного запуска |
|---|---|---|
| Разнородный шум | Полный перебор двух из четырёх строк | Набор $(1,2)$ без весов; $(2,3)$ с весами |
| DEIM | Идемпотентность и достижение нормы на ортогональном остатке | Норма $4.5823293$; отношение ошибок такое же с точностью $10^{-12}$ |
| Объёмная регрессия | Все наборы при $n=4,d=2,s=2,3,4$ | Ошибка среднего не выше $7.3\cdot10^{-16}$ |
| Прямоугольный максимум | Все тройки строк малой матрицы; восстановление и внешние коэффициенты | Ошибка восстановления $2.3\cdot10^{-16}$; нормы $0.444$ и $0.578$ при границе 1 |
| Два базиса | $N=128$, 8 ненулевых компонент, 45 шагов | Остатки $2.71\cdot10^{-10}$ и $9.20\cdot10^{-11}$ |
| Проекционный выбор | Одна общая предыстория в $\mathbb R^3$ | Максимумы исходной и нормированной корреляций приходятся на разные атомы |

Индексы в таблице начинаются с 1, в JSON — с 0. Числа могут слегка меняться между библиотеками линейной алгебры; проверяются тождества с допуском, а не побитовое совпадение.

![Среднее объёмных оценок проверяется полным перебором](80_assets/computational-algebra-principles/plots-v2-branches17/cap-07-unbiased-geometry.svg)

[Открыть рисунок в полном размере](80_assets/computational-algebra-principles/plots-v2-branches17/cap-07-unbiased-geometry.svg)

Для Кашина проверяется тождество $x=u+T^Tb+r$, спад остатка и диапазон двух частей. Операторы здесь хранятся плотными для прозрачной проверки. Поэтому опыт **не измеряет ускорение быстрого преобразования**; заявленная стоимость $O(N\log N)$ относится к реализации (3) через быстрые преобразования, которой этот малый сценарий не подменяет.

![Изменение диапазона координат проверяется отдельно от ошибки остатка](80_assets/computational-algebra-principles/plots-v2-branches17/journal-01-kashin-coordinates.svg)

[Открыть рисунок в полном размере](80_assets/computational-algebra-principles/plots-v2-branches17/journal-01-kashin-coordinates.svg)

Бесконечномерный контрпример Бородина не моделируется конечной матрицей. Его второй рисунок показывает лишь суммируемый бюджет потерь, а первый — различие критериев выбора. Это помогает не принять конечный расчёт за доказательство расходимости.

Связанные модули: [[30_mathematics/computational-algebra-principles/modules/cap-05-rectangular-d-optimal]], [[30_mathematics/computational-algebra-principles/modules/cap-06-deim]], [[30_mathematics/computational-algebra-principles/modules/cap-07-volume-sampling]], [[30_mathematics/computational-algebra-principles/modules/journal-01-kashin-two-bases]], [[30_mathematics/computational-algebra-principles/modules/journal-02-greedy-projection]].
