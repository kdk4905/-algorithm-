# while
i = 1 # 반복을 위한 변수 설정
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    result += i
    i += 1
print(result)

# 홀수만 더해서 출력
i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1
print(result)

# for
# for 기본 형태
# for 변수 in 리스트 :
#     실행할 소스코드

# for
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
for i in range(1,10):
    result += i
print(result)

# for문에 리스트 사용
scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

# continue
scores = [90, 85, 77, 65, 97]
black_list = [2, 4]

for i in range(5):
    if i + 1 in black_list:
        continue
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

# for문 중첩 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i * j)
    print()