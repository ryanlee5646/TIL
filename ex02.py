# #for문 활용 1
# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks:
#     number += 1
#     if mark >= 60:
#         print(f"{number}번 학생은 {mark}점으로 합격입니다.")
#     else:
#         print(f"{number}번 학생은 {mark}점으로  불합격입니다.")


# #for문에서 range() 함수 활용
# sum = 0
# for i in range(1, 11):
#     sum += i
# print(sum)

# #range()와 for문 응용
# marks = [90, 25, 67, 45, 80]
# number = 1
# for number in range(len(marks)):
#     if marks[number] >= 60:
#         print(f"{number+1}번님은 합격입니다.")
#     else:
#         print(f"{number+1}번님은 불합격입니다")
       
#for문과 range()함수를 활용한 구구단
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f"{i}*{j} = {i*j}")
    
class Service:
        secret = "영구는 배꼽이 두 개다."
pey  = Service()
pey.secret