## Как запустить сервис

***
- Обязательно ставим Python 3.11
- Идем в папку `./backend`
- Создаем окружение
   ```shell
   $ python -m venv envname
   $ virtualenv envname
   $ source envname/bin/activate
   (envname) $
   ```
- Cтавим зависимости
   ```shell
   pip install -r requirements.txt
   ```
- Подкидываем переменные окружения для бд, либо используем дефолтные значения из конфига
- Накатываем миграции
  ```shell
  alembic upgrade heads
  ```
- В случае возникновения ошибки связанной с `uuid_generate_v4()`в консоли бд выполняем команду:
  ```psql
  CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
  ```
- Запускаем `main.py`
- Идём в папку `./frontend` и запускаем `npm i`
- Когда всё необходимое поставилось запускаем `npm run start`
- Готово
