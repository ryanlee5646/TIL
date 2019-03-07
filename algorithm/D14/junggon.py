import sys
sys.stdin = open("junggon.txt", "r")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    num_list1 = list(map(int, input().split()))
    num_list2 = num_list1
    danjo = []
    result = []
    for i in num_list1:
        for j in num_list2:
            if i != j :
                danjo.append(i*j)
    for j in danjo:
        if j not in result and j >10 and j%10 != 0:
            result.append(j)
    for k in 


    print("#{} {}".format(t,max(result)))
