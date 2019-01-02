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
# print(lunch['중국집']) #=> '02-123-123'
idol = {
    'bts': {
        '지민':24,
        'RM': 25
    }
}
idol['bts'] #=> { '지민':24, 'RM':25 }
idol['bts']['RM'] #=> 25

# 4. 딕셔너리 반복문 활용하기
# 기본 활용
for key in lunch:
    print(key) #=> key
    print(lunch[key]) #=> value

# key만 가져오기 : .keys()
for key in lunch.keys():
    print(key)

# value만 가져오기 : .values()
for value in lunch.values():
    print(value)

# item (key, value) 가져오기 : .items()
# lunch.items() #=> [('중식','02'), ... ]
for key, value in lunch.items():
    print(key, value)

# 2개 = 자료형(list, tuple ...) 길이 2
a, b, c = (1, 2, 3)
print(a)
print(b)



# 문제
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}
# 1. 이 학생의 평균을 구하시오.
# 풀이 1
total_score = 0 # 270
for subject_score in score.values():
    total_score += subject_score

avg_score = total_score / len(score) #=> 270 / 3
print(avg_score)

# 풀이 2
total_score = sum(score.values()) #=> sum([80, 90, 100]) => 270
avg_score = total_score / len(score) #=> 270 / 3
print(avg_score)

# 2. 반 평균을 구하시오.

scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 70
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}


total_score = 0 #=> 80 + 90 + 70 + 80 + 90 + 100
count = 0 #=> 1 + 1 + 1 + 1 + 1 + 1

for person_score in scores.values(): #=> [{'수학': 80,'국어': 90,'음악': 70}, {'수학': 80,'국어': 90,'음악': 100}]
    # 2번째 시행
    # print(person_score) #=> {'수학': 80,'국어': 90,'음악': 100}
    # person_score.values() #=> [80, 90, 100]
    for subject_score in person_score.values():
        # 3번째 시행
        # subject_score #=> 100
        total_score += subject_score
        count += 1

avg_score = total_score / count
print(avg_score)


# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 6],
    '대전': [-3, -6, 2],
    '광주': [-0, -2, 10],
    '구미': [2, -2, 9]
}
# 3-1. 도시별 최근 3일의 온도 평균은?
'''
출력 예시)
서울 : 값
대전 : 값
광주 : 값
구미 : 값
'''

# city.items() #=> [('서울',[-6, -10, 6]), ( ... ), ...]
for name, temp in city.items():
    # name #=> '서울'
    # temp #=> [-6, -10, 6]
    # 1. 반복
    total_temp = 0 #=> -10
    count = 0
    for t in temp:
        # 1번째 시행
        # t #=> -6
        total_temp += t
        count += 1
    avg_temp = total_temp / count #=> -10 / 3

    # 2. 내장 함수
    avg_temp = sum(temp) / len(temp) #=> -10 / 3
    print(f'{name} : {avg_temp}')