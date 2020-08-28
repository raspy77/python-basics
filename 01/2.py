a= 1.5
print(a, type(a))
b=2.0
print(type(b))

# is_intger 함수는 float객체가 저장한 값으로 정수인지 실수인지 확인가능
b = 2.0
print(type(b))
print(b.is_integer())

c= 3e3
print(c)

#사칙연산
print(2*3)
print(2+3)
print(2-3)
print(2/3)

# //몫연산자 **지수승 % 나머지연산자
print(2//3)
print(2**3)
print(2%3)


#divmod() 함수
t = divmod(2, 3)
print(t, type(t))