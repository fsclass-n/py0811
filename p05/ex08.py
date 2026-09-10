# 공공 데이터 API 활용하기
# 국회 도서관 사이트 정보 활용하기
# pip install requests
# pip install beautifulsoup4
# pip install lxml
import requests
from bs4 import BeautifulSoup

# API URL과 키 설정
api_key = "1238233c36fee1220efc1ebdd6857b1be08d86da562ba0ef0d398cccb8bc7a57"
base_url = f'http://apis.data.go.kr/9720000/searchservice/basic?serviceKey={api_key}&pageno=1&displaylines=10&search=자료명,미국'

# API 요청
response = requests.get(base_url)
print(response.status_code)
# 403 -> 접근금지(API 키 승인x)
# 404 -> 페이지 없음
# 200 -> ok
# 500 -> 서버 문제
print(response.text)

# response.text를 BeautifulSoup에 전달하도록 수정
soup = BeautifulSoup(response.text, 'lxml')

# 결과 출력
# print(soup.prettify())  # .prettify()를 사용하면 XML/HTML 구조가 보기 좋게 정렬됩니다.
print(soup)
