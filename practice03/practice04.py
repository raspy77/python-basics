# 구구단 중에 특정 곱셈을 만들고 그 답을 선택하는 프로그램을 작성하는 문제입니다.
# 답을 포함하여 9개의 정수가 아래와 같은 형태로 출력되고 사용자는 답을 골라 입력하게 됩니다.
# 프로그램은 정답 여부를 다시 출력합니다.


import random

a = random.randrange(1, 10)
b = random.randrange(1, 10)

print(a, 'X', b,'= ?')

for i in range(10):
    pass

c = int(input('answer:'))

if c == (a*b):
    print('정답')