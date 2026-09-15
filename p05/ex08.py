# 공공 데이터 API 활용하기
# 국회 도서관 사이트 정보 활용하기
# pip install requests
# pip install beautifulsoup4
# pip install lxml
import requests
from bs4 import BeautifulSoup
# API URL과 키 설정
api_key = "API 키 입력"
base_url = f'http://apis.data.go.kr/9720000/searchservice/basic?serviceKey={api_key}&pageno=1&displaylines=10&search=자료명,미국'
# API 요청
response = requests.get(base_url)
# response.text를 BeautifulSoup에 전달하도록 수정
soup = BeautifulSoup(response.text, 'html.parser')
# 결과 출력
# print(soup.prettify())  # .prettify()를 사용하면 XML/HTML 구조가 보기 좋게 정렬됩니다.
print(soup)

# 데이터 처리하기
print(soup.find_all('item'))

for item in soup.find_all('item'):
    print(item.find('name'), item.find('value'))
    
# text 명령으로 텍스트만 추출하기
for item in soup.find_all('item'):
    print(item.find('name').text, item.find('value').text)
    
# '기사명'만 추출하기
for item in soup.find_all('item'):
    if item.find('name').text == '기사명':
        print(item.find('value').text)
        
# '저자명'만 추출하기
for item in soup.find_all('item'):
    if item.find('name').text == '저자명':
        print(item.find('value').text)
 
# 기사명과 저자명 한꺼번에 출력하기
for item in soup.find_all('item'):
    if item.find('name').text == '기사명':
        print(item.find('value').text)
    if item.find('name').text == '저자명':
        print(item.find('value').text)

import pandas as pd

# 판다스 형태로 출력하기
total = []
each_item = []

for item in soup.find_all('item'):
    if item.find('name').text in ['기사명', '자료명']:
        each_item.append(item.find('value').text)
    elif item.find('name').text == '저자명':
        each_item.append(item.find('value').text)

    if len(each_item) == 2:
        total.append(each_item)
        each_item = []

df = pd.DataFrame(total, columns=['기사명', '저자명'])
print(df)