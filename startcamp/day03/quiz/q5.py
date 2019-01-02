'''
문제 5.
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000
'''

prices = input('물품 가격을 입력하세요: ')
# 아래에 코드를 작성해 주세요.

# input : 10;2;3
# 1. .split() 이용
prices = prices.split(';') #=> ['10','2','3']

# 2. 반복을 통한 item들 int() 이용
int_price = [] # or list()
for i in prices: #=> ['10','2','3']
    int_price.append(int(i)) #=> [10, 2, 3]

int_price = list( map(int, prices) ) #=> [10, 2, 3]
# [int('10'), int('2'), int('3')] #=> [10, 2, 3]
# reduce, select, map

# 3. .sort() / sorted() 정렬
# int_price.sort(reverse=True) #=> [10, 3, 2]

# 3-1. .reverse() / reversed() 뒤집기
# int_price.reverse() #=> [10, 3, 2]

# 3-2. sorted() [+ reversed()]
sorted_price = sorted(int_price, reverse=True) #=> [10, 3, 2]

# 3-3. ?
# prices = ['10','2','3']
sorted_price = sorted(list( map(int, prices) ),reverse=True) #=> [10, 3, 2]

# 4. 출력
for i in sorted_price:
    print(i)
    # 10
    # 3
    # 2
