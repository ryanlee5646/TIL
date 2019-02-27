import sys
sys.stdin = open("5099_pizza.txt", "r")

T = int(input())

for t in range(1,T+1):
    oven, pizza = map(int, input().split())
    cheese = list(map(int, input().split()))
    num_cheese = []
    pizza_list = []
    for i in range(1, pizza+1):
        pizza_list.append(i)
    print(pizza_list)
    pizza_cheese = list(map(list, zip(pizza_list, cheese)))
    print(pizza_cheese)

    for i in range(12312):
        if pizza_cheese[1] == 0:

    # 한번 돌릴때마다 첫번째 인덱스에 오는 피자의 치즈가 0인지 확인
    #아니면 계속 회전시키고 화덕 개수만큼 돌렷을때 //2 해주기
