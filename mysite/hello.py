import random
import requests
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    name = request.args['name']
    # random

    result = random.choice(['ocean.jpg','ocean.jpg','ocean.jpg'])
    return render_template('pong.html', name_in_html=name, result=result)


@app.route('/lotto/<int:num>')
def lotto(num):
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    response = requests.get(url)
    lotto = response.json()

    winner = []
    for i in range(1,7):
        winner.append(lotto[f'drwtNo{i}']) #=> 30

    bonus = lotto['bnusNo'] #=> 6

    return render_template('lotto.html', w=winner, b=bonus, n=num)
