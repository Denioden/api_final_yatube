# Проект «API для Yatube»

## Описание:
Проект включает backend соцеальной сети для публикации и работы с постами.

### Реализован функционал дающий возможность:

#### Аутентифицированному пользователю:
* Подписываться на авторов постов.
* Просматривать, создавать , удалять и изменять посты.
* Просматривать и создавать группы.
* Комментировать, смотреть, удалять обновлять комментарии.

 #### Неаутентифицированному пользователю:
 * Просматривать посты, группы и коментарии.

К API есть документация по адресу http://localhost:8000/redoc/

## Технологии:

 * Python 3.7 
 * Django 2.2.16
 * Django REST Framework
 * JWT + Djoser

## Установка:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Denioden/api_final_yatube.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python3.7 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Примеры:   

### Регистрируем нового пользователя.

Отправляем POST-запрос на адрес ```api/v1/users/``` и передаем 2 поля в `data`. 
1. `username` - указываем имя пользователя.
2. `password` - указываем пароль пользователя.

### Получаем токен.

Отправляем POST-запрос на адрес ```api/v1/jwt/create``` и передаем 2 поля в `data`. 
1. `username` - указываем имя пользователя.
2. `password` - указываем пароль пользователя.

___Примечание.___ 
* Токен `refresh` нужен, чтобы обновить текущий токен. 
* Токен `access` нужно сохранить и бережно *хранить*. Используется для аунтефикации пользователя.
* Жизнь токена 1 день, в настройках можно изменить.

### Создать новый пост (POST):

(Требуется аутентификация)
```
http://127.0.0.1:8000/api/v1/posts/

```
### Получить определенный пост (GET):
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/
```

### Получить список всех постов (GET):
```
http://127.0.0.1:8000/api/v1/posts/
```

### Создать коментарий определенного поста (POST):
(Требуется аутентификация)
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```

### Получить коментарии определенного поста (GET):
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```

## Об авторе:

Студент "Яндек"с Практикум" - Откидышев Даниил Вячеславович

Контактный номер: 8-913-771-33-18
