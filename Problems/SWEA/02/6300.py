# 리스트 내포 기능을 이용해 [12, 24, 35, 70, 88, 120, 155]에서
# 홀수번째 항목을 제거한 후 리스트를 출력하는 프로그램을 작성하십시오.

a = [12, 24, 35, 70, 88, 120, 155]
b = []
for i, j in enumerate(a):
    if i % 2 == 1:
        b.append(j)
print(b)