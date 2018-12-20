# 1. 딕셔너리 만들기
lunch = {
    '중국집':'02-123-123',
    '양식집':'054-123-123',
    '한식집':'031-123-123'
}

dinner = dict(중국집='02-123-123')

# 2. 딕셔너리에 내용 추가하기
lunch['분식집'] = '053-123-123'

# 3. 딕셔너리 내용 가져오기
idol= {
    'bts': {
        '지민':24,
        'RM':25
    }
}
print(idol['bts']) #=>{'지민':24, 'RM':25}
print(idol['bts']['RM']) #=> 25
print(lunch['중국집']) #=> '02-123-123'

print(lunch)

# 4. 딕셔너리 반복문 활용하기
# 기본 활용
for key in lunch:
    print(key)
    print(lunch[key]) #=> value
# key만 가져오기 : .keys()
for key in lunch.keys():
    print(key)    

# value만 가져오기 : .values()
for value in lunch.values():
    print(value) 

# item (key, value) 가져오기 : .items()
# lunch.items() #=> [('중식', '02'), ...]
for item in lunch.items():
    print(item)    # 튜플의 형태로 출력됨
for key, value in lunch.items():
    print(key, value)  #튜플이 아닌 형태로 출력됨

#2개 = 자료형(list, tuple ...) 길이 2
a, b, c = (1, 2, 3)
print(a)
print(b)      

# 문제1.이 학생의 평균을 구하시오.
#풀이 1
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}
total_score = 0
for subject_score in score.values():
    total_score += subject_score
avg = total_score/ len(score)
print(avg)
#풀이 2
total_score = sum(score.values()) #=> sum([80, 90, 100]) => 270

# 문제2. 반평균을 구하시오


scores ={
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100   
    },
    'c': {
        '수학': 90,
        '국어': 75 ,
        '음악': 85
    }
}
# #방법 1
total_score = 0
total_lenth = 0
for students in scores: # students에는 scores의 key값이 들어가있다.
    for student_total in scores[students]:
        total_score += scores[students][student_total]
        total_lenth+=1
print(total_score/total_lenth)        
        
#방법 2
total_score = 0
count = 0 
for person_score in scores.values(): #=> [{'수학':80,'국어':75,'음악':85}, {'수학':80,'국어':75,'음악':85}, {'수학':80,'국어':75,'음악':85}]       
  # person_score #=> {'수학':80,'국어':90,'음악':70}
  # person_score.values() #=> [80, 90, 70]
    for subject_score in person_score.values():
        # 1번째 시행
        # subject_score #=> 80  
        total_score += subject_score
        count += 1
print(total_score/count)        

# 문제 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 6],
    '대전': [-3, -6, 2],
    '광주': [0, -2, 10],
    '구미': [2, -2, 9]
}
# 3-1. 도시별 최근 3일의 온도 평균은?
'''
출력 예시)
서울: 값
대전: 값
광주: 값
구미: 값
'''
#풀이 1
for city_name, city_temp in city.items():
    total_temp = 0
    for city_sum in city_temp:
        total_temp += city_sum
    city_avg = total_temp/len(city_temp)
    print(f"{city_name}: {round(city_avg,2)}")
#풀이 2
for city_name, city_temp in city.items():
    city_avg = sum(city_temp) / len(city_temp)
    print(f"{city_name} : {round(city_avg,1)}")
        
max_temp = 0
for name, temp in city.items():
    for t in temp:
        if t > max_temp:
            max_temp = t
            max_city = name
print(max_city, max_temp)            






