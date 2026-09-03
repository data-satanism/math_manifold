---
id: slt-source-map
title: "Карта источников: Статистическое обучение и теория информации"
aliases: ["Source map slt"]
type: source
status: canonical
publish: true
areas: [statistical-learning, information-theory, source-mapping]
concepts: [source-coverage, content-overlap]
prerequisites: [slt-course-map]
ai_domains: [statistical-learning, representation-learning, model-compression]
source_refs:
  - id: shashua-ml-notes-2009
    pages: "PDF 1–109"
    role: primary
  - id: stanford-ee376a-information-theory
    pages: "PDF 1–75"
    role: primary
level: research
created: 2026-08-12
updated: 2026-09-03
---

# Карта источников: Статистическое обучение и теория информации

| № | Источник и страницы | Целевой модуль | Статус |
|---:|---|---|---|
| 1 | shashua-ml-notes-2009, PDF 73–84 | [[30_mathematics/statistical-learning-information-theory/modules/slt-01-risk-erm-pac|Риск, эмпирический риск и PAC-постановка]] | canonical |
| 2 | shashua-ml-notes-2009, PDF 73–84 | [[30_mathematics/statistical-learning-information-theory/modules/slt-02-concentration-finite-classes|Концентрация и конечные классы гипотез]] | canonical |
| 3 | shashua-ml-notes-2009, PDF 84–93 | [[30_mathematics/statistical-learning-information-theory/modules/slt-03-vc-dimension-sauer|VC-размерность и лемма Зауэра—Шелаха]] | canonical |
| 4 | shashua-ml-notes-2009, PDF 93–100 | [[30_mathematics/statistical-learning-information-theory/modules/slt-04-symmetrization-double-sampling|Симметризация и метод двойной выборки]] | canonical |
| 5 | shashua-ml-notes-2009, PDF 16–22; stanford-ee376a-information-theory, PDF 9–15 | [[30_mathematics/statistical-learning-information-theory/modules/slt-05-relative-entropy-maxent|Относительная энтропия, максимальная энтропия и двойственность]] | canonical |
| 6 | stanford-ee376a-information-theory, PDF 9–15 | [[30_mathematics/statistical-learning-information-theory/modules/slt-06-entropy-mutual-information|Энтропия и взаимная информация]] | canonical |
| 7 | stanford-ee376a-information-theory, PDF 15–45 | [[30_mathematics/statistical-learning-information-theory/modules/slt-07-coding-channel-capacity|Кодирование, типичные последовательности и пропускная способность]] | canonical |
| 8 | stanford-ee376a-information-theory, PDF 62–73; shashua-ml-notes-2009, PDF 73–100 | [[30_mathematics/statistical-learning-information-theory/modules/slt-08-rate-distortion-generalization|Функция скорость–искажение и информационный взгляд на обобщение]] | canonical |

## Полное покрытие подразделов

| Источник | Глава и все входящие подразделы | Страницы | Решение или целевые модули |
|---|---|---:|---|
| shashua-ml-notes-2009 | 1. Байесовская теория решений: ограничения независимости, бросок монеты, гауссово оценивание, последовательное байесовское обновление, два нормальных класса | PDF 5–15 | reference-only |
| shashua-ml-notes-2009 | 2. Двойственность максимального правдоподобия и максимальной энтропии: эмпирическое распределение, относительная энтропия, MaxEnt | PDF 16–22 | slt-05-relative-entropy-maxent |
| shashua-ml-notes-2009 | 3. EM: общий алгоритм, независимые одинаково распределённые наблюдения, модель монет, смесь нормальных распределений, приложения | PDF 23–33 | reference-only |
| shashua-ml-notes-2009 | 4. SVM и ядра: квадратичная задача для зазора, SVM, ядерный трюк, полиномиальные ядра и ядра RBF, вывод | PDF 34–44 | reference-only |
| shashua-ml-notes-2009 | 5–6. Спектральный анализ: PCA, LDA, CCA и кластеризация | PDF 45–72 | reference-only |
| shashua-ml-notes-2009 | 7. Формальная PAC-модель | PDF 73–83 | slt-01-risk-erm-pac;slt-02-concentration-finite-classes |
| shashua-ml-notes-2009 | 8. VC-размерность | PDF 84–92 | slt-03-vc-dimension-sauer |
| shashua-ml-notes-2009 | 9. Теорема двойной выборки | PDF 93–100 | slt-04-symmetrization-double-sampling |
| shashua-ml-notes-2009 | Приложения и библиография | PDF 101–109 | reference-only |
| stanford-ee376a-information-theory | Введение: сжатие без потерь, канальное кодирование и сжатие с потерями | PDF 4–8 | slt-07-coding-channel-capacity |
| stanford-ee376a-information-theory | Энтропия, условная и совместная энтропия, относительная энтропия и взаимная информация | PDF 9–15 | slt-06-entropy-mutual-information |
| stanford-ee376a-information-theory | Свойство асимптотической равновероятности и сжатие фиксированной длины с исчезающей вероятностью потери | PDF 15–21 | slt-07-coding-channel-capacity |
| stanford-ee376a-information-theory | Сжатие без потерь: однозначно декодируемые и префиксные коды, коды Шеннона и Хаффмана, границы длины | PDF 21–31 | slt-07-coding-channel-capacity |
| stanford-ee376a-information-theory | Передача и пропускная способность: дискретные и непрерывные каналы, AWGN, совместная типичность, прямая и обратная теоремы, неравенство Фано | PDF 31–48 | slt-07-coding-channel-capacity |
| stanford-ee376a-information-theory | Метод типов и теорема Санова | PDF 48–55 | slt-08-rate-distortion-generalization |
| stanford-ee376a-information-theory | Условная и совместная типичность, лемма о совместной типичности | PDF 55–62 | slt-07-coding-channel-capacity |
| stanford-ee376a-information-theory | Сжатие с потерями и функция скорость—искажение: определения, примеры, прямая и обратная теоремы, геометрия | PDF 62–71 | slt-08-rate-distortion-generalization |
| stanford-ee376a-information-theory | Совместное кодирование источника и канала, теорема разделения | PDF 71–75 | slt-08-rate-distortion-generalization |

## Правило покрытия

Каждый указанный диапазон проверяется в исходном PDF. Если соседние подразделы объединены, их границы остаются видимыми в этой таблице и в `source_refs` модуля. Совпадающее содержание расширяет существующий узел или получает ссылку `reference-only`; отдельное определение-дубликат не создаётся.
