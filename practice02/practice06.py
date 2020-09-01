

import random

mi, ma = 1,100
n = random.randrange(ma)+mi


while True:
    print('수를 결정하였습니다. 맞추어보세요')

    while True:
        s = int(input('>>'))
        if s == n:
            print('맞았습니다.')
            break
        elif n < s:
           print('더낮게')
        else:
            print('더높게')

    a = input('다시 하시겠습니까?(y/n)')
    if a == 'n':
        break