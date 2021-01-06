1. Django에서 모델의 기초 데이터베이스의 값을 제공하기 위해서는 Fixtures를 사용한다. 해당파일은 기본적으로 각각의 app에 fixtures폴더에 있어야하며, 파일형식은 [   ]이거나 [   ]이다.

   => **json, yaml**(**xml**)

2. 워크샵처럼 실제Django에 데이터가 저장되어 있을 때, 아래의 fixtures파일을 만들고자 한다. 사용해야 하는명령어를 작성하라.

   => `python manage.py dumpdata myapp.person --indent2 > person.json` 

   => `python manage.py dumpdata > person.json` 

   # 뒤에 앱이름[모델명]이 없으면 모든 모델을 다 넘겨줌

