# 함수(function)
""" 
    함수 정의
        def 함수(매개변수1, 매개변수2, ...):
            문장
            [return 값]
    함수 호출
        함수명(인자1, 인자2, ...)

    def y(x):
        return 3 * x
    
    y(12)
"""
# 익명 함수
# 파이썬의 lambda는 이름을 붙이지 않고 간단한 함수를 한 줄로 만드는 문법입니다
y = lambda x : 3 * x
y(12)

add = lambda a, b : a + b
add(2, 3)

littlePrince = '''여섯 살 적에 나는 '체험한 이야기'라는 제목의 원시림에 관한 책에서 기막힌 그림 하나를 본 적이 있다. 맹수를 집어삼키고 있는 보아뱀 그림이었다. 위의 그림은 그럿을 옮겨 그린 것이다. 그 책에는 이렇게 씌어 있었다.
'보아뱀은 먹이를 씹지도 않고 통째로 집어삼킨다. 그리고는 꼼짝도 하지 못하고 여섯 달 동안 잠을 자면서 그것을 소화시킨다.' '''
# 슬라이싱
littlePrince[:10]

# 람다
short = lambda x : x[:10]
short(littlePrince)

exchange = lambda won : won * 0.00086
exchange(1000000) # 860.0
exchange(500000) # 430.0
exchange(250000) # 215.0


def add(a, b):
	return a + b
	
add(233, 43)


def calculator(a, b):
	return a + b, a - b, a * b, a / b

calculator(12, 3) # (15, 9, 36, 4.0)
type(calculator(12, 3))

type(1)
type(1.0)
type('문자')
type(True)
type("true")