# 함수
def add(a, b) :
    return a + b
print(add(3, 7))

# return문 없는 함수
def add(a, b) :
    print('함수의 결과 :', a + b)
add(3, 7)

# 함수에 매개변수 지정
def add(a, b) :
    print('함수의 결과 :', a + b)
add(b = 7, a = 3)

# global 키워드
a = 0

def func():
    global a # 지역변수 a가 아닌 함수 밖의 a
    a += 1

for i in range(10):
    func()
print(a)

# 람다 표현식
def add(a, b):
    return a + b

# 일반적인 add() 메서드 사용
print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b : a + b)(3, 7))
