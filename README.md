# Инструменты по индексации в ПС

Этот репозиторий содержит коллекцию инструментов для индексации в поисковых системах.

Специально для tg канала: [seo_code](https://t.me/seo_code)

## Инструменты

### Google Indexing API

Модуль [google_indexing_api](google_indexing_api) представляет инструмент для отправки страниц на индексацию с помощью
Google Indexing API.

Т.к. в Indexing API есть суточный лимит на отправку запросов, то **в скрипте реализована ротация аккаунтов**.
Как только в конкретном аккаунте заканчиваются лимиты - происходит его замена и скрипт продолжает отправку.

NOTE: Пока что отправка запросов реализована последовательно и это занимает определенное время.
У Indexing API есть поддержка batch запросов, что позволит отправлять запросы пачкой.
Но скрипт пока так делать не умеет.

#### Как пользоваться?

В папку [credits](google_indexing_api%2Fcredits) кладем креды от аккаунтов. Где их взять?

1. Перейдите [https://console.cloud.google.com/](https://console.cloud.google.com/) -> APIs & Services -> Credentials.
   Если у вас еще нет проектов - создайте его.
2. Нажмите "Create Credentials" -> "OAuth client ID" (**Application type = Desktop app**) и нажмите "Create".
3. Скачайте JSON файл и положите его в папку [credits](google_indexing_api%2Fcredits)
4. На странице APIs & Services -> перейдите в Library и активируйте сервис "Indexing API".

NOTE: все созданные аккаунты должны быть добавлены в Search Console, доступ должен быть ко всем доменам, с которыми вы
планируете работать. Права у аккаунтов - Owner.

Далее, положите все свои урлы, которые вы хотите проиндексировать, в файл urls.txt. И запустите скрипт:

```shell
cd google_indexing_api
```

```shell
poetry run python api.py
```

### Yandex IndexNow

Модуль `ya_index_now` предоставляет инструмент для индексации страниц с использованием Yandex IndexNow.

По ссылкам ниже описано, что нужно сделать для начала работы.

Документация:

- общая документация [IndexNow](https://yandex.ru/support/webmaster/indexing-options/index-now.html)
- [как сгенерировать ключ](https://yandex.ru/support/webmaster/indexnow/key.html)

### parse_sitemap.py

Скрипт `parse_sitemap.py` парсит URL-адреса из карты сайта (sitemap) и сохраняет их в файле `sitemap_urls.txt`.

### Ping Google Sitemap.xml

Скрипт [ping.py](google_ping_sitemaps%2Fping.py) пингует указанные сайтмапы в гугле.
Тесты показали, что пинг пока все еще работает, боты приходят.

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