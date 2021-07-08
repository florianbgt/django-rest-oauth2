---
title: Django REST Oauth2 authentication
description: Oauth2 implementation with Django REST project 
---

## Setting up our Django REST project

Setting up virtual environement
```bash
mkdir django-rest-oauth2
cd django-rest-oauth2
python -m venv env
### If you are using Windows
env\scripts\activate
### If you are using Mac or Linux
source env/bin/activate
```

install dependencies and setup django rest
```bash
pip install django djangorestframework
django-admin startprojects _project .
```

```python
### _project/settings.py
...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #local
    #third parties
    'rest_framework'        #new
]
...
```

Setting up custom user model
```bash
python manage.py startapp users
```

```python
### project/settings.py
...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #local
    'users',     #new
    #third parties
    'rest_framework',
]
...
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'users.CustomUser'        #new
...
```

```bash
python manage.py makemigrations users
python manage.py migrate
```

Fix admin
```bash
touch users/forms.py
```

```python
### users/forms.py
from django.contrib.auth import get_user_model      #new
from django.contrib.auth.forms import UserCreationForm, UserChangeForm      #new

class CustomUserCreationForm(UserCreationForm):      #new
    class Meta:      #new
        model = get_user_model()      #new
        fields = ('email', 'username',)      #new


class CustomUserChangeForm(UserChangeForm):      #new
    class Meta:      #new
        model = get_user_model()      #new
        fields = ('email', 'username',)      #new
```

```python
### users/admin.py
from django.contrib import admin      #new
from django.contrib.auth import get_user_model      #new
from django.contrib.auth.admin import UserAdmin      #new
from .forms import CustomUserCreationForm, CustomUserChangeForm      #new

CustomUser = get_user_model()      #new

class CustomUserAdmin(UserAdmin):      #new
    add_form = CustomUserCreationForm      #new
    form = CustomUserChangeForm      #new
    model = CustomUser      #new
    list_display = ['email', 'username',]      #new

admin.site.register(CustomUser, CustomUserAdmin)      #new
```

## Installing Django Oauth Toolkit

Installing package
```bash
pip install django-oauth-toolkit
```

```python
### _project/settings.py
...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #local
    'users',
    #third parties
    'rest_framework',
    'oauth2_provider',      #new
]
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


REST_FRAMEWORK = {      #new
    'DEFAULT_AUTHENTICATION_CLASSES': (     #new
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',      #new
    )       #new
}       #new
...
```

## Create simple API vies

```bash
python manage.py startapp tasks
```

```python
### _project/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #local
    'users',
    'tasks',        #new
    #third parties
    'rest_framework',
    # 'oauth2_provider',
]
```

```python
### tasks/models.py
from django.db import models

class PublicTask(models.Model):        #new
    title = models.CharField(max_length=50),        #new
    body: models.TextField(max_length=500)        #new

class TeamTask(models.Model):        #new
    title = models.CharField(max_length=50),        #new
    body: models.TextField(max_length=500)        #new

class PrivateTask(models.Model):        #new
    title = models.CharField(max_length=50),        #new
    body: models.TextField(max_length=500)        #new
```

```python
### tasks/admin.py
from django.contrib import admin
from .models import PublicTask, TeamTask, PrivateTask        #new

admin.site.register(PublicTask)        #new
admin.site.register(TeamTask)        #new
admin.site.register(PrivateTask)        #new
```

```bash
touch tasks/serializers.py
```

```python
###tasks/serializers.py
from rest_framework import serializers        #new
from .models import PublicTask, TeamTask, PrivateTask        #new

class PublicTaskSerializer(serializers.ModelSerializer):        #new
    class Meta:        #new
        model = PublicTask        #new
        fields = '__all__'        #new


class TeamTaskSerializer(serializers.ModelSerializer):        #new
    class Meta:        #new
        model = TeamTask        #new
        fields = '__all__'        #new


class PrivateTaskSerializer(serializers.ModelSerializer):        #new
    class Meta:        #new
        model = PrivateTask        #new
        fields = '__all__'        #new
```

```python
### tasks/views.py
from rest_framework import generics        #new
from .models import PublicTask, TeamTask, PrivateTask        #new
from .serializers import PublicTaskSerializer, TeamTaskSerializer, PrivateTaskSerializer        #new


class ListPublicTask(generics.ListCreateAPIView):        #new
    queryset = PublicTask.objects.all()        #new
    serializer_class = PublicTaskSerializer        #new


class DetailPublicTask(generics.RetrieveDestroyAPIView):        #new
    queryset = PublicTask.objects.all()        #new
    serializer_class = PublicTaskSerializer        #new


class ListTeamTask(generics.ListCreateAPIView):        #new
    queryset = TeamTask.objects.all()        #new
    serializer_class = TeamTaskSerializer        #new


class DetailTeamTask(generics.RetrieveDestroyAPIView):        #new
    queryset = TeamTask.objects.all()        #new
    serializer_class = TeamTaskSerializer        #new


class ListPrivateTask(generics.ListCreateAPIView):        #new
    queryset = PrivateTask.objects.all()        #new
    serializer_class = PrivateTaskSerializer        #new


class DetailPrivateTask(generics.RetrieveDestroyAPIView):        #new
    queryset = PrivateTask.objects.all()        #new
    serializer_class = PrivateTaskSerializer        #new
```

```bash
touch taks/urls.py
```

```python
### tasks/urls.py
from django.urls import path        #new
from .views import ListPublicTask, DetailPublicTask, ListTeamTask, DetailTeamTask, ListPrivateTask, DetailPrivateTask        #new

urlpatterns = [        #new
    path('public/', ListPublicTask.as_view()),        #new
    path('public/<int:pk>', DetailPublicTask.as_view()),        #new
    path('team/', ListTeamTask.as_view()),        #new
    path('team/<int:pk>', DetailTeamTask.as_view()),        #new
    path('private/', ListPrivateTask.as_view()),        #new
    path('private/<int:pk>', DetailPrivateTask.as_view())        #new
]        #new
```

```python
### _project/urls.py
from django.contrib import admin
from django.urls import path, include        #new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls'))        #new
]

```

```bash
python manage.py makemigrations tasks
python manage.py migrate
```