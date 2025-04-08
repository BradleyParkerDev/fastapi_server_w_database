# FastAPI Server with Database, Cron, and Logging

A production-ready FastAPI boilerplate that integrates scheduled cron jobs, SQLAlchemy with Alembic for database management, and robust logging utilities. Designed to be scalable, modular, and extendable across any web application or API-driven project.

---

## Overview

This server is a clean foundation for building robust FastAPI applications. It is ideal for developers looking to:
- Run periodic background jobs (e.g., cleanup tasks, data syncs).
- Build authenticated web applications or APIs.
- Use PostgreSQL with SQLAlchemy and Alembic.
- Maintain modular code with clean architecture.

---

## Features

- **FastAPI Framework** — Async, high-performance web framework.
- **Session-Based Auth** — On initial server hit, a guest session, token, and cookie are generated automatically.
- **Cron Integration** — APScheduler with runtime start/stop control.
- **SQLAlchemy ORM** — PostgreSQL-backed database models.
- **Alembic Migrations** — Version-controlled schema updates.
- **Logging** — Custom logger setup for debugging and production insights.
- **Modular App Structure** — Easily scale logic across controllers, routes, and utilities.
- **Middleware Stack** — GZip, CORS, No-Cache, Authorization.
- **Arel Hot Reload** — Auto-refresh on changes to `resources/` or `public/`.

---

## Project Structure

```
fastapi_server_w_database_cron_and_logging/
├── app/
│   ├── controllers/        # Route logic & page behavior
│   ├── database/           # SQLAlchemy models, DB engine, Alembic config
│   ├── lib/                # Core utilities: auth, cron, logger, layout
│   ├── routes/             # API and web route definitions
│   └── __init__.py
├── public/                # Static files (JS, CSS, images, etc.)
├── resources/             # Template files or other reloadable assets
├── main.py                # Server entry point
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
├── alembic.ini            # Alembic DB migration config
└── README.md              # Project documentation
```

---

## Getting Started

### Prerequisites

- **Python**: Version `3.12.6` or higher
- **pip**: Version `24.3.1` or higher

### Setup & Installation

1. **Clone & Navigate**:
   ```bash
   git clone https://github.com/BradleyParkerDev/fastapi_server_w_database_cron_and_logging.git
   cd fastapi_server_w_database_cron_and_logging
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   ```bash
   source ./venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate     # Windows
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables**:
   - Create a `.env` file based on `example.env`.
   ```bash
   cp example.env .env
   ```



### Database Setup
---

## Scripts

### Start the Server
To start the FastAPI server:
```bash
python main.py
```

By default, the server runs at `http://127.0.0.1:3010`.

---

## Development Notes

### Routes
- **API Routes**: Defined in `app/routes/users_routes.py` for user-related API endpoints.
- **Web Routes**: Defined in `app/routes/web_routes.py` for rendering web pages using templates.

### Middleware
Custom middleware can be found in `main.py`:
- **Authorization Middleware**: Intended purpose is to manage the user's session.
- **No-Cache Middleware**: Disables browser caching.

### Hot Reloading with Arel
- **Hot Reload**: Using Arel, any changes made to files in the `resources` and `public` directories automatically trigger a browser refresh.
- **WebSocket Setup**: A WebSocket route is included in `main.py` to support hot reloading.

### Installed Packages
- The only two packages that were explicitly installed for this project were **`FastAPI`** and **`Arel`**.
- All of the other packages that are listed in the `requirements.txt` were automatically downloaded as dependencies for these two packages.

---

## Requirements

Below are the primary dependencies:
- **FastAPI**: The core framework for APIs.
- **Jinja2**: Template rendering for web routes.
- **Uvicorn**: ASGI server for FastAPI.
- **Python-Dotenv**: Environment variable management.
- **Starlette**: Provides foundational ASGI support.
- **AnyIO**: Manages asynchronous operations.
- **Arel**: Enables hot reloading for improved development workflow.

See `requirements.txt` for the full list of dependencies.

---

## License

This project is open for personal and educational use. No specific license applies.
