### 파이썬으로 JSON 데이터 다루기

#### ● 오늘 내용 정리

1. JSON 데이터 간단 개요
2. 파이썬으로 JSON 데이터 읽고 쓰기
3. 파이썬으로  JSON 데이터 파싱 하기
4. Github Repository JSON 데이터 파싱 실습

**실습(과제): JSONPlaceholder 사이트에서 JSON 파싱 실습**

과제: https://jsonplaceholder.typicode.com

**JSON**: https://www.w3schools.com/js/js_json_syntax.asp

**SimpleJSON**: https://simplejson.readthedocs.io/en/latest

**JSON Sort 온라인**: https://jsoneditoronline.org  <= Json데이터를 정렬해주는 사이트



##### * JSON 데이터의 장점은 Number, Object, Boolean, String, Array, null 등 다양한 자료형 표현가능



`pip install simplejson`: 기존 파이썬 모듈에 json이 있지만 보다 쉽고 빠른 모듈임



#### JSON data 다루기(1)

```python 
import simplejson as json
# import json
# Dict(Json) 선언

data = {}
data['people'] = []
data['people'].append({
    'name':'Kim',
    'website': 'naver.com',
    'from':'Seoul'
})
data['people'].append({
    'name':'Park',
    'website': 'google.com',
    'from':'Busan'
})
data['people'].append({
    'name':'Lee',
    'website': 'daum.com',
    'from':'Daegu'
})

# print(data)
# Dict(Json) -> Str
e = json.dumps(data,indent=2) # 한줄로 나오는 json을 들여쓰기 해주는 indent
# print(type(e))
# print(e)

# Str -> Dict(json)
d = json.loads(e)
# print(type(d))
# print(d)

with open('C:/Users/student/Desktop/section4/member.json','w') as outfile:
    outfile.write(e)

with open('C:/Users/student/Desktop/section4/member.json','r') as infile:
    r = json.loads(infile.read())
    # print("=====")
    # print(type(r))
    # print(r)
    for p in r['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')

```

#### JSON 다루기(2)

```python
import simplejson as json
# import json

# Dict(Json) 선언

data = {}
data['people'] = []
data['people'].append({
    'name':'Kim',
    'website': 'naver.com',
    'from':'Seoul',
    'grade':[95,77,89,91]
})
data['people'].append({
    'name':'Park',
    'website': 'google.com',
    'from':'Busan',
    'grade':[85,67,100,93]
})
data['people'].append({
    'name':'Lee',
    'website': 'daum.com',
    'from':'Daegu',
    'grade':[77,98,97,44]
})

# print(data)

# sjon 파일쓰기(dump)
with open('C:/Users/student/Desktop/section4/member.json','w') as outfile:
    json.dump(data, outfile)

with open('C:/Users/student/Desktop/section4/member.json','r') as infile:
    r = json.load(infile)
    # print(type(r))
    # print(r)
    print("===============")
    for p in r['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        t = p['grade']
        grade = ''
        for g in t:
            grade = grade + ' ' + str(g)
        print('Grade:',grade.lstrip()) # lstrip 줄바끔
        print(' ')
```

#### Git에서 api 받아오기

```python
import urllib.request as request
import simplejson as json
import os.path

# url

url = "https://api.github.com/repositories"

# 경로 & 파일명
savename = "C:/Users/student/Desktop/section4/member.json"

if not os.path.exists(url):
    request.urlretrieve(url, savename)

items = json.load(open(savename, 'r', encoding='utf-8'))
items = json.loads(open(savename, 'r', encoding='utf-8').read())

# 출력
for item in items:
    print(item['full_name'] + "-" + item['owner']['url'])
```



## Pandas

#### 오늘 내용 정리

1. Python Pandas 개요
2. CSV 데이터 간단 개요
3. 파이썬 Pandas로 CSV 데이터 읽고 쓰기
4. 파이썬 Pandas로 CSV 데이터 편집하기

실습(과제) : 샘플 CSV 데이터 다운로드 후 읽기 및 쓰기 실습



과제: https://support.spatialkey.com/spatialkey-sample-csv-data

Pandas: http://pandas.pydata.org/

 

#### Pandas: 데이터 분석, 데이터 처리, 대용량, 정렬, 구조화

`pip install pandas`: pandas 설치



#### 1. Pandas 기본 

