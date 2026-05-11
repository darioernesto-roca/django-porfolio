# Django Portfolio Template

A Django 5.1 project that serves a multi-page personal portfolio website from reusable templates and static assets.

## Overview

This repository contains:

- A Django project: `queue_django`
- A single Django app: `pages`
- A large set of HTML templates for portfolio, blog, auth, hero, and demo pages
- Front-end assets (CSS, JS, SCSS, fonts, and images) under `static/`

The default homepage renders `templates/pages/demo-1.html` and any route like `/demo-2/` or `/blog/` dynamically maps to `templates/pages/<route>.html`.

## Tech Stack

- Python 3
- Django 5.1
- SQLite (default development database)
- Static front-end libraries bundled locally in `static/`

## Project Structure

```text
.
├── manage.py
├── requirements.txt
├── queue_django/          # Django project settings and root URL config
├── pages/                 # App with view and URL routing logic
├── templates/             # HTML templates (pages, hero sections, partials)
└── static/                # CSS, JS, images, fonts, and SCSS sources
```

## Routing Behavior

- `/` → renders `templates/pages/demo-1.html`
- `/<template_name>/` → attempts to render `templates/pages/<template_name>.html`
- Missing templates fall back to `templates/pages/pages-404.html`

## Getting Started

### 1) Clone and enter the repository

```bash
git clone <your-repo-url>
cd django-porfolio
```

### 2) Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows PowerShell
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Run migrations

```bash
python manage.py migrate
```

### 5) Start the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Common Commands

```bash
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser
python manage.py test
```

## Notes

- `DEBUG=True` and an exposed development secret key are currently set in `queue_django/settings.py`; do not use these settings in production.
- Static files are configured with `STATICFILES_DIRS = [BASE_DIR / "static"]` for development.

## License

No license file is currently included in this repository. Add one if you intend to distribute or open-source the project.
