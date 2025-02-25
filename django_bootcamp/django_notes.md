# Django Learning Guide

## Setting Up the Virtual Environment
```sh
python -m venv env  # Create a virtual environment
source env/bin/activate  # Activate the virtual environment (Linux/macOS)
# On Windows, use: env\Scripts\activate
```

## Creating a Django Project
```sh
django-admin startproject config .  # Initialize a Django project in the current directory
python manage.py runserver  # Start the development server
```

## Creating a Django App
```sh
python manage.py startapp <app_name>  # Create a new Django app
```
### Registering the App
Add the new app to `INSTALLED_APPS` in `config/settings.py`:
```py
INSTALLED_APPS = [
    ...
    '<app_name>',
]
```

## URLs and Views
### Views
Create a view in your app’s `views.py`:
```py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
```

### URLs
Define the URL pattern in your app’s `urls.py`:
```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```
Then, include the app’s URLs in the project's `config/urls.py`:
```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('<app_name>.urls')),
]
```

### Importance of URL Order
The order of URLs in `urlpatterns` is important. Django matches URLs from top to bottom and executes the first match it finds.

---
## Django Apps and Separation of Concerns
Django encourages breaking projects into multiple apps for better maintainability and modularity.

---
## Templates Structure
### Configuring Templates
In `config/settings.py`, ensure `'APP_DIRS': True` is set in `TEMPLATES`:
```py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        ...
    },
]
```

### Creating a Template Directory
```sh
mkdir -p <app_name>/templates/<app_name>
touch <app_name>/templates/<app_name>/index.html
```
Django will look for templates inside each app’s `templates/` directory by default.

---
## Models and Database Migrations
### Model Manager
```py
# Querying the database
ModelClass.objects.all()  # Get all records
ModelClass.objects.get(id=1)  # Get a specific record (raises error if not found)
ModelClass.objects.filter(company='kreditech')  # Filter records
```

### Making Migrations
```sh
python manage.py makemigrations  # Generate migration files
python manage.py migrate  # Apply migrations to the database
```

### Using Django Shell for Database Operations
```sh
python manage.py shell
```
```py
from <app_name>.models import ModelClass

# Create a new record
ModelClass.objects.create(field_name='value')

# Retrieve and update a record
instance = ModelClass.objects.get(id=1)
instance.field_name = 'updated value'
instance.save()

# Delete a record
instance.delete()
```

---
## Humanizing Data in Templates
Django provides the `humanize` filter to format numbers in a more readable way.

### Enable `humanize`
In `config/settings.py`, add:
```py
INSTALLED_APPS += ['django.contrib.humanize']
```

### Using `humanize` in Templates
At the top of your template, load `humanize`:
```html
{% load humanize %}

{{ salary|intcomma }}  {# Outputs: 45,000 instead of 45000 #}
```

---
## Admin Panel
### Creating a Superuser
```sh
python manage.py createsuperuser
```
Follow the prompts to set up an admin account.

### Registering Models in the Admin Panel
If your model does not appear in the Django admin panel, ensure it is registered in `admin.py`:
```py
from django.contrib import admin
from .models import ModelClass

admin.site.register(ModelClass)
```
Now, you can access the admin panel at `http://127.0.0.1:8000/admin/`.

---
## Additional Topics to Explore
- Django Middleware
- Forms and ModelForms
- Class-Based Views (CBVs)
- Django REST Framework (DRF)
- Authentication and Authorization
- Deployment (Gunicorn, Nginx, Docker)

This guide provides a solid foundation for getting started with Django. Keep building and exploring!


