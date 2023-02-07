from secrets.auth import phone, secret, channel
from coingecko import GeckoAPI
from const import base_url
from secrets.wealth import tickers
import time
import json
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
    return format_net(json.loads(api.token_price(token).text)[token]['chf'], 4)

def emit_price_update(asset):
    try:
        price = asset_price(asset)
        message = 'Current population of Casper city: ' + price + ' ,-'
        cli.send_message(message)
    except Exception as e:
        print(e)
        time.sleep(10)
def emit_portfolio_update():
    _tickers = ''
    for t in tickers:
        if _tickers == '':
            _tickers += t
        else:
            _tickers += ',{t}'.format(t=t)

    v = format_net(value(_tickers, tickers), 2)
    try:
        message = 'Your village was raided, you lost: ' + v + ' GOLD'
        cli.send_message(message)
    except Exception as e:
        print(e)
        time.sleep(10)
    #os.system('clear')
    return v