```python
import pandas as pd

# 기본 읽기
df = pd.read_csv("C:/Users/student/Desktop/section4/csv_s1.csv")
# print(df)

#    Month   "1958"   "1959"   "1960" => 자동으로 맨 위에는 header로 인식
# 0    JAN      340      360      417
# 1    FEB      318      342      391
# 2    MAR      362      406      419
# 3    APR      348      396      461
# 4    MAY      363      420      472
# 5    JUN      435      472      535
# 6    JUL      491      548      622
# 7    AUG      505      559      606
# 8    SEP      404      463      508
# 9    OCT      359      407      461
# 10   NOV      310      362      390
# 11   DEC      337      405      432

# 행 스킵
df = pd.read_csv("C:/Users/student/Desktop/section4/csv_s1.csv", skiprows=[0])
# 0번째 인덱스를 skip 했기때문에 기존 header 대신에 JAN 340 360 417이 header가 됌
# print(df)

# 행 스킵, 헤더 생략, 새로운 헤더 정의
df = pd.read_csv("C:/Users/student/Desktop/section4/csv_s1.csv", skiprows=[0], header=None, names=["Month",2013,2014,2015])
# 첫번째 줄을 건너뛰고, header을 없애고 새로운 컬럼을 추가
# print(df)

# 인덱스 컬럼 정의
df = pd.read_csv("C:/Users/student/Desktop/section4/csv_s1.csv", skiprows=[0], header=None, names=["Month",2013,2014,2015], index_col=[0])
# column에 있는 index값의 실데이터가 내려옴
# print(df)

# 특정 값 치환
df = pd.read_csv("C:/Users/student/Desktop/section4/csv_s1.csv", skiprows=[0], header=None, names=["Month",2013,2014,2015], na_values=['JAN'])
# print(df)

# 실습 정리 및 인덱스 재정의
df = pd.read_csv("C:/Users/student/Desktop/section4/csv_s1.csv", skiprows=[0], header=None, names=["Month",2013,2014,2015])
# print(df.index)
# print(list(df.index))
# print(df.index.values.tolist())
#
# print(df.rename(index={0:'aa', 1:'bb', 2:'cc'}))
# print(df.rename(index=lambda x:x*10)) # 람다식

# 읽기
df2 = pd.read_csv("C:/Users/student/Desktop/section4/csv_s2.csv", sep=';', skiprows=[0], header=None, names=['Name','Test1','Test2','Test3','Final','Grade'])
# print(df)

# 평균 내용 변경
df2 = pd.read_csv("C:/Users/student/Desktop/section4/csv_s2.csv", sep=';', skiprows=[0], header=None, names=['Name','Test1','Test2','Test3','Final','Grade'])
df2['Grade'] = df2['Grade'].str.replace('C','A++')
# print(df2)

# 평균 컬럼 추가
df2['Avg'] = df2[['Test1','Test2','Test3','Final']].mean(axis=1) # => 0이면 세로 방향으로 통계/ 1이면 가로 방향으로 통계
print(df2)

# 합계 컬럼 추가
df2['Sum'] = df2[['Test1','Test2','Test3','Final']].sum(axis=1)
print(df2)
```

```python
import pandas as pd

# 읽기
df2 = pd.read_csv("C:/Users/student/Desktop/section4/csv_s2.csv", sep=';', skiprows=[0], header=None, names=['Name','Test1','Test2','Test3','Final','Grade'])
# print(df)

# 평균 내용 변경
# df2 = pd.read_csv("C:/Users/student/Desktop/section4/csv_s2.csv", sep=';', skiprows=[0], header=None, names=['Name','Test1','Test2','Test3','Final','Grade'])
df2['Grade'] = df2['Grade'].str.replace('C','A++')
# print(df2)

# 평균 컬럼 추가
df2['Avg'] = df2[['Test1','Test2','Test3','Final']].mean(axis=1) # => 0이면 세로 방향으로 통계/ 1이면 가로 방향으로 통계
print(df2)

# 합계 컬럼 추가
df2['Sum'] = df2[['Test1','Test2','Test3','Final']].sum(axis=1)
print(df2)

# 쓰기
df2.to_csv("C:/Users/student/Desktop/section4/result_s1.csv")
df2.to_csv("C:/Users/student/Desktop/section4/result_s1.csv", index=False) # 인덱스를 컬럼을 없애고 싶다면
```

```python
import pandas as pd
import numpy as np # 선형대수, 행렬, 백터수학 등 수치데이터를 계산할 때

# 랜덤으로 DataFrame 생성
df = pd.DataFrame(np.random.randint(0,100,size=(100,4)), columns=['ONE','TWO','THREE','FOUR'])
df = pd.DataFrame(np.random.randn(100,4), columns=['ONE','TWO','THREE','FOUR'])
print(df)

df.to_csv('C:/Users/student/Desktop/section4/result_s2.csv', index=False)
df.to_csv('C:/Users/student/Desktop/section4/result_s2.csv', index=False, header=False)
```



