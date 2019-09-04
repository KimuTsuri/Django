# 新しいプロジェクトを作成する流れ

## Project, App を作成する
Project を作成する.
```
$ django-admin startproject [project name]
```
App を作成する.
```
$ cd [project name]
$ python3 manage.py startapp [app name]
```

## `project/project/`内の変更

### `settings.py`の変更
```
...omit...

# Application definition

INSTALLED_APPS = [
    'myapp.apps.MyappConfig', #change myapp → [app name]
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',

...omit...

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'ja' #change

TIME_ZONE = 'Asia/Tokyo' #change

USE_I18N = True

...omit...
```
### `urls.py`の変更
```
from django.contrib import admin
from django.urls import path, include #change

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')), #change myapp → [app name]
]

```


