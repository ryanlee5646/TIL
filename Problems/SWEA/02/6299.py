# 리스트 내포 기능을 이용해 [5, 6, 77, 45, 22, 12, 24]에서 짝수를 제거한 후 리스트를
# 출력하는 프로그램을 작성하십시오.

a = [5, 6, 77, 45, 22, 12, 24]
# b = []
# for i in a:
#     if i % 2:
#         b.append(i)
# print(b)
for i in a[:]:
    if i % 2 == 0:
        a.remove(i)
print(a)

