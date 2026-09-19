# Домашня робота №8

REST API для зберігання та керування контактами, створений за допомогою FastAPI, SQLAlchemy, PostgreSQL і Pydantic.

## Можливості

- створення, отримання, оновлення та видалення контактів;
- пошук за ім'ям, прізвищем або електронною адресою;
- отримання контактів із днями народження протягом найближчих семи днів;
- автоматична документація Swagger.

## Встановлення

Підготовка віртуального середовища та встановлення залежностей:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Підключення до PostgreSQL задається змінною середовища `DATABASE_URL`:

```powershell
$env:DATABASE_URL = "postgresql+psycopg2://<user>:<password>@<host>:<port>/<database>"
```

## Запуск

```powershell
uvicorn main:app --reload
```

## Основні маршрути

- `POST /contacts/` — створити контакт;
- `GET /contacts/` — отримати список контактів або виконати пошук;
- `GET /contacts/upcoming-birthdays` — отримати найближчі дні народження;
- `GET /contacts/{contact_id}` — отримати контакт за ідентифікатором;
- `PUT /contacts/{contact_id}` — оновити контакт;
- `DELETE /contacts/{contact_id}` — видалити контакт.
