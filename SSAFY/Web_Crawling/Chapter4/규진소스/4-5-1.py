import pandas as pd

# 기본 읽기
# df = pd.read_csv("C:/Users/student/Desktop/section4/csv_s1.csv")
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
# df = pd.read_csv("C:/Users/student/Desktop/section4/csv_s1.csv", skiprows=[0])
# 0번째 인덱스를 skip 했기때문에 기존 header 대신에 JAN 340 360 417이 header가 됌
# print(df)

# 행 스킵, 헤더 생략, 새로운 헤더 정의
# df = pd.read_csv("C:/Users/student/Desktop/section4/csv_s1.csv", skiprows=[0], header=None, names=["Month",2013,2014,2015])
# 첫번째 줄을 건너뛰고, header을 없애고 새로운 컬럼을 추가
# print(df)

# 인덱스 컬럼 정의
# df = pd.read_csv("C:/Users/student/Desktop/section4/csv_s1.csv", skiprows=[0], header=None, names=["Month",2013,2014,2015], index_col=[0])
# column에 있는 index값의 실데이터가 내려옴
# print(df)

# 특정 값 치환
# df = pd.read_csv("C:/Users/student/Desktop/section4/csv_s1.csv", skiprows=[0], header=None, names=["Month",2013,2014,2015], na_values=['JAN'])
# print(df)

# 실습 정리 및 인덱스 재정의
# df = pd.read_csv("C:/Users/student/Desktop/section4/csv_s1.csv", skiprows=[0], header=None, names=["Month",2013,2014,2015])
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
# df2 = pd.read_csv("C:/Users/student/Desktop/section4/csv_s2.csv", sep=';', skiprows=[0], header=None, names=['Name','Test1','Test2','Test3','Final','Grade'])
df2['Grade'] = df2['Grade'].str.replace('C','A++')
# print(df2)

# 평균 컬럼 추가
df2['Avg'] = df2[['Test1','Test2','Test3','Final']].mean(axis=1) # => 0이면 세로 방향으로 통계/ 1이면 가로 방향으로 통계
print(df2)

# 합계 컬럼 추가
df2['Sum'] = df2[['Test1','Test2','Test3','Final']].sum(axis=1)
print(df2)
