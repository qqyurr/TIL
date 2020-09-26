

[TOC]

# FishTank

> 물고기를 키우거나, 키우고 싶은 사람들끼리 정보를 공유하는 페이지를 만드는 프로젝트입니다.
>
> Django를 이용하여 CRUD, auth, comment 기능 구현

## 00. Intro

### venv 설정

```bash
$ python -m venv venv
```

```bash
$ pip install –r requirements.txt
```

### 프로젝트, 앱 생성

```bash
$ django-admin startproject CRUD .
```

```bash
$ python manage.py startapp articles
```

### Url생성

1. settings.py에 앱 등록

2. urls.py에 include사용해서 url 설정

3. articles에 urls.py 파일 생성

4. urls.py

   ```python
   from django.urls import path
   ```

   ```python
   app_name = 'articles'
   urlpatterns = [
   ]
   ```

### Template 생성

articles폴더에 templates폴더를 생성하고 그 안에 articles폴더를 만들어준다.**articles폴더와 나중에 만들 accounts폴더의 templates를 구분해주기 위해!**

## 01. Model

### model 정의

```python
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(_(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

### makemigrations, migrate

```bash
$ python manage.py makemigrations
```

```bash
$ python manage.py migrate
```



## 02. CRUD

### CRUD 

#### 1.Create

#### 2.Read

#### 3.Update

#### 4.Delete

### Admin

## 03. Form

1. ModelForm
2. Form 분리

## 04. Static & Media

1. Static
2. Media

## 05. Auth

1. Accounts
2. Sign Up
3. Login
4. Lougout
5. 접근 제한
6. 회원 탈퇴
7. 회원 수정
8. 비밀번호 변경

## 06. Many to one

1. ForeignKey
2. Comment
   1. CREATE
   2. READ
   3. DELETE