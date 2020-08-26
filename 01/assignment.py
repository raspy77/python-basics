

#치환문

a = 1
b = a+1
print(a, b)

#변수 할당값 오류 ( 연산방향오류)
#1+a=c

e = 3.5; f = 5.3
print(e, f)

# 여러개를 한번에 치환가능

e, f = 3.8, 8.3
print(e, f)

x=y=z=30
print(x,y,z)

#동적 타이핑(실팽중에 변수의타입을 결정)
a = 1
print(type(a))
a = 'hello'
print(type(a))

#확장 치환문

#a=10; a=a+10
a += 10
print(a)


#swqp

x=10
y=20
print('---swqp---')
print(x,y)

x= x+10
y= y-10
print(x,y)