SHS Alumni Portal

Quick notes to run locally and deploy to Render.

Run locally (development):

1. Create a Python virtualenv and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Start the app:

```bash
python3 shs_portal/app.py
```

3. Open http://127.0.0.1:5000 in your browser.

Deploy to Render (recommended for this assignment):

1. Push your repo to GitHub.
2. On Render, create a new Web Service and connect the repo.
3. Use the following settings:
   - Build command: `pip install -r requirements.txt` (Render will run this automatically)
   - Start command: `gunicorn shs_portal.app:app --bind 0.0.0.0:$PORT`
4. Set environment variables on Render:
   - `ADMIN_SECRET` (optional) — admin password for quick admin creation (default: `adminpass`)
   - `SECRET_KEY` — set a secure random secret for session encryption

Notes:
- The app uses SQLite (`shs_portal/shs_portal.db`). Render web services have ephemeral disks on scaled instances; for a class assignment this is fine but for persistent production data use a managed DB (Postgres).
- The password reset flow uses internal API endpoints (`/api/check-email` and `/api/reset-password`) which store the new password directly in the DB. There is no email delivery by default.

If you want, I can also:
- Add a `Procfile` or `Dockerfile` for alternative deploys.
- Add a small script to generate a secure `SECRET_KEY`.
# Alumni-Portal-Final
# Alumni-Portal-Final
