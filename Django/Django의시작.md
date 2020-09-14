# Django :checkered_flag:

### 가상환경 만들기

1. 폴더에서 venv 만들기

```bash
$ python -m venv venv
```

2. 가상환경 잡기

- ctrl + shift + P 
- Python: Select Interpreter
- Python 3.7.7 64-bit ('venv':venv) 선택
- `ctrl + 벡틱`  : 터미널창 켜기
- `pip list` : 새로운 환경 확인

3. requirements 설치

```bash
$ pip install -r requirements.txt
```

+ runserver

```bash
$ python manage.py runserver
```

+ runserver 이후 `ctrl + c` 로 서버 끄고 migrations 진행 

### migrations

```bash
$ python manage.py makemigrations
```

```bash
$ python manage.py migrate
```



