# Описание 
# Установка

Python3 уже должен быть установлен у вас в системе и добавлен в переменные окружение
Также потребуеться установить зависимости способом ниже:

```bash
pip install -r requirments.txt
```
# Использование
Ниже я приведу инструкцию и примеры использования скрипта

## Переменные файла .env
Для работы скрипта, вам потребються соответсвенные для него настройки приведенные ниже:

APOD_EPIC_API - в этой переменной должен храниться ваш API ключ, который будет использован для скачивания картинок
TELEGRAM_API - такой же ключ API, но уже созданного вами бота, который будет отправлять картинки непосредственно в ваш канал
PUBLISH_FREQ - частота, с которой будут отправлятсья картинки в секундах
## Пример запуска скрипта скачивания картинок
Для того чтобы отправлять картинки нужно их для начала скачать. Примеры скачивания картинок через 3 разных сервиса приведенны ниже
### APOD
Пример запуска скрипта:
```bash
python fetch_apod_image.py --folder images 20
```
Флаг 'folder' отвечает за то, в какую папку будут скачаны картинки. 
Второй обязательный флаг 'count' отвечает за количество картинок скачивыемых в папку.
Приведенный пример скачает 20 картинок в папку images.
### EPIC
Пример запуска скрипта:
```bash
python fetch_epic_images.py --folder images
```
Флаг 'folder' отвечает за то, в какую папку будут скачаны картинки. 
Приведенный пример скачает несколько картинок в папку images.
### SPACEX
```bash
python fetch_spacex_last_launch.py --folder images
```
Флаг 'folder' отвечает за то, в какую папку будут скачаны картинки. 
Приведенный пример скачает несколько картинок в папку images.

## Пример запуска скрипта публикации
Пример запуска основного скрипта.
```bash
python main.py
```
После запуска вы должны будете ввести имя каталога из которого будут отправлены картинки и айди телеграм канала, в который бот будет отправлять картинки.