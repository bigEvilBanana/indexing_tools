# Инструменты по индексации в ПС

Этот репозиторий содержит коллекцию инструментов для индексации в поисковых системах.

Специально для tg канала: [seo_code](https://t.me/seo_code)

## Инструменты

### Yandex IndexNow

Модуль `ya_index_now` предоставляет инструмент для индексации страниц с использованием Yandex IndexNow.

По ссылкам ниже описано, что нужно сделать для начала работы.

Документация:

- общая документация [IndexNow](https://yandex.ru/support/webmaster/indexing-options/index-now.html)
- [как сгенерировать ключ](https://yandex.ru/support/webmaster/indexnow/key.html)

### parse_sitemap.py

Скрипт `parse_sitemap.py` парсит URL-адреса из карты сайта (sitemap) и сохраняет их в файле `sitemap_urls.txt`.

## Как установить

1. Убедитесь, что у вас установлена версия Python 3.10. Вы можете проверить версию Python с помощью команды:

```shell
python --version
```

2. Скачайте и установите Poetry, инструмент для управления зависимостями и виртуальным окружением Python:

```shell
curl -sSL https://install.python-poetry.org | python3 -
```

3. Установите зависимости с помощью Poetry:

```shell
poetry install
```

4. Теперь вы можете запустить скрипты. Например:

```shell
poetry run python parse_sitemap.py
```

```shell
poetry run python ya_index_now/index_now.py
```