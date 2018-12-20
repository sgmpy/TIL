"""
난이도* 1. 지역(location)은 몇개 있나요? : list length
출력예시)
4

난이도** 2. python standard library에 'requests'가 있나요? : 접근 및 list in
출력예시)
false

난이도** 3. gm반의 반장의 이름을 출력하세요. : depth 있는 접근
출력예시)
엄윤주

난이도*** 4. ssafy에서 배우는 언어들을 출력하세요. : dictionary.keys() 반복
출력 예시)
python
web

난이도*** 5 ssafy gj반의 강사와 매니저의 이름을 출력하세요. dictionary.values() 반복
출력 예시)
change
pro-gj

난이도***** 6. framework들의 이름과 설명을 다음과 같이 출력하세요. : dictionary 반복 및 string interpolation
출력 예시)
flask는 micro이다.
django는 full-functioning이다.

난이도***** 7. 오늘 당번을 뽑기 위해 groups의 '4조'에서 한명을 랜덤으로 뽑아주세요. : depth 있는 접근 + list 가지고 와서 random.
출력 예시)
오늘의 당번은 하창언
"""

ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
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

# 1. 
ssafy['location'] #=> ['서울', '대전', '광주', '구미']
type(ssafy['location']) #=> list
print(len(ssafy['location'])) #=> 4

# 2.
library = ssafy['language']['python']['python standard library'] #=> ["os", "random", "webbrowser"]
# 'requests' in library #=> True / False
print('requests' in library)

# 3.
print(ssafy['classes']['gm']['class president']) #=> '엄윤주'

# 4. 
language = ssafy['language']
for key in language.keys(): #=> ['python', 'web']
    print(key)

# 5. 
gj = ssafy['classes']['gj']
for value in gj.values(): #=> ['change','pro-gj']
    print(value)

# 6. 
frameworks = ssafy['language']['python']['frameworks']
for key, value in frameworks.items(): #=> [('flask','micro'),('django','full-functioning')]
    # item #=> ('flask','micro')
    # key #=> 'flask', value #=> 'micro'
    print(f'{key}는 {value}이다.')

# 7.
import random
four = ssafy['classes']['gm']['groups']['4조'] #=> ["김교훈", "김유림", "송현우", "이현수", "진민재", "하창언"]
dang = random.choice(four)
print(dang)
'''
{
    "flask": "micro",
    "django": "full-functioning"
}
'''