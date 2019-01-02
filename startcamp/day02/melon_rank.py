import requests
import bs4

h = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
response = requests.get('https://www.melon.com/chart/index.htm',headers=h).text
print(response)
# soup = bs4.BeautifulSoup(response, 'html.parser')
# result = soup.select_one('#KOSPI_now').text
# print(result)