# 내장함수
# sum()
result = sum([1,2,3,4,5])
print(result)

# min()
result = min([1,2,3,4,5])
print(result)

# max()
result = max([1,2,3,4,5])
print(result)

# eval()
result = eval("(3 + 5) * 7")
print(result)

# sorted()
result = sorted([9,1,8,5,4])               # 오름차순 정렬
print(result)
result = sorted([9,1,8,5,4], reverse=True) # 내림차순 정렬
print(result)
result = sorted([('홍길동', 35),('이순신', 75),('아무개', 50)], key=lambda x: x[1], reverse=True)
print(result)

# itertools
# 순열
from itertools import count, permutations
data = ['A','B','C']
result = list(permutations(data, 3)) # 모든 순열 구하기
print(result)

# 조합
from itertools import combinations
data = ['A','B','C'] # 데이터 준비
result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기
print(result)

# 중복을 허용하는 모든 순열 구하기
from itertools import product
data = ['A','B','C'] # 데이터 준비
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기
print(result)

# 중복을 허용하는 모든 조합 구하기
from itertools import combinations_with_replacement
data = ['A','B','C'] # 데이터 준비
result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기(중복 허용)
print(result)

# heapq
import heapq

def heapsort(iterable):
    h = []
    result = []
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

# 최대 힙을 구현하여 내림차순 힙 정렬
import heapq

def heapsort(iterable):
    h = []
    result = []
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

# bisect 이진 탐색
from bisect import bisect_left, bisect_right
a = [1,2,4,4,8]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))

# collections
# deque, Counter
# deque, 큐 구현
from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data)) # 리스트 자료형으로 변환

# Counter
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue']) # 'blue'가 등장한 횟수 출력
print(counter['green']) # 'green'가 등장한 횟수 출력
print(dict(counter)) # 사전 자료형으로 변환

# math
# factorial(x) x! 값 반환
import math
print(math.factorial(5)) # 5 팩토리얼을 출력

# sqrt(x) 제곱근 반환
import math
print(math.sqrt(7)) # 7의 제곱근을 출력

# 최대 공약수 gdc(a, b) a와 b의 최대 공약수 반환
import math
print(math.gcd(21, 14))

# pi
import math
print(math.pi) # 파이(pi) 출력
print(math.e) # 자연상수 e 출력




