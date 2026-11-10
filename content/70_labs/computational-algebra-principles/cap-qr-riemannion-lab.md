---
id: cap-qr-riemannion-lab
title: 'Лаборатория А04–Г02: QR, сильный RRQR, LOI и спектральный шаг'
aliases: []
type: lab
status: canonical
publish: true
areas:
- numerical-linear-algebra
concepts:
- qr-factorization
- numerical-rank
- rank-revealing-factorization
prerequisites:
- cap-a04-qr-numerical-rank
- cap-g02-riemannion
ai_domains:
- compression
- parameter-efficient-fine-tuning
source_refs:
- id: source-qr-rank-revealing
  pages: Точные разделы и границы чтения приведены в тексте
  role: primary
level: advanced
created: '2026-11-03'
updated: '2026-11-03'
---

# Воспроизводимые примеры QR и Riemannion

Скрипт run_qr_riemannion.py и файл qr-riemannion-results.json находятся в этой папке. Текущий запуск выполнил **70 конечных проверок** и создал **семь SVG**. Использованы фиксированный seed 20261103, NumPy/SciPy и двойная точность; версии записаны в JSON. Дата SVG отключена, идентификаторы фиксированы.

    python 70_labs/computational-algebra-principles/run_qr_riemannion.py

Это собственные математические примеры. Код авторов Riemannion не исполнялся, обучение LLM и диффузионных моделей не запускалось, измерений времени и памяти нет. Независимая проверка математических утверждений выполняется отдельно от скрипта.

## QR: координаты и качество выбранного набора

Проверяются отражение Householder, QR-тождество, ортогональность ID-остатка и равенство его норм нормам хвоста. Формула обмена проверена независимо от её выражения через QR: отношение объёмов вычисляется как произведение сингулярных значений заменённых столбцов. На малом наборе полный перебор 20 троек столбцов находит глобальный максимальный объём и проверяет совместный сертификат с порогом 1.

У матрицы Кахана $c=0.8,s=0.6$, размеры от 4 до 24 с шагом 2, $k=n-1$. Сравниваются два разных объекта: исходный порядок, допустимый при точном равенстве всех активных норм, и фактическая перестановка SciPy/LAPACK. Последняя сохраняется в JSON; отсутствие обменов в библиотеке не предполагается.

![Исходный допустимый путь и фактическая перестановка библиотеки на матрице Кахана показаны отдельно](80_assets/computational-algebra-principles/qr-riemannion-plots-v1/cap-a04-kahan.svg)

<a href="80_assets/computational-algebra-principles/qr-riemannion-plots-v1/cap-a04-kahan.svg" target="_blank" rel="noopener" data-router-ignore>Открыть рисунок в полном размере</a>

> [!example]- Анимация (GIF)
>
> ![Жадные равенства могут скрывать плохой выбор](80_assets/course-gif-pca-v2/early/cap-a04-kahan.gif)
>
> В исходном порядке матрицы Кахана оставшиеся высоты на каждом шаге равны. Этот допустимый жадный путь даёт растущие ошибку и сертификат обмена; фактический выбор SciPy/LAPACK показан отдельно.
>
> [Открыть GIF в полном размере](80_assets/course-gif-pca-v2/early/cap-a04-kahan.gif)


Численный ранг иллюстрируется спектром $1,0.1,0.01,10^{-4},10^{-7}$, диагональным возмущением спектральной нормы $10^{-4}$, абсолютным порогом $10^{-3}$ и масштабированием на $10^{-3}$. Порог остаётся фиксированным, меняется классификация матрицы. Строгий знак больше исключает точное равенство порогу.

![Фиксированный абсолютный допуск меняет результат классификации при масштабировании данных](80_assets/computational-algebra-principles/qr-riemannion-plots-v1/cap-a04-rank-threshold-v2.svg)

<a href="80_assets/computational-algebra-principles/qr-riemannion-plots-v1/cap-a04-rank-threshold-v2.svg" target="_blank" rel="noopener" data-router-ignore>Открыть рисунок в полном размере</a>

> [!example]- Анимация (GIF)
>
> ![Масштаб меняет ранг при абсолютном пороге](80_assets/course-gif-pca-v2/early/cap-a04-rank-threshold-v2.gif)
>
> Уменьшение всех сингулярных чисел в одинаковое число раз меняет численный ранг при фиксированном пороге. Если порог пропорционален наибольшему сингулярному числу, ранг в этом примере сохраняется.
>
> [Открыть GIF в полном размере](80_assets/course-gif-pca-v2/early/cap-a04-rank-threshold-v2.gif)


