# while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
# a = '*'
# count = 5
# star = 7
# while count > 0:
#     count  -= 1
#     print(f'{(a*star):^7}')
#     star -= 2

i = 0
while i < 4:
	i += 1
	print(('*' * (i * 2 - 1) + (' ' * (6 - i))))

#공백 문자 + 문자는 가운데? 이해가 안됨;

print((' '*5) + ('*'*1))
print((' '*4) + ('*'*3))
print((' '*3) + ('*'*5))
