#방법 1 csv사용하는 방법
import csv
with open('home.csv','r',encoding='utf8',) as f:
    lines = f.readlines()
    for line in lines:
    # items = csv.reader(f)
        print(line.strip().split(',')) 
        #stirp()은 print()가 기본으로 가지고 있는 개행문자(\n)를 제거해줌
        #split은 딕셔너리를 분리해줌.

#방법 2 csv사용하지 않는 방법
#         import csv
# with open('home.csv','r',encoding='utf8',) as f:
#     lines = f.readlines()
#     for items in itemss:
#         print(line.strip().split(',')) 
#         #stirp()은 print()가 기본으로 가지고 있는 개행문자(\n)를 제거해줌
#         #split은 딕셔너리를 분리해줌.