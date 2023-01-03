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
        # Если у пользователя другие UID/GID,
        # то нужно исправить эти значения на соответствующие:
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

После этого можно собирать и запускать:
```
docker-compose up -d
```
