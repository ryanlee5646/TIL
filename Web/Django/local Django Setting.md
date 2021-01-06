### Bash에서 django환경설정하기

1.  `mkdir api(폴더명)`: 프로젝트 작업환경을 설정할 폴더를 생성 후 폴더로 이동

2.  원래는 가상환경 설정할때 python을 앞에 붙이지만 bash에서는 그걸 인식 못함.

그래서 따로 설정을 해줘야함.

그래서 `cd~` 로 폴더 바깥에 나가서 `code .bash_profile` 을 실행 후 `alias python='winpty python'`

를 작성해준다.

3. 

4. `python -m venv api(가상환경이름)-venv`: 아무런 메세지가 안나오는게 정상

5. `ls`를 입력하면 가상환경 확인가능
6. `source api-venv/Scripts/activate`:  

### CMD에서 환경설정

1. `C:\Users\student>cd gyujin/django/api` 폴더로 이동
2. `api-venv\Scripts\activate.bat` basho에서와는 다르게 source 빼고 입력
3. `pip install django` 입력(버전에 맞게)

4. `pip install djangorestframework`

5. `pip install django-rest-swagger`