'''
문제 2.
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

n = int(input('숫자를 입력하세요: '))
# 아래에 코드를 작성해 주세요.

# 1.
i = 0
while i < 5:
    print(i+1)
    i += 1

# 2.
# n = 5
for i in range(n):
    print(i+1)

# 3.
for i in range(1,n+1):
    print(i)

# int('123') <=> str(123) #=> '123'