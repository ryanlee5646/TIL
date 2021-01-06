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
