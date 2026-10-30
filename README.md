# Portfolio Project

A Django-based personal portfolio with an AI assistant, admin panel, contact form,
and dynamic content management.

## Features

- Dynamic portfolio content (profile, skills, projects, education, experience, services)
- Django admin panel (styled with Jazzmin)
- AI portfolio assistant (OpenAI)
- Contact form with email notifications
- Project demo + source code links

## Quick Start

```bash
# 1. Create & activate a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment variables
copy .env.example .env        # Windows
# cp .env.example .env        # macOS/Linux
# then edit .env and fill in the values (see below)

# 4. Apply migrations
python manage.py migrate

# 5. Create an admin user
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

Visit http://127.0.0.1:8000/ and the admin at http://127.0.0.1:8000/admin/.

## Environment Variables (.env)

| Variable | Description |
| --- | --- |
| `DJANGO_SECRET_KEY` | Django secret key (keep secret) |
| `DJANGO_DEBUG` | `True` for development, `False` for production |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated hosts (e.g. `localhost,127.0.0.1,example.com`) |
| `EMAIL_HOST` / `EMAIL_PORT` / `EMAIL_USE_TLS` | SMTP settings |
| `EMAIL_HOST_USER` | Sender email address |
| `EMAIL_HOST_PASSWORD` | Email app password (Gmail app password) |
| `OPENAI_API_KEY` | **OpenAI API key for the AI assistant agent** |

### Where to set the OpenAI API key (agent)

The AI assistant agent reads the key from the `OPENAI_API_KEY` environment variable.

- **Local development:** put it in the `.env` file:
  ```
  OPENAI_API_KEY=sk-...
  ```
- **Production (e.g. PythonAnywhere):** add it in the web app environment variables
  (or in the WSGI file via `os.environ["OPENAI_API_KEY"] = "sk-..."`).
- Never commit the real key to version control.

## Collecting Static Files (production)

```bash
python manage.py collectstatic
```

## Tests

```bash
python manage.py test
```

## Deploy on Render

This project includes a `render.yaml` blueprint for one-click deployment.

1. Push the repo to GitHub.
2. In Render, choose **New → Blueprint** and select the repo.
3. Render will create:
   - a Python web service (build + start commands from `render.yaml`)
   - a free PostgreSQL database (`DATABASE_URL` is wired automatically)
   - a persistent disk mounted at `media/` for uploads
4. Fill in the secret env vars marked `sync: false` in the Render dashboard:
   - `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` (Gmail app password)
   - `OPENAI_API_KEY` (for the AI assistant agent)
5. After deploy, create a superuser via the Render shell:
   ```bash
   python manage.py createsuperuser
   ```

### Notes
- `DJANGO_DEBUG=False` is set in `render.yaml`; security headers/SSL are enabled automatically.
- Static files are served by WhiteNoise (`collectstatic` runs in the build step).
- User uploads (media) persist on the Render disk; for larger/production media, consider Cloudinary.
- `ALLOWED_HOSTS` defaults to `.onrender.com`; add your custom domain if needed.

## Keep the Render free tier awake

Render free web services sleep after ~15 minutes of inactivity. To keep it warm:

1. This project exposes a lightweight health endpoint: `GET /health/` (returns `{"status": "ok"}`).
2. The homepage pings `/health/` every 60 seconds while a visitor has it open.
3. For 24/7 coverage, add a free external monitor such as **UptimeRobot**:
   - Monitor type: HTTP(s)
   - URL: `https://your-app.onrender.com/health/`
   - Interval: every 5 minutes
