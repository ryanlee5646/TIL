# A와 B가 가위바위보를 하였다. 
# 가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.
# A와 B중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.

# [입력]
# 입력으로 A와 B가 무엇을 냈는지 빈 칸을 사이로 주어진다.
# [출력]
# A가 이기면 A, B가 이기면 B를 출력한다.

# a, b = map(int,input().split())
# if a > b :
#     print('A')
# elif a == b:
#     pass
# else: 
#     print('B')

win = ['3 2', '3 1', '2 1']
if map(int,input().split()) in win:
    print('A')
else:
    print('B')
