Простенький Телеграм-робот, который отсылает в ответ на "ахахах" вот такую картинку с Архимедом:
![Архимед](archimedes.jpg?raw=true)

Для соединения робот ожидает стандартных трёх параметров:

* `API_ID` - переменная окружения или строчка в файле `.env`
* `API_HASH` - переменная окружения или строчка в файле `.env`
* `session_name` - имя сессии. Предполагается существование файла `<session_name>.session`. Задаётся через конфигурационный файл [config.yaml](config.yaml), по умолчанию имя сессии "archimedes".

Инструкцию по получению `API_ID` и `API_HASH`, а также генерированию файла сессии можно найти, например, [здесь](https://habr.com/ru/sandbox/169203/).
