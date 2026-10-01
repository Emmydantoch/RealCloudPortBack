# Portfolio Backend

## Run locally

From the repository root, install the dependencies and initialize the database:

```powershell
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe backend\manage.py migrate
.\venv\Scripts\python.exe backend\manage.py createsuperuser
.\venv\Scripts\python.exe backend\manage.py runserver
```

For a local secret key, generate one with:

```powershell
.\venv\Scripts\python.exe -c "import secrets; print(secrets.token_urlsafe(50))"
```

Put the generated value in `backend/.env` as `DJANGO_SECRET_KEY=...`. Keep `DJANGO_DEBUG=True` only for local development. `backend/.env.example` shows the available backend settings, and `.gitignore` excludes local env files. The frontend's `REACT_APP_API_URL` is a public URL, not a secret; never put passwords or API tokens in `frontend/.env` because React embeds those values in the browser bundle.

Open `http://127.0.0.1:8000/admin/`, sign in, and add records under **Portfolio projects**. Choose a category, upload the image, and enter the YouTube URL and technologies. Published records appear on the portfolio site.

The public API is `http://127.0.0.1:8000/api/projects/`. Filter it with a category slug, for example `?category=product_design`. Available slugs are `product_design`, `full_stack_development`, `digital_marketing`, and `graphics`.

Uploaded images are stored in `backend/media/` for local development. Configure persistent object storage before deploying; Django's development media server is not suitable for production.

## Deploy to Railway and Vercel

The repository includes `railway.toml`. In Railway, create a project from the GitHub repository and add a PostgreSQL service. Set these variables on the Django service:

- `DATABASE_URL`: reference the PostgreSQL service's `DATABASE_URL`.
- `DJANGO_SECRET_KEY`: a fresh random key generated for production.
- `DJANGO_DEBUG`: `False`.
- `DJANGO_ALLOWED_HOSTS`: your Railway backend hostname, without `https://`.
- `CORS_ALLOWED_ORIGINS`: your Vercel site origin, including `https://` and no path.

The Railway service runs migrations and collects Django admin static files as part of deployment. Create a Railway volume mounted at `/app/backend/media` to keep uploaded project images across redeploys. Configure a backup for that volume. Do not use the local SQLite database or local media directory as production storage.

For Vercel, set the project root to `frontend`, use `npm run build`, and set the output directory to `build`. Set `REACT_APP_API_URL` to the Railway backend origin, for example `https://your-service.up.railway.app`, then redeploy because Create React App embeds this value at build time.

The Railway database starts empty; the local SQLite records and uploaded images are not copied automatically. Recreate the portfolio entries in the deployed Django admin and upload their images again. Create the production admin account in the Railway service shell with `python backend/manage.py createsuperuser`.