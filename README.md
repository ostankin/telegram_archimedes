Простенький Телеграм-робот, который мониторит личку, и когда кто-то пишет "ахахах", шлёт в ответ вот такую картинку с Архимедом:

![Архимед](archimedes.jpg?raw=true)

Для соединения робот ожидает стандартных трёх параметров:

* `API_ID` - переменная окружения или строчка в файле `.env`
* `API_HASH` - переменная окружения или строчка в файле `.env`
* `session_name` - имя сессии. Предполагается существование файла `<session_name>.session`. Задаётся через конфигурационный файл [config.yaml](config.yaml), по умолчанию имя сессии "archimedes".

Инструкцию по получению `API_ID` и `API_HASH`, а также генерированию файла сессии можно найти, например, [здесь](https://habr.com/ru/sandbox/169203/).

Можно запустить из-под `docker-compose`. Для этого создайте файл `docker-compose.yml` следующего содержания:
```yaml
version: "3.4"

services:
  archimedes:
    build:
      context: https://github.com/ostankin/telegram_archimedes.git
      args:
        # Если у пользователя, имеющего доступ на запись к файлу с сессией,
        # другие UID/GID, то нужно исправить эти значения на соответствующие:
        UID: "1000"
        GID: "1000"
    environment:
      - API_ID
      - API_HASH
    volumes:
      - "./archimedes.session:/app/archimedes.session"
    restart: unless-stopped
```

Не забудьте также создать файл `.env` (значения, естественно, другие):
```shell
API_ID=12345678
API_HASH="1af822b2a9055ad52d76c18afbd05ae824d332b6"
```

Если для работы Телеграм требуется прокси, добавьте в `.env` следующие строки:

```shell
PROXY_TYPE='socks5'
PROXY_ADDR='1.2.3.4'
PROXY_PORT=1234
PROXY_USERNAME='jane.doe'  # необязательно
PROXY_PASSWORD='secret'  # необязательно
PROXY_RDNS=true  # необязательно
```

Подробности см. в
[документации к объекту TelegramClient](https://docs.telethon.dev/en/stable/basic/signing-in.html#signing-in-behind-a-proxy).

**Важно:** все перечисленные в файле `.env` переменные нужно продублировать в секции `environment`
файла `docker-compose.yml` (уже без значений, только имена переменных):

```yaml
    environment:
      - API_ID
      - API_HASH
      - PROXY_TYPE
      - PROXY_ADDR
      # и так далее
```

После этого можно собирать и запускать:
```
docker-compose up -d
```
