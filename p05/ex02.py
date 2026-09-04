# 넘파이로 배열 정의하기
# import 모듈 as 별칭
import numpy as np

# np.array() 함수로 배열 정의
a = np.array([[2, 3], [5, 2]])
print(a)

# 3x5 배열을 만들어 d에 저장
d = np.array([[1, 2, 3, 4, 5], [2, 4, 5, 6, 7], [5, 7, 8, 9, 9]])
print(d)

# 인덱싱
# 배열명[행인덱스][열인덱스]
# 배열명[행인덱스, 열인덱스]
print(d[1][2])
print(d[1, 2]) # 이처럼 표현할 수도 있다.

# 배열 슬라이싱 하기
print(d[1:, 3:])

# 1차원 배열
d = np.array([2, 3, 4, 5, 6])
print(d)

# 배열의 크기 알아내기: shape 속성
# 1차원 배열의 크기: 요소의 개수
# 함수()
# 객체.메서드(method, 동작, 기능)
# 객체.속성(property, 특징)
print(d.shape) # d에는 1개 리스트에 5개의 원소가 있다.

# 2차원 배열
e = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
print(e)

# 2차원 배열의 크기: 행과 열의 개수
# 행의 개수: 2, 열의 개수: 4 -> (2, 4)
print(e.shape) # e에는 2개의 리스트에 각 4개의 원소가 있다.

# 배열 d의 자료형 확인
# int64: 64비트 정수형
print(d)
print("38:",d.dtype)

# 배열 유형 바꾸기: astype() 함수
# data 배열의 자료형을 float(실수)으로 바꾸기
print("45:",d.astype('float64'))

# 넘파이 함수 알아보기
# 0으로 이뤄진 배열 만들기 - np.zeros() 함수
# 2행 10열의 0으로 이뤄진 배열 만들기
print(np.zeros((2, 10)))

# 1로 이뤄진 배열 만들기 - np.ones() 함수
# 2행 10열의 1로 이뤄진 배열 만들기
print(np.ones((2, 10)))


# 연속형 정수 생성하기 - np.arange() 함수
# 2부터 9까지의 정수로 이뤄진 배열 만들기
print(np.arange(2, 10))


# 행과 열 바꾸기 - np.transpose() 함수
a = np.ones((2, 3))
print(a)
# a에 저장된 배열의 행과 열을 바꿔서 b에 저장하기
b = np.transpose(a)
print(b)


# 배열의 사칙 연산
arr1 = np.array([[2, 3, 4], [6, 7, 8]])
arr2 = np.array([[12, 23, 14], [36, 47, 58]])
# 배열의 덧셈
print(arr1 + arr2)
# 배열의 곱셈
print(arr1 * arr2)
# 배열의 나눗셈
print(arr1 / arr2)


# 크기가 서로 다른 배열끼리 더하기
arr3 = np.array([100, 200, 300])
print(arr1.shape)
print(arr3.shape)
# arr1과 arr3의 shape이 다르지만, arr1의 열의 개수와 arr3의 요소의 개수가 같기 때문에 arr1과 arr3을 더할 수 있다.
# 브로드캐스팅(Broadcasting): 크기가 서로 다른 배열을 연산하는 기능!
print(arr1 + arr3)


