# 외부에서 사용자가 값을 입력
# 내장 함수: input()
# input 결과는 숫자가 아닌 문자열이다.
a = input('숫자를 하나 입력해 보세요: ')
print('방금' + a + '을 입력하셨죠!')

# 복제: shift+alt+방향키
print(type(a))
# 위치이동: alt+방향키

a = int(a)
print(type(a))

a = float(a)
print(type(a))