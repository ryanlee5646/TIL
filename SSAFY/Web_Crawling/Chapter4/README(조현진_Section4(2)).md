## 섹션 4. 파이썬 다양한 데이터 형식 가공하기(2)



### 파이썬으로 JSON 데이터 다루기

* JSON 데이터 간단 개요

  JSON : Number, Object, Boolean, String, Array, Null 등을 한번에 처리하여 보낼 수 있다.

* 파이썬으로 JSON 데이터 읽고 쓰기

  ```python
  import simplejson as simplejson
  import json
  
  # Dict(Json) 선언
  
  data = {}
  data['people'] = []
  data['people'].append({
      'name':'Kim',
      'website':'naver.com',
      'from':'Seoul'
  })
  data['people'].append({
      'name':'Kim',
      'website':'google.com',
      'from':'Busan'
  })
  data['people'].append({
      'name':'Kim',
      'website':'daum.net',
      'from':'Incheon'
  })
  
  # print(data)
  
  # {'people': [{'name': 'Kim', 'from': 'Seoul', 'website': 'naver.com'}, {'name': 'Kim', 'from': 'Busan', 'website': 'google.com'}, {'name': 'Kim', 'from': 'Incheon', 'website': 'daum.net'}]}
  
  # Dict(Json) -> Str
  e = json.dumps(data, indent=4)
  # print(type(e))
  # print(e)
  
  # Str -> Dict(Json)
  d = json.dumps(e)
  # print(type(d))
  # print(d)
  
  with open('C:/Users/student/Desktop/section4/member.json','w') as outfile:
      outfile.write(e)
  
  
  with open('C:/Users/student/Desktop/section4/member.json','r') as infile:
      r = json.loads(infile.read())
      print("=====")
      # print(type(r))
      # print(r)
      for p in r['people']:
          print('Name:' + p['name'])
          print('website:' + p['website'])
          print('From:' + p['from'])
          print('')
  ```

  

* 파이썬으로 JSON 데이터 파싱하기

  ```python
  import simplejson as simplejson
  import json
  
  # Dict(Json) 선언
  
  data = {}
  data['people'] = []
  data['people'].append({
      'name':'Kim',
      'website':'naver.com',
      'from':'Seoul',
      'grade':[95,77,89,91]
  })
  data['people'].append({
      'name':'Kim',
      'website':'google.com',
      'from':'Busan',
      'grade':[86,67,100,93]
  })
  data['people'].append({
      'name':'Kim',
      'website':'daum.net',
      'from':'Incheon',
      'grade':[98,79,99,92]
  })
  
  # print(data)
  
  # json 파일쓰기(dump)
  
  with open('C:/Users/student/Desktop/section4/member.json','w') as outfile:
      json.dump(data, outfile)
  
  with open('C:/Users/student/Desktop/section4/member.json','r') as infile:
      r = json.load(infile)
      # print(type(r))
      # print(r)
      print("==============")
      for p in r['people']:
          print('Name:' + p['name'])
          print('website:' + p['website'])
          print('From:' + p['from'])
          t = p['grade']
          grade = ''
          for g in t:
              grade = grade + ' ' + str(g)
          print('Grade:',grade.lstrip())
          print('')
  ```

  

* Github Repository JSON 데이터 파싱 실습

  ```python
  import urllib.request as req
  import simplejson as json
  import os.path
  
  
  # url
  url="https://api.github.com/repositories"
  
  # 경로 & 파일명
  savename = 'C:/Users/student/Desktop/section4/repo.json'
  
  if not os.path.exists(url):
      req.urlretrieve(url, savename)
  
  items = json.load(open(savename, 'r', encoding='utf-8'))
  # items = json.load(open(savename, 'r', encoding='utf-8').read())
  
  # 출력
  for item in items:
      print(item["full_name"] + " - " + item["owner"]["url"])
  
  ```

  