# Team Issue Tracker

A Django REST API for team collaboration and issue tracking, featuring JWT authentication, Swagger docs, WebSocket notifications, background jobs, and file attachments.

## Setup & Run Instructions

### 1. Clone the Project
```sh
git clone <your-repo-url>
cd <project-folder>
```

### 2. Create and Activate Virtual Environment
```sh
python -m venv venv
venv\Scripts\activate   # On Windows
# Or use: source venv/bin/activate   # On Mac/Linux
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
# If requirements.txt is missing, install manually:
pip install django djangorestframework djangorestframework-simplejwt drf-yasg django-filter Pillow channels celery redis daphne
```

### 4. Apply Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### 5. Collect Static Files
```sh
python manage.py collectstatic --noinput
```

### 6. Create Superuser (Admin)
```sh
python manage.py createsuperuser
```

### 7. Run the App (ASGI for Channels/WebSocket)
```sh
daphne team_issue_tracker.asgi:application
# Or for standard Django:
python manage.py runserver
```

### 8. Access Swagger API Docs
- Open your browser and go to:  
  `http://127.0.0.1:8000/swagger`

---

**Notes:**
- For WebSocket and async features, use Daphne (`daphne team_issue_tracker.asgi:application`).
- For background jobs, start Redis and run Celery worker:
  ```sh
  celery -A team_issue_tracker worker --loglevel=info
  ```
- All static files are served from `/static/`.
- Swagger UI is available at the root URL.

---

Share these instructions with your team for easy setup and running of the project!
