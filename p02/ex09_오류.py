# ex09.py -> F5, 
# 실행 시킬 명령문을 블록설정 후 shift+enter
# 오류 종류
print(foo)
# 1. NameError: name 'foo' is not defined

print(1 + 'hello')
# 2. TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 타입 변환 함수
# int(), float(), str(), bool()
# list(), tuple(), set(), dict()
int('hello')
int('10') # 10
# 주석: ctrl+/
# 3. ValueError: invalid literal for int() with base 10: 'hello'

# 데이터 유형: 리스트
# 변수: my_list
# 연산자: =
# 함수: print()
# 인덱싱: [3]

my_list = [1, 2, 3]
print(my_list[3])
# 4. IndexError: list index out of range

print(my_disc['key'])
# NameError: name 'my_disc' is not defined

my_object.attribute
# NameError: name 'my_object' is not defined


# 제어문
# 조건문
# shift+alt+a: 다중 문자열 -> 주석
# 예약어: if, else
# 함수: print()
""" 
    if 조건:
        참문장
    [else:
        거짓문장]
"""

# 1이 2보다 작은가? 참(True)
if 1 < 2:
print('hi')
else:
    print('world')
# 5. IndentationError: expected an indented block after 'if' statement on line 1

if 1 > 2:
    print('hello')
        print('world')        