Для ортогональности использована матрица $[\mathbf1^T;\delta I_5]$, где $\delta$ от $10^{-2}$ до $10^{-12}$. Реализации классического и модифицированного Грама–Шмидта однопроходные, без повторной ортогонализации. Householder QR берётся из NumPy. Вывод относится к этому примеру и точности вычислений, не к безусловной оценке всех реализаций.

![Потеря ортогональности при почти зависимых столбцах не является тестом качества выбора ранга](80_assets/computational-algebra-principles/qr-riemannion-plots-v1/cap-a04-orthogonality.svg)

<a href="80_assets/computational-algebra-principles/qr-riemannion-plots-v1/cap-a04-orthogonality.svg" target="_blank" rel="noopener" data-router-ignore>Открыть рисунок в полном размере</a>

> [!example]- Анимация (GIF)
>
> ![Почти зависимые столбцы испытывают QR](80_assets/course-gif-pca-v2/early/cap-a04-orthogonality.gif)
>
> Когда столбцы матрицы Лойхли сближаются, классический Грам–Шмидт теряет ортогональность. На тех же данных QR Хаусхолдера удерживает ошибку у уровня округления.
>
> [Открыть GIF в полном размере](80_assets/course-gif-pca-v2/early/cap-a04-orthogonality.gif)


## Спектральное выравнивание и повторная проекция

Берутся $X=E_{11}$ и $M=\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)$. Точные формулы дают $\|PO\|_2\approx1.145561$, хотя $\|O\|_2=1$. Проверяются некоммутативность операций и допустимость нормированного направления из приложения I.

В функции polar ненулевой спектр численно определяется условием $\sigma_j>10^{-12}\sigma_1$, а для нулевой матрицы берётся нулевая полярная матрица. Это явный **численный допуск**, не точный алгебраический ранг. Он отличается от буквального заполнения всех нулевых значений ядра в прочитанной ветке программы авторов. Соглашение сохранено и при вычислении малого ядра; другие допуски могут изменить результат возле границы ранга.

![В точном контрпримере повторная проекция увеличивает спектральную норму выше единицы](80_assets/computational-algebra-principles/qr-riemannion-plots-v1/cap-g02-polar-projection.svg)

<a href="80_assets/computational-algebra-principles/qr-riemannion-plots-v1/cap-g02-polar-projection.svg" target="_blank" rel="noopener" data-router-ignore>Открыть рисунок в полном размере</a>

> [!example]- Анимация (GIF)
>
> ![Повторная проекция может увеличить спектральную норму](80_assets/course-gif-pca-v2/early/cap-g02-polar-projection.gif)
>
> После полярного выравнивания оба сингулярных числа равны единице. Удаление нормальной клетки восстанавливает касательность, но увеличивает спектральную норму до примерно 1,146.
>
> [Открыть GIF в полном размере](80_assets/course-gif-pca-v2/early/cap-g02-polar-projection.gif)


## LOI: два блока градиента в одном касательном пространстве

Фиксирован $G=\operatorname{diag}(5,3,1,0.4,0.2)$, ранг адаптера 1. Перекрёстный $X_0=0.1e_1e_2^T$ даёт $P_{X_0}G=\operatorname{diag}(5,3,0,0,0)$ и норму $\sqrt{34}\approx5.83095$. Совпадающие ведущие направления $X_0=0.1e_1e_1^T$ захватывают только 5. На 100 фиксированных случайных парах максимум около 5.26175, ниже точного оптимума. Случайные пробы не доказывают глобальность — она доказана в [[30_mathematics/computational-algebra-principles/modules/cap-g02-riemannion|Г02]].

![Перекрёстная LOI-конструкция захватывает два ведущих блока; случайные подпространства служат лишь иллюстрацией](80_assets/computational-algebra-principles/qr-riemannion-plots-v1/cap-g02-loi-capture.svg)

<a href="80_assets/computational-algebra-principles/qr-riemannion-plots-v1/cap-g02-loi-capture.svg" target="_blank" rel="noopener" data-router-ignore>Открыть рисунок в полном размере</a>

