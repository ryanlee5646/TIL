import sys
sys.stdin = open("elec_bus2.txt","r")

# 처음 출발점에서 끝까지 갓을때 횟수를 기본값으로 해주고
# 출발점에서 갈수있는 최대거리에서 뒤로 한칸씩 이동했을때 갈수있는 최대횟수랑 비교해줌(While문으로 재귀 사용)
# 가장 밖에 있는 재귀 함수는 최대 충전횟수만큼 인덱스를 추가해줌

def Back(here, remain, count):
    # here+1, charge[here+1], c
    # here+1, h-1, c



T = int(input())
for t in range(1,T+1):
    charge = list(map(int,input().split())) #충전소
    N = charge.pop(0) # 충전소 횟수 here이 N이되면 종료
    print(charge)
    print(N)
    low = 987654321 # 충전 횟수
    temp = 0
    charge_num = 0 # 충전 잔량
    # visited = [0]*(N-1)
    # print(visited)
    Back(0)


