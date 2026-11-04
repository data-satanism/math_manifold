---
id: tva-source-map
title: "Видеокурс Тыртышникова: карта глав, источников и ограничений"
aliases: []
type: map
status: canonical
publish: true
areas: [numerical-analysis, tensor-methods]
concepts: [numerical-linear-algebra, tensor-decomposition, source-grounded-notes]
prerequisites: []
ai_domains: [compression, linear-regression, latent-variable-models]
source_refs:
  - id: tyrtyshnikov-video-algebra-2026
    pages: "Видеокурс 2026; отдельные записи и временные метки приведены в тексте"
    role: primary
level: advanced
created: 2026-10-28
updated: 2026-10-28
---

# Видеокурс Тыртышникова: карта глав, источников и ограничений

Карта построена по описаниям исходных видео и сохранённым расшифровкам. Главы автора служат единицами проверки; название главы само по себе не означает, что соответствующее утверждение доказано в записи. Сокращённые формулы субтитров сверяются с математикой и выбранными кадрами. Тексты дополнений составителя не выдаются за утраченные слова лектора.

Сейчас доступны десять видео, суммарно 13 ч 32 мин 37 с. Полнота источника различается: у восьмой расшифровки есть длинный пропуск; у остальных девяти проверка временных меток не обнаружила разрывов более 45 секунд. Короткие паузы не означают отсутствия речи и сами по себе не доказывают полноту распознавания.

## 01. Матричные разложения, QR-алгоритм

