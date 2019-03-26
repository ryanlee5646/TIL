import sys
sys.stdin = open("elec_bus2.txt","r")

T = int(input())
for t in range(1,T+1):
    charge = list(map(int,input().split()))
    N = charge.pop(0)
    print(charge)
    print(N)
    count = 0
    visited = [0]*(N-1)
    print(visited)
    charge_num = 0
    while True:
        for i in range(charge):
            if not visited[i]:
                visited[i] = 1
                charge_num = charge[i]
                
