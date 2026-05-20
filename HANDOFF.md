# FastAPI Template Handoff

## Overview

This is a clean reusable FastAPI backend template using:

- FastAPI
- Pydantic v2
- pydantic-settings
- Uvicorn
- Simple JSON-file storage for local example CRUD features

The template intentionally does not include a real database or authentication by default.

Add database/auth only when a task explicitly requires it.

## Current Status

The app is clean when this command passes:

python -c "from main import app; print(app.title)"

Expected output:

FastAPI Template

## File Structure

main.py
config.py
requirements.txt
core/
  storage.py
  utils.py
middleware/
  cors.py
models/
  base.py
routers/
  health.py
schemas/
  base.py

## Current Routes

GET /
GET /health/

Docs:

/docs
/redoc

## Important Rules

- Do not commit .env files.
- Do not commit __pycache__ files.
- Keep shared template files simple.
- Do not add auth, database, payments, or external services unless requested.
- Register new routers in main.py.
- Keep one router file per feature.
- Keep schemas in schemas/.
- Keep route logic in routers/.
- Use response_model where practical.

## Settings

Settings are loaded from config.py using pydantic-settings.

Supported environment variables:

APP_NAME
APP_VERSION
DEBUG
HOST
PORT

Use .env.example as the reference.

## JSON Storage Mode

The current template uses JSON-file storage helpers in core/storage.py.

Available helpers:

load_db()
save_db()
generate_id()

This is only for local examples and simple generated CRUD.

Do not treat db.json as production storage.

If a task asks for a real database, add a proper database layer intentionally.

## Utility Helpers

core/utils.py provides:

now_iso()
not_found(resource, id)

Use them when they fit the feature.

## Adding a Simple CRUD Feature

For a feature named books:

Create:

schemas/books.py
routers/books.py

Edit:

main.py

In schemas/books.py:

- define BookCreate
- define Book response schema

In routers/books.py:

- define router = APIRouter(prefix="/books", tags=["books"])
- implement GET /
- implement POST /
- implement GET /{book_id}
- implement PUT /{book_id}
- implement DELETE /{book_id}

In main.py:

from routers import books
app.include_router(books.router)

## Validation

After changes, run:

python -c "from main import app; print(app.title)"
python -c "from main import app; print([route.path for route in app.routes])"

Before handoff:

- app imports successfully
- routes are registered
- no .env file is tracked
- no __pycache__ files are tracked
- git status is clean
