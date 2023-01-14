from secrets.auth import phone, secret, channel
from coingecko import GeckoAPI
from const import base_url
from secrets.wealth import tickers
import time, os
import json
from termcolor import colored
from tqdm import tqdm
from telegram import TeleClient
from helper import format_net
import requests

phone = phone
cli = TeleClient(secret, channel)
api = GeckoAPI(base_url)

def tokens():
    _tokens = api.coin_list().text
    tokens_json = json.loads(_tokens)
    ids = []
    for t in tokens_json:
        ids.append(t['id'])
    return ids

def value(tokens, _tokens):
    value = 0
    time.sleep(0.1)
    res = json.loads(api.token_price(tokens).text)
    for t in _tokens:
        amount = float(_tokens[t])
        price = res[t]
        value += amount * price['chf']
    return value

def asset_price(token):
    return format_net(json.loads(api.token_price(token).text)[token]['chf'])

def emit_portfolio_update():
    _tickers = ''
    for t in tickers:
        if _tickers == '':
            _tickers += t
        else:
            _tickers += ',{t}'.format(t=t)

    v = format_net(value(_tickers, tickers))
    try:
        message = 'Value: ' + v + ' CHF'
        cli.send_message(message)
    except Exception as e:
        print(e)
        time.sleep(10)
    #os.system('clear')
    return v

def emit_price_update():
    for t in tickers:
        cli.send_message('{t}: {price} CHF'.format(t=t, price=asset_price(t)))
        time.sleep(10)
last_net = 0
while True:
    try:
        emit_price_update()
        _net = float(emit_portfolio_update())
        if _net > last_net:
            print(colored("Portfolio Value: "+ str(_net)+ " CHF", "green"))
        elif _net < last_net:
            print(colored("Portfolio Value: ", str(_net)+ " CHF", "red"))
        else:
            print(colored("Portfolio Value: "+ str(_net)+ " CHF", "yellow"))
        last_net = _net

    except Exception as Req_Limit:
        print('[E]: Request limit exceeded')
        print('-> ', Req_Limit)

    timer = tqdm(total=10)
    for i in range(0, 10):
        time.sleep(1)
        timer.update(1)
    time.sleep(0.1)
    timer.close()
    os.system('clear')
