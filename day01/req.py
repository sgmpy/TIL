import requests
import bs4

response = requests.get('https://finance.naver.com/sise/').text
soup = bs4.BeautifulSoup(response, 'html.parser')
result = soup.select_one('#KOSPI_now').text
print(result)
