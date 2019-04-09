import sys
sys.stdin = open("painting_4836.txt", "r")

T = int(input())
for t in range(1,T+1):
	N = int(input())
	data = [list(map(int,input().split())) for _ in range(N)]
	red_start = []
	red_end = []
	blue_start = []
	blue_end = []
	red_visited = [[0]*10 for _ in range(10)]
	blue_visited = [[0]*10 for _ in range(10)]
	for i in data:
		if i[-1] == 1:
			red_start.append([i[0],i[1]])
			red_end.append([i[2],i[3]])
		else:
			blue_start.append([i[0],i[1]])
			blue_end.append([i[2],i[3]])
	print(red_start)
	print(red_end)
	for i in range()

	count = 0
	for y in range(10):
		for x in range(10):
			if red_visited[y][x] ==1 and blue_visited[y][x] == 1:
				count+=1
	print("#{} {}".format(t,count))
