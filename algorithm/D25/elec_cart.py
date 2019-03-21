import sys
sys.stdin = open("elec_cart.txt", "r")

def DFS(here):
    global temp, min_use
    if 0 not in visited:
        temp += data[here][0]
        if min_use >= temp:
            min_use = temp
        temp-=data[here][0]
        return

    if min_use < temp:
        return

    for i in range(1,N):
        if not visited[i]:
            visited[i] = 1
            next = i
            temp += data[here][next]
            DFS(next)
            visited[i] = 0
            temp -= data[here][next]

T= int(input())
for t in range(1, T+1):
    N = int(input())
    data = []
    visited = [0]*N
    visited[0]=1
    temp = 0
    min_use = 21442336
    for i in range(N):
        data.append(list(map(int,input().split())))

    DFS(0)
    print("#{} {}".format(t,min_use))
