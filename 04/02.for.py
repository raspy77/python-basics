# for ~반복문
# for o in [sequnce 객체] :
for number in [10, 20, 30, 40]:
    result = number**2
    print(result, end=' ')
else:
    print('')


a = ['cat', 'cow', 'tiger']
for animal in a:
    print(animal, end=' ')
else:
    print('')

l = [('둘리', 10), ('마이콜', 30), ('또치', 11)]
for t in l:
    print('이름: %s, 나이:%d' %t)

#10번 반복하는 loop

for i in range(1,11):
    print(i, end=' ')
else:
    print('\n---------------------')


s = 0
for n in range(1,11):
    s += n
print(s)

for n in range(10):
    if n >5:
        break
    print(n, end= ' ')
else:
    print('\n정상루트종료')
print('\n------------------')

for n in range(10):
    print(n, end= ' ')
    if n <=5:
        continue
else:
    print('\n정상루트종료')

print('\n---------구구단---------')

for i in range(1, 10):
    for j in range(1,10):
        print("{0} X {1} = {2}".format(j, i, j*i), end = '\t')
    print('')
        # print("%d X %d = %d"%(i, j, i*j))

print('\n---------삼각형---------')
for i in range(10):
    for j in range(0, i+1):
        print('*', end='')
    else:
        print('')

print('\n---------삼각형2---------')
for i in range(10):
    print('*'*(i+1))
print('')



print('\n---------역삼각형---------')
for i in range(10, 0, -1):
    print('*' * i)


