# Project Radar API

Backend-сервис для управления пользователями, проектами, задачами и тегами.
Проект написан на FastAPI, использует PostgreSQL, SQLAlchemy, Alembic,
Pydantic и запускается через Docker Compose.

## Что умеет сервис

- пользователи: `Create`, `Read`, `Update`, `Delete`;
- проекты: `Create`, `Read`, `Update`, `Delete`;
- задачи: `Create`, `Read`, `Update`, `Delete`;
- назначение задач пользователям;
- теги для задач;
- краткий анализ текста задачи;
- понятные ошибки с корректными HTTP-статусами.

## Стек

- Python 3.11+
- FastAPI
- Pydantic 2
- SQLAlchemy 2
- Alembic
- PostgreSQL 15
- Pytest
- Docker Compose

## Быстрый запуск через Docker

Перед запуском убедитесь, что Docker запущен.

```bash
docker compose up -d --build
```

После запуска откройте:

- Swagger: http://localhost:8000/docs
- Проверка состояния: http://localhost:8000/api/v1/health

Остановить проект:

```bash
docker compose down
```

## Локальный запуск без Docker

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
set DATABASE_URL=sqlite+pysqlite:///./dev.db
python -m alembic upgrade head
uvicorn app.main:app --reload
```

Для PowerShell переменная окружения задается так:

```powershell
$env:DATABASE_URL="sqlite+pysqlite:///./dev.db"
```

## Проверки

```bash
python -m pytest --cov=app --cov-report=term-missing
python -m flake8 app tests --max-line-length=100
python -m mypy app --ignore-missing-imports
```

Тесты покрывают API, сервисы, DTO и работу с базой. Покрытие кода выше 90%.

## Основные эндпоинты

- `GET /api/v1/health`
- `POST /api/v1/users`
- `GET /api/v1/users`
- `POST /api/v1/projects`
- `GET /api/v1/projects`
- `POST /api/v1/tasks`
- `GET /api/v1/tasks`
- `POST /api/v1/analysis/analyze`
- `POST /api/v1/tasks/{task_id}/summary`

## Структура

```text
app/
  controllers/     HTTP-эндпоинты
  dto/             Pydantic DTO для запросов и ответов
  repositories/    работа с базой данных
  services/        бизнес-логика
  database/        подключение к базе и общий Base
  models.py        SQLAlchemy-модели
  config.py        настройки приложения
  security.py      хеширование паролей
  text_analysis/   анализ текста задачи
  utils/           ошибки, валидаторы, rate limit
tests/
  unit/            тесты DTO и сервисов
  integration/     тесты API и базы данных
alembic/
  versions/        миграции базы данных
```

Логика разделена по слоям:

- `controllers` принимают HTTP-запросы;
- `dto` описывают входные и выходные данные;
- `services` выполняют бизнес-логику;
- `repositories` работают с таблицами;
- `models.py` хранит структуру базы данных.
