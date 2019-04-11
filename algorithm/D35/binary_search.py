import sys
sys.stdin = open("binary_search.txt", "r")

def binary(end,l,r,count):
	global temp
	center = int((l + r)/2)

	if center == end:
		return count

	elif center < end:
		l = center
		return binary(end,l,r,count+1)

	elif center > end:
		l = 1
		r = center
		return binary(end,l,r,count+1)


T = int(input())
for t in range(1,T+1):
	right,A,B = map(int, input().split())
	temp = 0
	count_a = binary(A,1,right,0)
	count_b = binary(B,1,right,0)
	if count_a > count_b:
		print(count_a)
		print(count_b)
		print("#{} B".format(t))
	elif count_a == count_b:
		print(count_a)
		print(count_b)
		print("#{} 0".format(t))
	else:
		print(count_a)
		print(count_b)
		print("#{} A".format(t))