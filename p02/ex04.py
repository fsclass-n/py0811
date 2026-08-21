# # print(출력 내용)
# print(2 * 1)
# print(2 * 2)
# print(2 * 3)
# print(2 * 4)
# print(2 * 5)
# print(2 * 6)
# print(2 * 7)
# print(2 * 8)
# print(2 * 9)
# # -----------------
# print(3 * 1)


# # 리스트
# """ 
#     for 변수 in 반복가능객체:
#         실행문
# """
# # 0,1,2,3,...,9
# for item in range(10):
# 	print(item)
# # 2,3,4,5,...,19
# for item in range(2, 20):
# 	print(item)
# # 1,2,3,4,...,9
# for item in range(1, 10):
# 	print(2 * item)

# for item in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
# 	print(2 * item)

# 다중 for문
for item in range(2, 10):
	for each in range(1, 10):
		print(item * each)

# print(인자1, 인자2, ...)
# 최종 결과
for item in range(2, 10):
	for each in range(1, 10):
		print(item, ' x ', each, ' = ', item * each)

# 연산자
# 대입(할당)연산자: =
# 산술연산자: + - * / % // **
# 비교연산자: > < >= <= == !=

# 내장 함수: print(), type(), range(), round()

# 데이터 타입: 
# - 숫자(정수, 실수), 문자열, 불
# - 리스트, 튜플, 세트, 딕셔너리

# 프롬프트: 
# vscode 터미널에 2단부터 9단까지 가로로 표시되게 코드 수정해줘
# print(인자1, 인자2, ..., end='\n')
for each in range(1, 10):
    for item in range(2, 10):
        print(item, ' x ', each, ' = ', item * each, end='\t')
    print()

print('안녕', end='\t')
print('하세요', end='\t')
# 안녕  하세요