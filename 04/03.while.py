# 1~10 합을구하기
s=0
# for n in range(1,11):
#     s += n
# print(s)

cnt = 0
while cnt < 11:
    s += cnt
    cnt += 1
print(s)

#break
for n in range(100):
    if n > 5:
        break
    print(n,end=' ')
print('\n')

i=0
while i <10:
    if i > 5:
        break
    print(i, end=' ')
    i += 1
print('\n--------------------------------')

# countinue

i=0
while i <10:
    if i <= 5:
        i += 1
        continue
    print(i, end=' ')
    i += 1

print('\n--------------------------------')


# 무한루프
# while True:
#     print('infinite loop')
i = 0
while True:
    print(i, end=' ')
    if i > 5:
        break
    i += 1