Маршрут: [[30_mathematics/tyrtyshnikov-video-2026/lectures/tva-01-matrix-factorizations-qr|подробный конспект]]. [Первичная запись](https://www.youtube.com/watch?v=_lsr5o9A2bw).

| Начало | Глава по описанию записи |
| --- | --- |
| [00:00:00](https://www.youtube.com/watch?v=_lsr5o9A2bw&t=0s) | Интро |
| [00:00:41](https://www.youtube.com/watch?v=_lsr5o9A2bw&t=41s) | Идея разделения переменных |
| [00:04:55](https://www.youtube.com/watch?v=_lsr5o9A2bw&t=295s) | Скелетное разложение матрицы |
| [00:14:55](https://www.youtube.com/watch?v=_lsr5o9A2bw&t=895s) | О матричных разложениях |
| [00:17:10](https://www.youtube.com/watch?v=_lsr5o9A2bw&t=1030s) | LU-разложение |
| [00:26:12](https://www.youtube.com/watch?v=_lsr5o9A2bw&t=1572s) | Упражнение на дом |
| [00:28:15](https://www.youtube.com/watch?v=_lsr5o9A2bw&t=1695s) | Решение СЛАУ при помощи LU |
| [00:32:30](https://www.youtube.com/watch?v=_lsr5o9A2bw&t=1950s) | PLU-разложение |
| [00:33:50](https://www.youtube.com/watch?v=_lsr5o9A2bw&t=2030s) | LPU-разложение Брюа |
| [00:35:12](https://www.youtube.com/watch?v=_lsr5o9A2bw&t=2112s) | QR-разложение |
| [00:38:00](https://www.youtube.com/watch?v=_lsr5o9A2bw&t=2280s) | Об ортогональных преобразованиях |
| [00:40:30](https://www.youtube.com/watch?v=_lsr5o9A2bw&t=2430s) | Решение СЛАУ при помощи QR-разложения |
| [00:41:20](https://www.youtube.com/watch?v=_lsr5o9A2bw&t=2480s) | Устойчивость численных методов |
| [00:46:00](https://www.youtube.com/watch?v=_lsr5o9A2bw&t=2760s) | Гипотеза Уилкинсона |
| [00:53:20](https://www.youtube.com/watch?v=_lsr5o9A2bw&t=3200s) | Проблема собственных значений |
| [00:54:20](https://www.youtube.com/watch?v=_lsr5o9A2bw&t=3260s) | Подход через характеристический многочлен |
| [01:03:30](https://www.youtube.com/watch?v=_lsr5o9A2bw&t=3810s) | QR-алгоритм |
| [01:13:15](https://www.youtube.com/watch?v=_lsr5o9A2bw&t=4395s) | Теорема о стремлении к треугольному виду (Уилкинсон) |

## 02. QR-алгоритм (продолжение). Быстрое преобразование Фурье

Маршрут: [[30_mathematics/tyrtyshnikov-video-2026/lectures/tva-02-qr-fft|подробный конспект]]. [Первичная запись](https://www.youtube.com/watch?v=WZOa90UaR8w).

| Начало | Глава по описанию записи |
| --- | --- |
| [00:00:00](https://www.youtube.com/watch?v=WZOa90UaR8w&t=0s) | Интро |
| [00:00:10](https://www.youtube.com/watch?v=WZOa90UaR8w&t=10s) | Вспоминание QR-алгоритма |
| [00:09:26](https://www.youtube.com/watch?v=WZOa90UaR8w&t=566s) | Цена одной итерации |
| [00:14:50](https://www.youtube.com/watch?v=WZOa90UaR8w&t=890s) | Замечание о QR-итерациях для трехдиагональной матрицы |
| [00:23:49](https://www.youtube.com/watch?v=WZOa90UaR8w&t=1429s) | Теплицевы и циркулянтные матрицы |
| [00:40:28](https://www.youtube.com/watch?v=WZOa90UaR8w&t=2428s) | Матрица Фурье |
| [00:45:02](https://www.youtube.com/watch?v=WZOa90UaR8w&t=2702s) | Лемма о свойствах матрицы Фурье |
| [00:49:20](https://www.youtube.com/watch?v=WZOa90UaR8w&t=2960s) | Основная спектральная теорема о циркулянтных матрицах |
| [00:58:25](https://www.youtube.com/watch?v=WZOa90UaR8w&t=3505s) | Быстрое преобразование Фурье ("разделяй и властвуй") |
| [01:15:23](https://www.youtube.com/watch?v=WZOa90UaR8w&t=4523s) | Итоги |

## 03. Матричные нормы. Сингулярное разложение

Маршрут: [[30_mathematics/tyrtyshnikov-video-2026/lectures/tva-03-norms-svd|подробный конспект]]. [Первичная запись](https://www.youtube.com/watch?v=Sz-qDhSdPxs).

| Начало | Глава по описанию записи |
| --- | --- |
| [00:00:00](https://www.youtube.com/watch?v=Sz-qDhSdPxs&t=0s) | Интро |
| [00:01:44](https://www.youtube.com/watch?v=Sz-qDhSdPxs&t=104s) | Определение нормы вектора и нормированного пространства |
| [00:07:40](https://www.youtube.com/watch?v=Sz-qDhSdPxs&t=460s) | Примеры векторных норм и эквивалентность норм в конечномерном пространстве |
| [00:12:19](https://www.youtube.com/watch?v=Sz-qDhSdPxs&t=739s) | Определение операторной нормы, подчинённой векторным нормам |
| [00:18:35](https://www.youtube.com/watch?v=Sz-qDhSdPxs&t=1115s) | Введение в сингулярное разложение матрицы |
| [00:24:05](https://www.youtube.com/watch?v=Sz-qDhSdPxs&t=1445s) | Доказательство существования сингулярного разложения |
| [00:38:40](https://www.youtube.com/watch?v=Sz-qDhSdPxs&t=2320s) | Сингулярное разложение |
| [00:55:03](https://www.youtube.com/watch?v=Sz-qDhSdPxs&t=3303s) | Связь сингулярного разложения с задачами приближения матриц |
| [01:00:07](https://www.youtube.com/watch?v=Sz-qDhSdPxs&t=3607s) | Малоранговые приближения: сжатие данных и борьба с шумом |
| [01:04:17](https://www.youtube.com/watch?v=Sz-qDhSdPxs&t=3857s) | Теорема о наилучшем малоранговом приближении |
| [01:06:36](https://www.youtube.com/watch?v=Sz-qDhSdPxs&t=3996s) | Поворот камеры, который вам нужен |
| [01:10:16](https://www.youtube.com/watch?v=Sz-qDhSdPxs&t=4216s) | Теорема Мирского и унитарно инвариантные нормы |
| [01:18:20](https://www.youtube.com/watch?v=Sz-qDhSdPxs&t=4700s) | Доказательство основной теоремы |

## 04. Сингулярное разложение (продолжение). Метод наименьших квадратов

Маршрут: [[30_mathematics/tyrtyshnikov-video-2026/lectures/tva-04-svd-least-squares|подробный конспект]]. [Первичная запись](https://www.youtube.com/watch?v=tmLdRA3eeb8).

| Начало | Глава по описанию записи |
| --- | --- |
| [00:00:00](https://www.youtube.com/watch?v=tmLdRA3eeb8&t=0s) | Интро |
| [00:00:05](https://www.youtube.com/watch?v=tmLdRA3eeb8&t=5s) | Теорема о наилучшем малоранговом приближении в спектральной норме и норме Фробениуса |
| [00:04:48](https://www.youtube.com/watch?v=tmLdRA3eeb8&t=288s) | Доказательство теоремы: использование унитарной инвариантности нормы Фробениуса |
| [00:14:11](https://www.youtube.com/watch?v=tmLdRA3eeb8&t=851s) | Напоминание свойств эрмитовых (самосопряженных) и нормальных матриц |
| [00:19:24](https://www.youtube.com/watch?v=tmLdRA3eeb8&t=1164s) | Три фундаментальные теоремы для эрмитовых матриц: закон инерции, теорема Куранта-Фишера и соотношения разделения |
| [00:23:18](https://www.youtube.com/watch?v=tmLdRA3eeb8&t=1398s) | Теорема о соотношениях разделения для собственных значений |
| [00:26:44](https://www.youtube.com/watch?v=tmLdRA3eeb8&t=1604s) | Доказательство соотношений разделения с помощью секулярного уравнения |
| [00:44:53](https://www.youtube.com/watch?v=tmLdRA3eeb8&t=2693s) | Завершение доказательства теоремы о малоранговом приближении с использованием соотношений разделения |
| [00:51:26](https://www.youtube.com/watch?v=tmLdRA3eeb8&t=3086s) | Метод наименьших квадратов: постановка задачи для несовместных систем |
| [00:52:31](https://www.youtube.com/watch?v=tmLdRA3eeb8&t=3151s) | Невязка и псевдорешение |
| [01:00:42](https://www.youtube.com/watch?v=tmLdRA3eeb8&t=3642s) | Утверждение: формула для вычисления нормального псевдорешения через сингулярное разложение |
| [01:04:19](https://www.youtube.com/watch?v=tmLdRA3eeb8&t=3859s) | Доказательство геометрических свойств нормального псевдорешения |
| [01:09:04](https://www.youtube.com/watch?v=tmLdRA3eeb8&t=4144s) | Проблема неустойчивости нормального псевдорешения: пример с малыми возмущениями |
| [01:13:05](https://www.youtube.com/watch?v=tmLdRA3eeb8&t=4385s) | Заключение: некорректность вычисления псевдорешения по приближенным данным |

## 05. Идея регуляризации

Маршрут: [[30_mathematics/tyrtyshnikov-video-2026/lectures/tva-05-regularization|подробный конспект]]. [Первичная запись](https://www.youtube.com/watch?v=eN352S8n0fs).

| Начало | Глава по описанию записи |
| --- | --- |
| [00:00:00](https://www.youtube.com/watch?v=eN352S8n0fs&t=0s) | Интро |
| [00:00:42](https://www.youtube.com/watch?v=eN352S8n0fs&t=42s) | Определение нормального псевдорешения |
| [00:04:34](https://www.youtube.com/watch?v=eN352S8n0fs&t=274s) | Определение регуляризованной системы |
| [00:09:46](https://www.youtube.com/watch?v=eN352S8n0fs&t=586s) | Теорема об оценке погрешности |
| [00:13:46](https://www.youtube.com/watch?v=eN352S8n0fs&t=826s) | Доказательство теоремы |
| [00:44:32](https://www.youtube.com/watch?v=eN352S8n0fs&t=2672s) | Важное замечание о методах регуляризации |
| [00:50:59](https://www.youtube.com/watch?v=eN352S8n0fs&t=3059s) | Новая тема о вычислении сингулярного разложения |
| [00:56:06](https://www.youtube.com/watch?v=eN352S8n0fs&t=3366s) | Замечание о бидиагональном виде матрицы |
| [01:14:28](https://www.youtube.com/watch?v=eN352S8n0fs&t=4468s) | Важное замечание о скорости сходимости |
| [01:20:24](https://www.youtube.com/watch?v=eN352S8n0fs&t=4824s) | Новая тема об аппроксимации матрицами малого ранга и крестовом методе |

## 06. Принцип максимального объёма. Крестовый метод

Маршрут: [[30_mathematics/tyrtyshnikov-video-2026/lectures/tva-06-maxvol-cross|подробный конспект]]. [Первичная запись](https://www.youtube.com/watch?v=usY6fqraVoM).

| Начало | Глава по описанию записи |
| --- | --- |
| [00:00:00](https://www.youtube.com/watch?v=usY6fqraVoM&t=0s) | Интро |
| [00:01:48](https://www.youtube.com/watch?v=usY6fqraVoM&t=108s) | Определение матрицы приближенного ранга r |
| [00:07:11](https://www.youtube.com/watch?v=usY6fqraVoM&t=431s) | Теорема о принципе максимального объема |
| [00:09:05](https://www.youtube.com/watch?v=usY6fqraVoM&t=545s) | Определение объема квадратной подматрицы |
| [00:14:32](https://www.youtube.com/watch?v=usY6fqraVoM&t=872s) | Важное замечание об оценке через наилучшее приближение |
| [00:15:58](https://www.youtube.com/watch?v=usY6fqraVoM&t=958s) | Доказательство теоремы о максимальном объеме |
| [00:26:41](https://www.youtube.com/watch?v=usY6fqraVoM&t=1601s) | Определение дополнения по Шуру |
| [00:43:19](https://www.youtube.com/watch?v=usY6fqraVoM&t=2599s) | Лемма о соотношениях разделения для сингулярных чисел |
| [00:45:33](https://www.youtube.com/watch?v=usY6fqraVoM&t=2733s) | Замечание о поиске оптимального креста |
| [00:55:18](https://www.youtube.com/watch?v=usY6fqraVoM&t=3318s) | Крестовый алгоритм малорангового приближения |
| [01:11:57](https://www.youtube.com/watch?v=usY6fqraVoM&t=4317s) | Принцип наибольшего объема для интерполяции |

## 07. Тензорные разложения

Маршрут: [[30_mathematics/tyrtyshnikov-video-2026/lectures/tva-07-tensor-rank-uniqueness|подробный конспект]]. [Первичная запись](https://www.youtube.com/watch?v=v8jWpXRENhs).

| Начало | Глава по описанию записи |
| --- | --- |
| [00:00:00](https://www.youtube.com/watch?v=v8jWpXRENhs&t=0s) | Интро |
| [00:03:39](https://www.youtube.com/watch?v=v8jWpXRENhs&t=219s) | Новая тема о тензорных разложениях многомерных матриц |
| [00:09:18](https://www.youtube.com/watch?v=v8jWpXRENhs&t=558s) | Умножение матриц |
| [00:26:52](https://www.youtube.com/watch?v=v8jWpXRENhs&t=1612s) | Определение тензорного ранга |
| [00:43:01](https://www.youtube.com/watch?v=v8jWpXRENhs&t=2581s) | Теорема о главном ранге комплексных тензоров |
| [00:45:48](https://www.youtube.com/watch?v=v8jWpXRENhs&t=2748s) | Теорема единственности тензорного разложения |
| [01:09:56](https://www.youtube.com/watch?v=v8jWpXRENhs&t=4196s) | Теорема Крускала об однозначности |
| [01:13:18](https://www.youtube.com/watch?v=v8jWpXRENhs&t=4398s) | Замечание о вещественном и комплексном случаях |

## 08. Теорема Крускала

Маршрут: [[30_mathematics/tyrtyshnikov-video-2026/lectures/tva-08-kruskal-proof|подробный конспект]]. [Первичная запись](https://www.youtube.com/watch?v=NA6cJBmO-tc).

| Начало | Глава по описанию записи |
| --- | --- |
| [00:00:00](https://www.youtube.com/watch?v=NA6cJBmO-tc&t=0s) | Интро |
| [00:00:05](https://www.youtube.com/watch?v=NA6cJBmO-tc&t=5s) | Теорема Крускала об однозначности канонического разложения |
| [00:09:17](https://www.youtube.com/watch?v=NA6cJBmO-tc&t=557s) | Лемма о ранге специального произведения |
| [00:24:29](https://www.youtube.com/watch?v=NA6cJBmO-tc&t=1469s) | Лемма о неравенстве Сильвестра |
| [00:31:27](https://www.youtube.com/watch?v=NA6cJBmO-tc&t=1887s) | Замечание о ранге подматриц и коранге |
| [00:51:00](https://www.youtube.com/watch?v=NA6cJBmO-tc&t=3060s) | Ключевая лемма Крускала |
| [01:11:11](https://www.youtube.com/watch?v=NA6cJBmO-tc&t=4271s) | Финальный шаг доказательства |
| [01:20:39](https://www.youtube.com/watch?v=NA6cJBmO-tc&t=4839s) | Важное замечание о точном тензорном ранге разложения |

**Ограничение:** глава о рангах/кранге пересекается с пропуском 32:55–49:07. Нормализованный математический переход — дополнение составителя. Авторские слова здесь не восстановлены.

## 09. Разложение Таккера. Тензорный поезд

Маршрут: [[30_mathematics/tyrtyshnikov-video-2026/lectures/tva-09-tucker-tt|подробный конспект]]. [Первичная запись](https://www.youtube.com/watch?v=d3qAGpH-pmA).

| Начало | Глава по описанию записи |
| --- | --- |
| [00:00:00](https://www.youtube.com/watch?v=d3qAGpH-pmA&t=0s) | Интро |
| [00:03:12](https://www.youtube.com/watch?v=d3qAGpH-pmA&t=192s) | Определение разложения Таккера |
| [00:05:34](https://www.youtube.com/watch?v=d3qAGpH-pmA&t=334s) | Важное замечание о проклятии размерности в разложении Таккера |
| [00:07:56](https://www.youtube.com/watch?v=d3qAGpH-pmA&t=476s) | Определение минимального разложения Таккера |
| [00:12:44](https://www.youtube.com/watch?v=d3qAGpH-pmA&t=764s) | Новая тема о матрицах развертки тензора |
| [00:23:52](https://www.youtube.com/watch?v=d3qAGpH-pmA&t=1432s) | Теорема о рангах минимального разложения Таккера |
| [00:30:06](https://www.youtube.com/watch?v=d3qAGpH-pmA&t=1806s) | Важное замечание об ортогональном выборе опорных матриц |
| [00:44:31](https://www.youtube.com/watch?v=d3qAGpH-pmA&t=2671s) | Определение ортогонального разложения Таккера |
| [00:46:02](https://www.youtube.com/watch?v=d3qAGpH-pmA&t=2762s) | Определение сингулярного разложения Таккера |
| [00:46:38](https://www.youtube.com/watch?v=d3qAGpH-pmA&t=2798s) | Теорема об оценке погрешности приближенного разложения Таккера |
| [00:56:03](https://www.youtube.com/watch?v=d3qAGpH-pmA&t=3363s) | Важное замечание о вычислительных преимуществах разложения Таккера |
| [00:57:53](https://www.youtube.com/watch?v=d3qAGpH-pmA&t=3473s) | Новая глава о разложении в тензорный поезд |
| [01:06:35](https://www.youtube.com/watch?v=d3qAGpH-pmA&t=3995s) | Важное замечание о сжатии тензора и исчезновении проклятия размерности |

## 10. Построение тензорного поезда

Маршрут: [[30_mathematics/tyrtyshnikov-video-2026/lectures/tva-10-tt-construction-rounding|подробный конспект]]. [Первичная запись](https://www.youtube.com/watch?v=MhhdhLFYIwc).

| Начало | Глава по описанию записи |
| --- | --- |
| [00:00:00](https://www.youtube.com/watch?v=MhhdhLFYIwc&t=0s) | Интро |
| [00:11:15](https://www.youtube.com/watch?v=MhhdhLFYIwc&t=675s) | Новая тема об алгоритме построения тензорного поезда |
| [00:27:02](https://www.youtube.com/watch?v=MhhdhLFYIwc&t=1622s) | Новая тема о редуцировании рангов в тензорном поезде |
| [00:36:07](https://www.youtube.com/watch?v=MhhdhLFYIwc&t=2167s) | Определение ортогонального тензорного вагона |
| [00:39:24](https://www.youtube.com/watch?v=MhhdhLFYIwc&t=2364s) | Лемма о произведении ортогональных вагонов |
| [00:46:48](https://www.youtube.com/watch?v=MhhdhLFYIwc&t=2808s) | Теорема о представлении тензорного поезда |

## Различать изложение и математическое дополнение

Курс не везде содержит полное доказательство: общий главный ранг комплексных тензоров вынесен за его пределы; отдельные шаги Крускала оставлены упражнениями; TT-cross в последней лекции дан как идея с оговоркой о теории. Эти границы сохранены. Самостоятельные раскрытия упражнений помечены, независимая проверка подтверждает математику раскрытия, а не факт произнесения этих строк в лекции.

Алгебраические вейвлеты упомянуты как неуспевшая тема. Они не считаются изложенными и не получают вымышленного одиннадцатого конспекта.
