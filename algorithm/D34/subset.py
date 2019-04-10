import sys
sys.stdin = open("subset.txt", "r")

def combination(index,combi,N):
	if len(combi) == N:
		print(combi)
		return
	if index > len(data):
		return
	combination(index+1,combi+[data[index]],N)
	combination(index,combi,N)



T = int(input())
data = [i for i in range(1,13)]
print(data)
for t in range(1,T+1):
	N, K = map(int,input().split())
	combination(0,[],N)
