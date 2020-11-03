import sys
sys.stdin = open("maxNum.txt", "r")

T = int(input())

max_list = []

for i in range(T):
    num = list(map(int, input().split()))
    print("num: " , num)
    max_list.append(max(num))
    print("max_list: " , max_list)

for j, k in enumerate(max_list):
    print(f'#{j+1} {k}')

print(max_list[1])

'''
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1
'''
