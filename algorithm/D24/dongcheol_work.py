import sys
sys.stdin = open("dongcheol_work.txt", "r")

def Back(y,temp):
    global max_num
    # count = 1
    # for i in permutation:
    #     count = count * i
    #     if count > max_num:
    #         return

    if len(permutation) == N:
        if  max_num == 1 or temp > max_num:
            max_num = temp
        return

    for x in range(N):
            if not visited[x]:
                visited[x] = 1
                count = 1
                temp = count*data[y][x]
                Back(y+1,temp)
                visited[x] = 0
                permutation.pop()

T = int(input())
for t in range(1,T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    permutation = []
    max_num = 1
    print(data)
    Back(0,0)
    print("#{} {}".format(t, round(max_num*100, 6)))