import random
students = [
        '강대현','강현구','권령경','권민재','김교훈',
        '김미진','김영훈','김유림','박재휘','서민수',
        '서민호','송현우','신인택','양도혁','엄윤주',
        '윤종원','이규진','이지현','이현수','조영현',
        '조현진','진민재','하창언',
]
print('앞문')
random.shuffle(students)
for index, student in enumerate(students,start=1):
    print(f'{student:5}',end='')
    if index % 5 == 0:
        print()

print('\n뒷문')

