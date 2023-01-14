import requests
class GeckoAPI:
    def __init__(self, url):
        self.url = url
    def token_price(self, token):
        return requests.get('{url}simple/price?ids={token}&vs_currencies=chf'.format(url=self.url, token=token))
    def coin_list(self):
        return requests.get('{url}coins/list'.format(url=self.url))
