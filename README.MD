# Конвертер валют

Используются Flask и бесплатное апи от Apilayer (Fixer api)

## Установки

Установить зависимости из [requirements.txt](requirements.txt)

    pip install -r requirements.txt 

Для запуска использовать сам файл main.py, или же __flask --app main run__

## Использование

Для получения конвертации используется ссылка http://localhost:5000/api/rates?from=USD&to=RUB&value=1

Обязательно нужно указывать from= и to=

value= является необязательным и по автомату выставляется на 1.



