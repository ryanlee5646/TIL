import sys
sys.stdin = open("best_distance.txt","r")
def cal(lst):       # list 를 인자로 받으며 회사 , 집까지 고려해 거리 반환
    tmp = starte + route + end
    tmpsum = 0
    for i in range(1, len(tmp)):
        tmpsum += (abs(tmp[i][0] - tmp[i - 1][0]) + abs(tmp[i][1] - tmp[i - 1][1]))
    return tmpsum
def Backtrack(start):
    global low
    if len(route) == N:     #개수가 N개이면 무조건 계산
        tmpresult = cal(route)
        if tmpresult <low:
            low = tmpresult
        return
    if len(route) >= 1 and low != 987654321:    #초기값이 9876...이 아니면(계산이 한번됬으면)계산
        tmpresult = cal(route)
        if tmpresult>=low:      #중간 계산 결과가 결과 값보다 크면 리턴 후속작업 안함
            return
    for i in range(len(people)):
        if not visited[i]:
            visited[i] = 1
            route.append(people[i])
            Backtrack(start+1)
            visited[i] = 0
            route.pop()
T = int(input())
# 회사, 집, N명의 고객
# 0 0 100 100 70 40 30 10 10 5 90 70 50 20
for t in range(1,T+1):
    N = int(input())
    data = list(map(int, input().split()))
    people = []  #고객 좌표
    route = []
    starte = [[data[0],data[1]]]
    end = [[data[2],data[3]]]
    visited = [0] * N
    low = 987654321
     #이동경로를 담을 리스트
    for i in range(4,(N+2)*2,2):
        people.append([data[i],data[i+1]])


    Backtrack(0)
    print("#{} {}".format(t,low))


# T = int(input())
#
#     # 회사, 집, N명의 고객
#     # 0 0 100 100 70 40 30 10 10 5 90 70 50 20
#
# def DFS(here, r):
#     if len(result) == r:
#         start_end.append(result[:])
#         return
#     for i in range(1, len(road)):
#         if not visited[i]:
#             visited[i] = 1
#             result.append(road[i])
#             DFS(here + 1, r)
#             visited[i] = 0
#             result.pop()
#
# for t in range(1, T + 1):
#     people = int(input())
#     position = list(map(int, input().split()))
#     road = []  # 중간에 들려야할 고객 좌표
#     company = []  # 회사 좌표
#     home = []  #
#     start_end = []
#     visited = [0] * people
#     low = 12359129
#     for i in range(0, people * 2 + 4, 2):
#         road.append([position[i], position[i + 1]])  # 고객 좌표를 road 변수에 저장
#     company.append(road.pop(0))  # 첫번째 회사 좌표를 company 변수에 저장
#     home.append(road.pop(0))  # 마지막 집 좌표를 home 변수에 저장
#     result = []
#
#     print("company: {}".format(company))
#     print("people: {}".format(road))
#     print("home: {}".format(home))
#     DFS(0, len(road))
#
#     for j in range(len(start_end)):
#         start_end[j].insert(0, company[0])
#         start_end[j].append(home[0])
#
#     for y in range(0,len(start_end)):
#         temp_x = 0
#         temp_y = 0
#         temp_distance = 0
#         for x in range(1,len(start_end[0])):
#             temp_x += abs(start_end[y][x-1][0] - start_end[y][x][0])
#             temp_y += abs(start_end[y][x-1][1] - start_end[y][x][1])
#         temp_distance += temp_x + temp_y
#         print(temp_distance)
#         print(low)
#         if low > temp_distance:
#             low = temp_distance
#     print("#{} {}".format(t,low))




