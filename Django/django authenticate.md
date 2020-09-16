# 0916 authenticate

python -m venv venv

ctrl shift p -> 선택

pip install -r requirements.txt

python manage.py startapp accounts -> settings.py에 등록 -> urls.py 만들고 프로젝트파일의 urls.py에 등록

Authentication Built-in Forms

회원가입 : UserCreationForm

로그인 : AuthenticationFOrm

https://docs.djangoproject.com/en/3.1/topics/auth/default/

1. 회원가입 작성 - GET

2. 회원가입 로직 - POST

   -> 두개를 한번에 signup이라는 함수에서 실행

python manage.py createsuperuser



form 과 modelform 차이

form

-  save() 없음

modelform(class meta 사용)

- article = form.save() 가능
- 모델폼은 모델을 상속받아서 굳이 저희가 필드를 안만들어줘도 괜찮아요

##### HTTP 원리!

https://developer.mozilla.org/ko/docs/Web/HTTP/Messages

주소창을 통한 모든 것은 get!

##### PASSWORD 원리!

https://d2.naver.com/helloworld/318732



DAYS_IN_SECONDS = 86400

SESSION_COOKIE_AGE = DAYS_IN_SECONDS 

SESSION_SAVE_EVERY_REQUEST = True



Authentication 과 Authorization

@login_required -> create함수위에 쓰면 create하려고 접근하면 login페이지로 이동

login을 했으면 create으로 다시 갈수있게 만들면?? 좋다

@login_required가 붙은함수에 접근했는데, 로그인안됐을때

: http://127.0.0.1:8000/accounts/login/?next=/articles/create/

튕겨진 주소가 next뒤에 붙는다!

##### action=""

action 비워놓으면 현재주소로 다시 요청

- 두개를 같이 쓰면 안된다!!!!!

@login_required # 로그인된 유저만 로그아웃이 가능하게끔 방어.

@require_POST # GET 요청으로 로그아웃이 안되게끔 방지하기 위함.

