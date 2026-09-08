# 1,2 파이썬 기본 문법
# 3,4 응용: 외부 파일 불러오기 txt, csv(엑셀)
# 5 파이썬 용도: 
# *.ipynb: shift+enter
#  - 데이터분석(넘파이, 판다스) -> 시각화(맵플롤립)
# *.py: F5
#  - 6. 크롤링

# 내장 모듈
import os
# 외장 모들
import pandas as pd

os.chdir(r'E:\wi\git\py0811\p05')

# 판다스로 CSV 파일 읽기
df = pd.read_csv('apt2308.csv', thousands=',')

# 10억 원을 초과하는 가격으로 거래된 아파트
print(df.loc[:, ['단지명', '거래금액']][df['거래금액'] > 100000])





