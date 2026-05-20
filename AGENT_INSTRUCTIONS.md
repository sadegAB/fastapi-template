# Agent Instructions

You are working inside a reusable FastAPI backend template.

Read this file before editing the project.

## Core Rules

- Keep the template clean, simple, and reusable.
- Do not add production-specific business logic to shared template files.
- Do not add a database, authentication, payments, or external services unless the task explicitly requires them.
- Do not commit .env files.
- Do not commit __pycache__ files.
- Do not install new packages unless the task explicitly requires them.
- Keep code readable and typed where practical.
- The app must import successfully before the task is complete.

## Current Architecture

This template currently uses:

- FastAPI app in main.py
- Settings in config.py
- CORS setup in middleware/cors.py
- Routers in routers/
- Schemas in schemas/
- Simple JSON storage helpers in core/storage.py
- Utility helpers in core/utils.py

## Router Rules

- Create one router file per feature.
- Each router file must define a variable named router.
- Use APIRouter.
- Register new routers in main.py with app.include_router().
- Use response_model where practical.
- Keep endpoint paths simple and REST-like.

Example feature routes:

- GET /items/
- POST /items/
- GET /items/{item_id}
- PUT /items/{item_id}
- DELETE /items/{item_id}

## Schema Rules

- Put request and response schemas in schemas/{feature}.py.
- Use Pydantic BaseModel.
- Use Create schemas for request bodies.
- Use response schemas for returned objects.
- Do not mix route logic into schemas.

## Storage Rules

The current default storage mode is JSON-file storage.

Use core/storage.py helpers for simple CRUD examples:

- load_db()
- save_db()
- generate_id()

Use core/utils.py helpers when useful:

- now_iso()
- not_found()

Do not treat JSON storage as production data storage.

If the task asks for a real database, add a proper database layer intentionally instead of forcing JSON storage.

## Validation Checklist

Before finishing:

- python -c "from main import app; print(app.title)" passes.
- New router imports work.
- New routes appear in FastAPI docs.
- No .env file is tracked.
- No __pycache__ files are tracked.
- No unrelated files are changed.
