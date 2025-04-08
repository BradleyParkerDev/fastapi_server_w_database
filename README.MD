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

- **Python**: Version `3.13.1` or higher
- **pip**: Version `25.0.1` or higher

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

   **Configure `.env` with your connection string**:
   ```bash
   DATABASE_URL=postgresql://user:password@localhost:5432/your_database
   ```
   **Run Alembic Migrations**
   ```bash
   alembic revision --autogenerate -m "init"
   alembic upgrade head
   ```

### Cron Job Configuration

   **Enable in `.env`**:
   ```bash
   RUN_SCHEDULER=true
   ```
   **Runtime Control (in code)**:
   ```bash
   cron = CronJobUtility()
   cron.session.start_cron()     # Starts cron
   cron.session.stop_cron()      # Stops cron
   cron.session.restart_cron()   # Restarts cron
   ```
   Cron job runs every 10 minutes (10, 20, ..., 0) to clean expired sessions. It deletes expired sessions directly from the database, ensuring stale session data does not persist.

---

## Scripts

### Start the Server
To start the FastAPI server:
```bash
python main.py
```

By default, the server runs at `http://127.0.0.1:3010`.

---

## License

This project is open for personal and educational use. No specific license applies.
