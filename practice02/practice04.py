

for i in range(1, 100):
    a = str(i)
    cnt = a.count('3') + a.count('6') + a.count('9')
    print('{0} {1}'.format(a, '짝'*cnt))