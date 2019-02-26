import sys
sys.stdin = open("4875_미로.txt", "r")

def IsSafe(y,x):
    if x>=0 and x<N and y>=0 and y<N:
        return True
def IsPossible(y,x):
    if data[y][x] != 1:
        return True
def IsNotVisited(y,x):
    if data[y][x] != -1:
        return True

def DFS(y,x):
    global result
    if data[y][x] == 3:
        data[y][x] = -1
        result = 1
        return
    else:
        if data[Start_y][Start_x] == 0:
            for y in

T = int(input())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
result = 0
for t in range(1, T+1):
    N = int(input())
    data = []
    for i in range(N):
        data.append(list(map(int, input())))
    for y in range(N):
        for x in range(N):
            if data[y][x] == 2:
                Start_y = y
                Start_x = x

print(data)
