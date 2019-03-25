import sys
sys.stdin = open("best_distance.txt","r")

# T = int(input())
# # 회사, 집, N명의 고객
# # 0 0 100 100 70 40 30 10 10 5 90 70 50 20
#
# def DFS(here, r):
#     global low
#     if len(result) == r:
#         start_end.append(result[:])
#         # if low > temp_distance:
#         #     low = temp_distance
#         # print(result)
#         return
#     for i in range(1, len(road)):
#         if not visited[i]:
#             visited[i] = 1
#             result.append(road[i])
#             print(result)
#             temp_x = 0
#             temp_y = 0
#             temp_distance = 0
#             # for y in range(1,len(result)):
#             #         temp_x += abs(result[y-1][0] - result[y][0])
#             #         temp_y += abs(result[y-1][1] - result[y][1])
#             #     temp_distance += temp_x + temp_y
#             DFS(here+1,r)
#             visited[i] = 0
#             result.pop()
#
# for t in range(1,T+1):
#     people = int(input())
#     position = list(map(int, input().split()))
#     road = [] # 중간에 들려야할 고객 좌표
#     company = [] # 회사 좌표
#     home = [] #
#     start_end = []
#     temp = []
#     visited = [1]+[0]*people
#     low = 12359129
#     for i in range(0,people*2+4,2):
#         road.append([position[i],position[i+1]]) # 고객 좌표를 road 변수에 저장
#     company.append(road.pop(0)) # 첫번째 회사 좌표를 company 변수에 저장
#     home.append(road.pop(0)) # 마지막 집 좌표를 home 변수에 저장
#     result = [company[0]]
#     # print("company: {}".format(company))
#     # print("people: {}".format(road))
#     # print("home: {}".format(home))
#     DFS(0,len(road)+1)
#
#     for j in range(len(start_end)):
#         start_end[j].insert(0,company[0])
#         start_end[j].append(home[0])
#     # print(start_end[0])
#     # print(start_end[0][0])
#     # print(start_end[0][0][0])
#     # print(len(start_end[0]))
#
#     # for y in range(0,len(start_end)):
#     #     temp_x = 0
#     #     temp_y = 0
#     #     temp_distance = 0
#     #     for x in range(1,len(start_end[0])):
#     #         temp_x += abs(start_end[y][x-1][0] - start_end[y][x][0])
#     #         temp_y += abs(start_end[y][x-1][1] - start_end[y][x][1])
#     #     temp_distance += temp_x + temp_y
#     #     # print(low)
#     #     if low > temp_distance:
#     #         low = temp_distance
#     # print("#{} {}".format(t,low))




T = int(input())

    # 회사, 집, N명의 고객
    # 0 0 100 100 70 40 30 10 10 5 90 70 50 20

def DFS(here, r):
    if len(result) == r:
        start_end.append(result[:])
        return
    for i in range(1, len(road)):
        if not visited[i]:
            visited[i] = 1
            result.append(road[i])
            DFS(here + 1, r)
            visited[i] = 0
            result.pop()

for t in range(1, T + 1):
    people = int(input())
    position = list(map(int, input().split()))
    road = []  # 중간에 들려야할 고객 좌표
    company = []  # 회사 좌표
    home = []  #
    start_end = []
    temp = []
    visited = [0] * people
    low = 12359129
    for i in range(0, people * 2 + 4, 2):
        road.append([position[i], position[i + 1]])  # 고객 좌표를 road 변수에 저장
    company.append(road.pop(0))  # 첫번째 회사 좌표를 company 변수에 저장
    home.append(road.pop(0))  # 마지막 집 좌표를 home 변수에 저장
    result = []

    print("company: {}".format(company))
    print("people: {}".format(road))
    print("home: {}".format(home))
    DFS(0, len(road))

    for j in range(len(start_end)):
        start_end[j].insert(0, company[0])
        start_end[j].append(home[0])

    for y in range(0,len(start_end)):
        temp_x = 0
        temp_y = 0
        temp_distance = 0
        for x in range(1,len(start_end[0])):
            temp_x += abs(start_end[y][x-1][0] - start_end[y][x][0])
            temp_y += abs(start_end[y][x-1][1] - start_end[y][x][1])
        temp_distance += temp_x + temp_y
        print(temp_distance)
        print(low)
        if low > temp_distance:
            low = temp_distance
    print("#{} {}".format(t,low))




