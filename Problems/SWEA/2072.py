# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

# result = []
# num = []
# evens = 0
# T = int(input())
# for i in range(T):
#     num = list(map(int, input().split()))
#     for even in num:
#         if even % 2 == 1:
#             evens += even    
#     result.append(evens)
#     evens = 0
# for j, n in enumerate(result):
#     print(f'#{j+1} {n}')


num = []
evens = 0
T = int(input())
for i in range(T):
    num = list(map(int, input().split()))
    for even in num:
        if even % 2 == 1:
            evens += even    
    print(f'#{i+1} {evens}')
    evens = 0
