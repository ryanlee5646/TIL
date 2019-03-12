import sys
sys.stdin = open("Sudoku.txt","r")


T = int(input())
for t in range(1,T+1):
    data = []
    for i in range(9):
        data.append(list(map(int,input().split())))

    for y in range(9):
        visited_x = [1]+[0]*9
        visited_y = [1]+[0]*9
        flag = True
        for x in range(9):
            visited_x[data[y][x]] = 1
            visited_y[data[x][y]] = 1
            for z in range(1,10):
                if(visited_x[z] != 1) or (visited_y[z]!= 1):
                    flag = False
                    break
    if flag:
        print("#{} 1".format(t))
    else:
        print("#{} 0".format(t))
