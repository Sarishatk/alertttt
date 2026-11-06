DYNATRACE ALERT TRACKER — SHARED TEAM VERSION (NO LOGIN)
========================================================

This project is a Django application. It uses PostgreSQL (Neon) as the shared
team database when DATABASE_URL is configured. All team members using the same
deployed URL see the same records.

FEATURES
--------
- No login page.
- Add, view, edit and delete alert records.
- Fields: Date, Alert Name, Triggered Time, Tower (including Other), Update,
  Status, Entered By and Last Updated By.
- Records page refreshes every 15 seconds.
- Asia/Kolkata timezone.

IMPORTANT SECURITY NOTE
-----------------------
Because there is no login, anyone who knows the website URL can view, add, edit,
or delete records. Do not enter passwords, customer data, confidential incident
information, or other sensitive company information. Use only if your company
approves this access model. The Entered By field is self-reported, not verified.

A. OPEN AND TEST IN VS CODE (WINDOWS POWERSHELL)
------------------------------------------------
1. Extract this ZIP.
2. In VS Code, open the folder that contains manage.py.
3. Open Terminal > New Terminal and run these commands one by one:

   py -3.12 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver

4. Open http://127.0.0.1:8000/

If activation is blocked, run:
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
Then activate the environment again.

Without DATABASE_URL, local development uses SQLite. That local database is
NOT shared with Vercel or other computers.

B. CREATE THE SHARED DATABASE (NEON)
------------------------------------
1. Create a PostgreSQL database/project in https://neon.tech/.
2. Copy its pooled PostgreSQL connection string. It should start with
   postgresql:// and include sslmode=require (Neon provides this).
3. Keep the connection string private. Never commit it to GitHub or paste it
   into source code.

C. SET VERCEL ENVIRONMENT VARIABLES BEFORE DEPLOYING
----------------------------------------------------
In Vercel > your Project > Settings > Environment Variables, add these for
Production (and Preview too, if you want preview deployments to work):

   DATABASE_URL       = Neon pooled PostgreSQL connection string
   DJANGO_SECRET_KEY  = a long random secret key
   DJANGO_DEBUG       = False

Generate a secret locally with:
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

If you use a custom domain, optionally add:
   APP_DOMAIN = your-domain.example

After changing environment variables, trigger a NEW deployment. Old deployments
do not receive newly added environment variables.

D. PUSH TO GITHUB AND DEPLOY FROM VERCEL
----------------------------------------
1. Create/open your GitHub repository.
2. Put the CONTENTS of this project folder in the repository root (manage.py
   should be at the repository root, not hidden inside another nested folder).
3. Commit and push to the branch connected to Vercel (usually main).
4. In Vercel, import/connect that GitHub repository. The project Root Directory
   should be the folder containing manage.py. Leave the Django build settings on
   Vercel's automatic detection unless your dashboard specifically requires one.
5. Deploy. Vercel's current Django support detects manage.py automatically; this
   project intentionally does not use the older custom api/index.py routing.

E. CREATE TABLES IN NEON (ONE-TIME SETUP)
-----------------------------------------
After the Vercel environment variables are configured, run migrations once from
PowerShell in this project folder, using the Neon connection string:

   $env:DATABASE_URL = "PASTE_NEON_CONNECTION_STRING_HERE"
   $env:DJANGO_SECRET_KEY = "PASTE_THE_SAME_DJANGO_SECRET_KEY_HERE"
   python manage.py migrate

This creates the tables in the shared Neon database. Do not run migrations on
SQLite and assume those tables are created in Neon; they are separate databases.

F. IF VERCEL STILL SHOWS 500 FUNCTION_INVOCATION_FAILED
-------------------------------------------------------
The 500 page is only a generic message. In Vercel open the failed Deployment >
Functions/Logs and inspect the Python traceback. Common causes are:
- DJANGO_SECRET_KEY missing from the Production environment.
- DATABASE_URL missing, invalid, or copied from the wrong Neon project.
- Neon database not reachable / incorrect credentials.
- Migrations not run against Neon.

Check that DATABASE_URL and DJANGO_SECRET_KEY are present in the same Vercel
environment as the deployment. Never share their values in screenshots or chat.

requirements.txt contains only the runtime packages required by this project.
