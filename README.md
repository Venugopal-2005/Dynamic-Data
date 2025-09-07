# Django Task Project

This is a Django project with a task management system.

## Project Structure
```
myproject/
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── myapp/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── static/
    │   └── css/
    │       └── style.css
    └── templates/
        └── task.html
```

## Setup Instructions

1. Extract the ZIP file
2. Navigate to the myproject directory
3. Install Django:
   ```bash
   pip install django
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
6. Access the task page at: http://localhost:8000/url/task/

## Features

- Task.html page with dynamic data
- CSS styling with modern design
- URL routing: localhost:8000/url/task/
- View that responds with task.html
- Dynamic data display including:
  - User information
  - Task list with status
  - Statistics
  - Current timestamp

## URL Configuration

The project includes the required URL pattern:
- Main URLs: `/url/` includes app URLs
- App URLs: `/task/` maps to task_view
- Final URL: `localhost:8000/url/task/`

## Dynamic Data

The view provides dynamic data including:
- User name and role
- Current timestamp
- Task list with different statuses
- Task statistics (total, completed, pending)
