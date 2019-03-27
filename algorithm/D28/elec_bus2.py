import sys
sys.stdin = open("elec_bus2.txt","r")

def Back(here,):
    global count





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


