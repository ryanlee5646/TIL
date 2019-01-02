#두 개의 정수 n과 m이 주어집니다. 반복문을 사용하지 않고 별(*) 문자를 이용해 가로
#의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.
n = 5
m = 9
print((f'*'*n+'\n')*m)



#다음 딕셔너리에서 평균 점수를 출력하시오.
student = {'python':80, 'algorithm':99, 'django':89, 'flask':83}
total = sum(student.values())
average = total / len(student)
print(f"평균점수: {average}")

#다음은 학생들의 혈액형(A, B, AB, O)에 대한 데이터이다. for문을 이용하여 각 혈액형
#별 학생수의 합계를 구하시오.
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
result = {}
for blood_type in blood_types:
    if blood_type in result:
        result[blood_type] += 1
    else:
        result[blood_type] = 1
print(result)        


# blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
# bt_a = 0
# bt_b = 0
# bt_o = 0
# bt_ab = 0
# for i in blood_types:
#     if i == 'A':
#         bt_a += 1
#     elif i == 'B':
#         bt_b += 1
#     elif i == 'O':
#         bt_o += 1
#     else:
#         bt_ab += 1   
# print(f"""A형:{bt_a}명, B형:{bt_b}명, O형:{bt_o}명, AB형:{bt_ab}명""")

blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

print(f"""
A형:{blood_types.count('A')}명, B형:{blood_types.count('B')}명, 
O형:{blood_types.count('O')}명, AB형:{blood_types.count('AB')}명
""")

