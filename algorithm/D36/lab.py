import sys, itertools
sys.stdin = open("lab.txt","r")

def IsSafe(y,x):
	if 0<=y<N and 0<=x<N and data[y][x] != 1:
		return True
	else:
		return False

def BFS(start):
	global count
	for i in start:
		visited[i[0]][i[1]] = 1
	queue = start
	while queue:
		y,x = queue.pop(0)
		for i in range(4):
			newy = y+dy[i]
			newx = x+dx[i]
			if IsSafe(newy,newx):
				if visited[y][x] + 1 < visited[newy][newx]:
					visited[newy][newx] = visited[y][x] + 1
					count = visited[y][x] + 1
					queue.append([newy,newx])

dy = [-1,1,0,0]
dx = [0,0,-1,1]

T = int(input()) # 백준에는 해당 X

for t in range(1,T+1):
	N,M = map(int,input().split())
	data = [list(map(int,input().split())) for _ in range(N)]
	print(data)
	start = []
	visited = [[987654321]*N for _ in range(N)]
	count = 987654321
	result = []
	for y in range(N):
		for x in range(N):
			if data[y][x] == 2: # 맵에서 2인경우 출발지점
				start.append([y,x])
	combination = list(itertools.combinations(start, M))

	for i in combination:
		visited = [[987654321] * N for _ in range(N)]
		BFS(list(i))
		for i in visited:
			print(*i)
		print()
		temp1 = 0
		for y1 in range(N):
			temp2 = 0
			for x1 in range(N):
				if data[y1][x1] == 0 and visited[y1][x1] == 987654321:
					print("#{} -1".format(t))
				elif visited[y1][x1] != 987654321 and visited[y1][x1] > temp2:
					temp2 = visited[y1][x1]
					if temp1 < temp2:
						temp1 = temp2
		if temp1 < count:
			count =temp1
		result.append(count)
	print("#{} {}".format(t,min(result)-1))
