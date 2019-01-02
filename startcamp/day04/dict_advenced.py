
"""



난이도***** 7. 오늘 당번을 뽑기 위해 groups의 4조 중에 한명을 랜덤으로 뽑아주세요. : depth 있는 접근 + list 가지고 와서 random.
출력예시)
오늘의 당번은 하창언
"""

ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser","request"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gm":  {
            "lecturer": "junwoo",
            "manager": "pro-gm",
            "class president": "엄윤주",
            "groups": {
                "1조": ["강대현", "권민재", "서민수", "이규진"],
                "2조": ["박재형", "서민호", "윤종원", "이지현"],
                "3조": ["김미진", "김영훈", "엄윤주", "여성우"],
                "4조": ["김교훈", "김유림", "송현우", "이현수", "진민재", "하창언"],
            }
        },
        "gj": {
            "lecturer": "change",
            "manager": "pro-gj"
        }
    }
}
'''난이도* 1. 지역(location)은 몇개 있나요? : list length
# 출력예시)
# 4'''
print(len(ssafy["location"]))

'''난이도** 2. python standard library에 'requests'가 있나요? : 접근 및 list in
# 출력예시)
# false'''
for key in ssafy["language"]["python"]["python standard library"]:
    if key == "request":
       key = True
    else:
        key = False
print(key) 

'''난이도** 3. gm반의 반장의 이름을 출력하세요. : depth 있는 접근
 출력예시) 엄윤주'''
print(ssafy["classes"]["gm"]["class president"])

'''#난이도*** 4. ssafy에서 배우는 언어들을 출력하세요. : dictionary.keys() 반복
# 출력 예시)
# python
# web'''
# //for key in ssafy["language"]:
#     print(key)    
#//language = ssafy["language"].keys()
# for key in language:
#     print(key)

'''# 난이도*** 5 ssafy gj반의 강사와 매니저의 이름을 출력하세요. dictionary.values() 반복
# 출력 예시)'''
# change
# pro-gj
for name in ssafy["classes"]["gj"].values():
    print(name)

'''# 난이도***** 6. framework들의 이름과 설명을 다음과 같이 출력하세요. : dictionary 반복 및 string interpolation
# 출력 예시)
# flask는 micro이다.
# django는 full-functioning이다.'''
for key,value in ssafy["language"]["python"]["frameworks"].items():
    print(f"{key}는 {value}이다.")


'''# 난이도***** 7. 오늘 당번을 뽑기 위해 groups의 4조 중에 한명을 랜덤으로 뽑아주세요. : depth 있는 접근 + list 가지고 와서 random.
# 출력예시)
# 오늘의 당번은 하창언'''
import random
gr = random.choice(ssafy["classes"]["gm"]["groups"]["1조"])
print(f"오늘 저녁은 {gr}이/가 쏩니다.")
