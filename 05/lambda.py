def f(x):
    r = x * x
    return r


for i in range(10):
    s = '{0}:{1}'.format(i, f(i))
    print(s)



# 함수를 안에내장 위와같은결과
for i in range(10):
    s = '{0}:{1}'.format(i, (lambda x: x * x)(i))
    print(s)

