# FastAPI Template

Clean backend starter template using:

- FastAPI
- Pydantic v2
- pydantic-settings
- Uvicorn
- Simple JSON-file storage for example CRUD features

This template is designed to be easy for humans and AI coding agents to extend.

## Purpose

Use this repository as a small FastAPI starting point for APIs, CRUD modules, and backend experiments.

The template intentionally does not include a real database or authentication by default.

Add database/auth only when the task explicitly requires it.

## Getting Started

Create a virtual environment:

python -m venv .venv

Activate it on Windows PowerShell:

.venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

Run the app:

uvicorn main:app --reload

Open docs:

http://127.0.0.1:8000/docs

Health check:

http://127.0.0.1:8000/health/

## Environment Variables

Create a local .env file based on .env.example.

Do not commit .env.

Available variables:

APP_NAME=FastAPI Template
APP_VERSION=1.0.0
DEBUG=True
HOST=0.0.0.0
PORT=8000

## Project Structure

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

## Current Storage Mode

This template currently uses simple JSON-file storage through core/storage.py.

This is useful for:

- small generated CRUD examples
- local testing
- AI-agent workflow validation
- backend scaffolding

It is not intended for production data.

For real applications, add a proper database layer only when requested.

## Validation

Check Python syntax:

python -m compileall main.py config.py core middleware models routers schemas

Check app import:

python -c "from main import app; print(app.title)"

Run server:

uvicorn main:app --reload

## Agent Rules

Before finishing a task:

- App must import successfully.
- New routers must be registered.
- New endpoints must appear in /docs.
- Do not commit .env.
- Do not commit __pycache__.
- Keep feature code simple and consistent.

