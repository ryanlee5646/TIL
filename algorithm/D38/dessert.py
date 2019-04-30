import sys
sys.stdin = open('dessert.txt','r')

def IsSafe(y,x):
    if 0<=y<N and 0<=x<N and visited[data[y][x]] != 1:
        return True
    else:
        return False

def DFS(y, x, count):
    global result
    if y == sy and x == sx and count > 3 :
        if count > result:
            result = count
            return

    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if IsSafe(ny,nx):
            visited[data[ny][nx]] = 1
            DFS(ny,nx, count+1)
            visited[data[ny][nx]] = 0


dy = [1, 1,-1,-1] # 좌, 우, 상, 상
dx = [-1, 1,1,-1] # 하, 하, 우, 좌

T = int(input())
for t in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * 101
    result = 0
    for y in range(N):
        for x in range(N):
            sy = y
            sx = x
            DFS(y,x,0)
            visited = [0] * 101
    if result < 4:
        print("#{} -1".format(t))
    else:
        print("#{} {}".format(t, result))