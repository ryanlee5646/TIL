import sys
sys.stdin = open('dessert.txt','r')

def IsSafe(y,x):
    if 0<=y<N and 0<=x<N:
        return True
    else:
        return False

dy = [1, 1,-1,-1]
dx = [-1, 1,1,-1]

T = int(input())
for t in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    print(data)
