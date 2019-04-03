import sys
sys.stdin = open("sangwon_party.txt", "r")

T = int(input())

def BFS(start):
    queue = [start]
    visited[start] = 1
    while queue:
        y = queue.pop(0)
        for x in range(1,N+1):
            if mymap[y][x] == 1 and not visited[x]:
                visited[x] = visited[y] + 1
                queue.append(x)
        # if visited[x] > 3:
        #     return

for t in range(1,T+1):
    N, M = map(int, input().split())
    data = [list(map(int,input().split())) for i in range(M)]
    count = 0
    # print(data)
    mymap = [[0]*(N+1) for i in range(N+1)]
    start = []
    visited = [0]*(N+1)
    # print(visited)
    for i in data:
        mymap[i[0]][i[1]] = 1
        mymap[i[1]][i[0]] = 1
        # if i[0] == 1:
        #     start.append(i)
        #     visited[i[0]][i[1]] = 1
    # print(mymap)
    BFS(1)
    # print(visited)
    for i in visited:
        if 0 < i <=3:
            count+=1

    if count == 0:
        print("#{} 0".format(t))
    else:
        print("#{} {}".format(t,count-1))
