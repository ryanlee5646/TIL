import sys
sys.stdin = open("lab.txt","r")

def IsSafe(y,x):
	if 0<=y<N and 0<=x<N:
		for i in start:
			if y!=i[0] and x !=i[1]:
				return True
	else:
		return False

def BFS(start):
	queue = start
	while queue:
		y,x = queue.pop(0)
		print(y)
		print(x)



dy = [-1,1,0,0]
dx = [0,0,-1,1]

T = int(input()) # 백준에는 해당 X

for t in range(1,T+1):
	N,M = map(int,input().split())
	data = [list(map(int,input().split())) for _ in range(N)]
	print(data)
	start = []
	visited = [[987654321]*N for _ in range(N)]

	for y in range(N):
		for x in range(N):
			if data[y][x] == 2:
				visited[y][x] = 0
				start.append([y,x])
	print(start)
	for i in start:
		BFS(i)

