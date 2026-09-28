# Django Portfolio

A Django 5.1 portfolio website built with reusable Django templates, Bootstrap 5,
HTMX, and Alpine.js. It includes multiple portfolio and blog layouts plus a
database-backed contact workflow that can be managed through Django admin.

## Current Status

The application currently provides:

- A server-rendered portfolio homepage composed from reusable template partials
- Ten alternative demo pages, portfolio pages, blog pages, and authentication UI templates
- Responsive Bootstrap 5 styling with SCSS sources and locally hosted theme assets
- HTMX-enhanced contact form submissions without a full-page refresh
- Alpine.js message-length feedback on the contact form
- Server-side contact validation with a non-JavaScript form submission fallback
- Persistent contact messages stored in SQLite and searchable through Django admin
- Automated tests for the contact form and service endpoint

Portfolio, blog, résumé, and authentication content is currently template-based.
Only contact messages are stored in a Django model.

## Tech Stack

### Backend

- Python 3
- Django 5.1
- SQLite for local development

### Frontend

- Django templates and reusable partials
- Bootstrap 5
- HTMX 2.0.4
- Alpine.js 3.14.8
- Project SCSS/CSS, JavaScript, fonts, icons, and images under `static/`

Bootstrap and the theme assets are served locally. HTMX and Alpine.js are loaded
from pinned jsDelivr URLs. The contact form remains functional as a standard HTML
form if those enhancement scripts are unavailable.

## Project Structure

```text
.
├── manage.py
├── requirements.txt
├── queue_django/              # Project settings, root URLs, ASGI, and WSGI
├── pages/
│   ├── admin.py               # Contact message administration
│   ├── forms.py               # Contact ModelForm and Bootstrap widgets
│   ├── migrations/            # Database migrations
│   ├── models.py              # ContactMessage model
│   ├── tests.py               # Contact workflow tests
│   ├── urls.py                # Page and contact service routes
│   └── views.py               # Template rendering and contact handling
├── templates/
│   ├── hero/                  # Hero variants
│   ├── pages/                 # Demo, blog, portfolio, auth, and error pages
│   └── partials/              # Reusable page sections and contact fragments
└── static/                    # CSS, SCSS, JavaScript, images, and fonts
```

## Routes

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/` | Renders `templates/pages/demo-1.html` |
| `GET` | `/<template_name>/` | Renders `templates/pages/<template_name>.html` when it exists |
| `POST` | `/services/contact/` | Validates and stores a contact message |
| `GET` | `/admin/` | Opens Django admin |

Unknown dynamic template names render `templates/pages/pages-404.html`. The
contact service accepts POST requests only and returns an HTML fragment for HTMX
requests. Standard form submissions redirect to the homepage after a successful
save.

## Getting Started

### 1. Clone and enter the repository

```bash
git clone <your-repository-url>
cd django-porfolio
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install the Python dependencies

```bash
python -m pip install -r requirements.txt
```

No Node.js installation or frontend build step is currently required.

### 4. Apply database migrations

```bash
python manage.py migrate
```

This creates the development database and the table used to store contact
messages.

### 5. Optionally create an administrator

```bash
python manage.py createsuperuser
```

After signing in at `/admin/`, contact messages can be viewed and searched.

### 6. Run the development server

```bash
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in a browser.

## Contact Workflow

1. Django renders a CSRF-protected `ContactMessageForm` on portfolio landing pages.
2. HTMX posts the form to `/services/contact/` and replaces the form with either
   field errors or a success message.
3. Alpine.js updates the message character counter in the browser.
4. Django validates the submitted values and stores valid messages in the database.
5. If JavaScript is unavailable, the browser submits the same form normally and
   Django redirects back to the homepage after saving it.

The service stores messages but does not currently send email notifications.

## Testing and Validation

Run the automated test suite:

```bash
python manage.py test
```

Run Django's project checks:

```bash
python manage.py check
```

Confirm that model changes have a corresponding migration:

```bash
python manage.py makemigrations --check --dry-run
```

The test suite covers homepage form rendering, successful HTMX submissions,
validation failures, standard HTML submissions, database persistence, and
rejection of unsupported request methods.

## Development Notes

- Template and static-file discovery is configured for the top-level `templates/`
  and `static/` directories.
- The dynamic page route must remain after specific service routes so it does not
  capture paths intended for Django services.
- The legacy `static/js/contact.js` and `static/php/contact.php` files remain in
  the theme assets but are not loaded by the current contact workflow.
- The SCSS files are source files; the application directly serves the committed
  CSS and does not currently define an automated SCSS build command.

## Production Considerations

The included settings are for local development and must not be used unchanged in
production. Before deployment:

- Read the secret key from a protected environment variable.
- Disable `DEBUG`.
- Configure `ALLOWED_HOSTS`.
- Configure HTTPS redirects, HSTS, and secure session and CSRF cookies.
- Configure production static-file serving.
- Use a production database and define backup and retention policies for contact data.
- Add rate limiting or spam protection to the public contact endpoint.
- Review whether HTMX and Alpine.js should be self-hosted and add an appropriate
  Content Security Policy.
- Run `python manage.py check --deploy` against the production settings.

## License

This project is available under the [MIT License](LICENSE).
