import pandas as pd

# 기본 읽기
# df = pd.read_csv('C:/Users/student/Desktop/section4/csv_s1.csv')
# print(df)

# 행 스킵
# df = pd.read_csv('C:/Users/student/Desktop/section4/csv_s1.csv', skiprows=[0])
# print(df)

# 행 스킵, 헤더 생략
# df = pd.read_csv('C:/Users/student/Desktop/section4/csv_s1.csv', skiprows=[0], header=None)
# print(df)

# 헤더 정의
# df = pd.read_csv('C:/Users/student/Desktop/section4/csv_s1.csv', skiprows=[0], header=None, names=["Month",2013,2014,2015])
# print(df)

# 인덱스 컬럼 정의
# df = pd.read_csv('C:/Users/student/Desktop/section4/csv_s1.csv', skiprows=[0], header=None, names=["Month",2013,2014,2015], index_col=[0])
# print(df)

# 특정 값 치환
# df = pd.read_csv('C:/Users/student/Desktop/section4/csv_s1.csv', skiprows=[0], header=None, names=["Month",2013,2014,2015], index_col=[0], na_values=['JAN'])
# print(pd.isnull(df))
# print(df)

# 실습 정리 및 인덱스 재정의
df = pd.read_csv('C:/Users/student/Desktop/section4/csv_s1.csv', skiprows=[0], header=None, names=["Month",2013,2014,2015])
# print(df)
# print(df.index)
# print(list(df.index))
# print(df.index.values)
# print(df.index.values.tolist())
# print(df.rename(index={0:'aa', 1:'bb', 2:'bb'}))
# print(df.rename(index=lambda x:x*10))

# 읽기
df2 = pd.read_csv('C:/Users/student/Desktop/section4/csv_s2.csv',sep=';', skiprows=[0], header=None, names=['Name', 'Test1', 'Test2', 'Test3', 'Final','Grade'])
# print(df)

# 컬럼 내용 변경
# df2['Grade'] = df2['Grade'].str.replace('C', 'A++')
# print(df2)

# 평균 컬럼 추가
df2['Avg'] = df2[['Test1', 'Test2', 'Test3', 'Final']].mean(axis=1)
# print(df2)

# 합계 컬럼 추가
df2['Sum'] = df2[['Test1', 'Test2', 'Test3', 'Final']].sum(axis=1)
print(df2)
