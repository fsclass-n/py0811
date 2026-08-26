# ex09.py -> F5, 
# 실행 시킬 명령문을 블록설정 후 shift+enter
# 오류 종류
# 1. NameError
print(foo)
# NameError: name 'foo' is not defined

# 2. TypeError
print(1 + 'hello')
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 3. ValueError
# 타입 변환 함수
# int(), float(), str(), bool()
# list(), tuple(), set(), dict()
int('hello')
int('10') # 10
# 주석: ctrl+/
# ValueError: invalid literal for int() with base 10: 'hello'

# 4. IndexError
# 데이터 유형: 리스트
# 변수: my_list
# 연산자: =
# 함수: print()
# 인덱싱: [3]

my_list = [1, 2, 3]
print(my_list[3])
# IndexError: list index out of range

# 5. KeyError
my_disc = {'name': 'Alice', 'age': 25}
print(my_disc['key'])
# KeyError: 'key'


# 6. AttributeError
class Person:
    def __init__(self, name):
        self.name = name

my_object = Person('Alice')
print(my_object.attribute)
# AttributeError: 'Person' object has no attribute 'attribute'

# 7. SyntaxError
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
if 1 < 2
    print('hi')
else:
    print('world')
# SyntaxError: expected ':'


# 8. IndentationError
if 1 > 2:
    print('hello')
        print('world')  
# IndentationError: expected an indented block after 'if' statement on line 1      

# 9. ModeleNotFoundError
import my_module
# ModuleNotFoundError: No module named 'my_module'

# 10. ImportError
from math import not_exist_func
# ImportError: cannot import name 'not_exist_func' from 'math' (unknown location)

# ZeroDivisionError
print(1 / 0)
# ZeroDivisionError: division by zero