> [!example]- Анимация (GIF)
>
> ![Перекрёстный адаптер захватывает энергию ранга 2](80_assets/course-gif-pca-v2/early/cap-g02-loi-capture.gif)
>
> При усилении второй сингулярной группы перекрёстная конструкция ранга 1 захватывает её вместе с первой. В показанном семействе квадрат нормы проекции совпадает с суммой квадратов двух ведущих сингулярных чисел.
>
> [Открыть GIF в полном размере](80_assets/course-gif-pca-v2/early/cap-g02-loi-capture.gif)


## Учебная матричная последовательность

Цель $F(X)=\tfrac12\|X-A\|_F^2$, $A=\operatorname{diag}(4,2,0.6,0.2)$, ранг 2, начальные факторы заданы seed. Используется согласованная геометрическая схема: касательный градиент → частичная полярная матрица → повторная проекция → SVD-ретракция. **Импульс и уменьшение весов отключены.** Длина шага дополнительно ограничивается разрывом ранга и обратным поиском Armijo. Это учебная модификация для контролируемого примера, а не буквальное воспроизведение Algorithm 5, ветки репозитория или протокола обучения статьи.

Для двух эквивалентных начальных факторизаций матричные последовательности за 36 итераций совпали с максимальным расхождением порядка $5.5\cdot10^{-15}$. Проверены сохранение ранга и монотонность цели в этом запуске. Это не универсальная теорема сходимости Riemannion и не сравнительный эксперимент с Adam.

![В контролируемой схеме без импульса эквивалентные факторы дают одну матричную траекторию](80_assets/computational-algebra-principles/qr-riemannion-plots-v1/cap-g02-toy-invariance.svg)

<a href="80_assets/computational-algebra-principles/qr-riemannion-plots-v1/cap-g02-toy-invariance.svg" target="_blank" rel="noopener" data-router-ignore>Открыть рисунок в полном размере</a>

> [!example]- Анимация (GIF)
>
> ![Разные факторы дают одну матричную траекторию](80_assets/course-gif-pca-v2/early/cap-g02-toy-invariance.gif)
>
> Две факторизации одной начальной матрицы приводят к совпадающим траекториям учебной матричной схемы. Шаг принимается по условию Армихо; импульс и уменьшение весов отключены.
>
> [Открыть GIF в полном размере](80_assets/course-gif-pca-v2/early/cap-g02-toy-invariance.gif)


## Градиентные произведения и малое ядро

Формулы двух вспомогательных производных проверяются центральными конечными разностями для нелинейной функции $F(W)=\tfrac12\|\sin(WZ)\|_F^2$, при $m=5,n=4,r=2$ и $h=10^{-6}$. Это независимая численная проверка цепного правила; она не выдаётся за запуск автоматического дифференцирования конкретного ML-фреймворка.

Для факторов $7\times4$ и $6\times4$ проверены совпадение ненулевого спектра произведения со спектром QR-ядра $4\times4$ и равенство результата усечения ядра плотной SVD.

![Малое QR-ядро сохраняет ненулевые сингулярные значения большого произведения](80_assets/computational-algebra-principles/qr-riemannion-plots-v1/cap-qr-small-core.svg)

<a href="80_assets/computational-algebra-principles/qr-riemannion-plots-v1/cap-qr-small-core.svg" target="_blank" rel="noopener" data-router-ignore>Открыть рисунок в полном размере</a>

> [!example]- Анимация (GIF)
>
> ![Смена базиса выделяет малое ядро](80_assets/course-gif-pca-v2/early/cap-qr-small-core.gif)
>
> QR-базисы собирают всё ненулевое действие произведения в блоке $4\times4$. После удаления нулевых строк и столбцов остаются те же четыре ненулевых сингулярных числа.
>
> [Открыть GIF в полном размере](80_assets/course-gif-pca-v2/early/cap-qr-small-core.gif)


**Самопроверка.** Почему нулевой шаг важен для проверки псевдокода ретракции? При $\eta=0$ он обязан вернуть текущий $X$; если формула возвращает ноль, в ней потерян исходный матричный член. Этот тест проверен отдельно для напечатанной блочной строки и согласованной формулы, но программа авторов не исполнялась.

Математика и условия: [[30_mathematics/computational-algebra-principles/modules/cap-a04-qr-numerical-rank|А04]], [[30_mathematics/computational-algebra-principles/modules/cap-g02-riemannion|Г02]], [[30_mathematics/computational-algebra-principles/theorems/cap-strong-rrqr|сильное RRQR]], [[30_mathematics/computational-algebra-principles/theorems/cap-spectral-lmo|спектральный оракул]], [[50_bridges/cap-qr-small-core|малое ядро]].
