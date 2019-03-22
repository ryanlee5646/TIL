import sys
sys.stdin = open("best_distance.txt","r")

T = int(input())
#회사, 집, N명의 고객
for t in range(1,T+1):
    people = int(input())
    position = list(map(int, input().split()))
    road = []

    for i in range(0,people+2,2):
        road.append([position[i],position[i+1]])
    print(road)