import os
import requests
token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')
# 하고 싶은 것들 작성할 수 있음.
text = '안녕하세요'
requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')