# 다음은 학생의 점수를 나타내는 리스트입니다.
# [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
# while 문과 리스트 객체의 pop()을 이용해 80점 이상의 점수들의 총합을 구하시오.
score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
count = 0
sum_score = 0
while count < 10:  
    if score[-1] < 80:
        score.pop() 
    count += 1
print(sum_score)
    