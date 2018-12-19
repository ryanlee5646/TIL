'''
문제 5.
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000
'''

# prices = input('물품 가격을 입력하세요: ')
# # 아래에 코드를 작성해 주세요. 
# prices = prices.split(';')  #1. split()을 이용하여 문자열을 쪼개줌
# int_prices = [] ## for문으로 돌린 결과값을 담아줄 리스트를 만들어  줌.
# for i in prices:  #2. 반복을 통한 item들을 int()를 이용하여 정수값으로 변환
#     int_prices.append(int(i))
# #  #3. .sort() or sorted()정렬
# int_prices.sort(reverse=True)
# print(int_prices)


prices = input('물품 가격을 입력하세요: ')
prices = prices.split(';')
list( map(int, prices) ) #=> [10, 2, 3]      ##reduce, select, map 비슷한 부류의 함수
#[int('10'), int('2), int('3')] #=> [10, 2, 3]
prices.sort(reverse=True)
print(prices)

