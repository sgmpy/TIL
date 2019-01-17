import random as ra

name=[('권령경',1), ('김영훈',1), ('조현진',1), ('조영현',1), ('김유림',1),
('김미진',2), ('송현우',2), ('신인택',2), ('서민수',2), ('엄윤주',2),
('강현구',3), ('여성우',3), ('양도혁',3), ('하창언',3), ('박재휘',3),
('이지현',4), ('서민호',4), ('진민재',4), ('이현수',4), ('권민재',4),
('김교훈',5), ('박재형',5), ('윤종원',5), ('강대현',5), ('이규진',5)]


bools=True
while bools:
    count=1
    ra.shuffle(name)
    for i,j in enumerate(name):
        if j[1] == i//5+1:
            count=0
            break     
    if count:
        bools=False

print("앞문")
for k,l in enumerate(name):
    print(f'{l[0]} ', end="")
    if (k+1)%5==0:
        print("")
print("뒷문")