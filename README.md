# Django
Django framework for Mac

## New Project start
```
$ django-admin startproject [project name]
```

## New App start
```
$ python3 manage.py startapp [app name]
```

## Open Run server
```
$ python3 manage.py runserver
Django version 2.2.4, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
ブラウザで`http://127.0.0.1:8000/`を開く.

## Add changes
```
$ python3 manage.py makemigrations [app name]
$ python3 manage.py migrate
```

## 管理画面
```
$ python3 manage.py createsuperuser
ユーザー名 : [user name]
メールアドレス: [mail address]
Password: 
Password (again): 
Superuser created successfully.
```
これで管理ユーザーが作成できる.
`http://127.0.0.1:8000/admin/`
↑管理画面
