# Math Manifold

Русскоязычная связанная база знаний по математике для искусственного
интеллекта и машинного обучения.

Сайт построен на Quartz 5. Публичное дерево создаётся однонаправленным
экспортом из authoring-vault `MathAI_Knowledge`: в репозиторий попадают только
заметки со статусом `canonical` и признаком `publish: true`, а также реально
используемые иллюстрации и интерактивы.

## Проверка и сборка

```bash
python scripts/verify_production.py content content-manifest.json
npm ci
npx quartz plugin install --from-config
npx quartz build
python scripts/check_built_links.py public --base-path math_manifold
```

Ветка `v5` автоматически собирается и публикуется через GitHub Pages.

## Лицензирование

Код Quartz распространяется по лицензии MIT. Авторские учебные материалы и
иллюстрации принадлежат владельцу репозитория; сторонние PDF, OCR и исходные
книги в репозитории отсутствуют.
