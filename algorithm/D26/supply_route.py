import sys
sys.stdin = open("supply_route.txt", "r")


def IsSafe(y,x,N):
    if y>=0 and y<N and x>=0 and x<N:
        return True
    else:
        return False
def Back(y,x):
    global low
    if y == end_y and x == end_x:
        low = temp[y][x]
        print("******low:{}".format(low))
        return

    for i in range(4):
        if IsSafe(y+dy[i], x+dx[i], N):
            if temp[y][x] + route[y+dy[i]][x+dx[i]] < temp[y+dy[i]][x+dx[i]]:
                print("temp:")
                for j in temp:
                    print(j)
                print("route:{}".format(route))
                temp[y+dy[i]][x+dx[i]] = temp[y][x] + route[y+dy[i]][x+dx[i]]
                if temp[y+dy[i]][x+dx[i]] > low:
                    return
                else:
                    Back(y+dy[i],x+dx[i])

T = int(input())
for t in range(1,T+1):
    N = int(input())
    route = [list(map(int,input())) for i in range(N)]

    dy=[0,1,0,-1] # 하우상좌
    dx=[1,0,-1,0]

    low = 987654321
    end_y = end_x = N-1
    temp = [[987654321]*N for _ in range(N)]
    temp[0][0] = 0


    Back(0,0)
    print("#{} {}".format(t, low))
