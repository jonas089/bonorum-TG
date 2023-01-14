import requests
class TeleClient:
    def __init__(self, token, channel_id):
        url = 'https://api.telegram.org/bot{token}/sendMessage?'
        self.token = token
        self.channel_id = channel_id
        self.url = url.format(token=token)
    def send_message(self, message):
        url = '{base_url}chat_id={channel_id}&text={message}'.format(base_url=self.url, channel_id=self.channel_id, message=message)
        res = requests.get(url).text
        print("URL: ", url)
        return res
