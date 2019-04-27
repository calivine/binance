import requests
import hashlib
import hmac
from setup import BINANCE_KEY, SECRET_KEY

class Client(object):

    API_URL = 'https://api.binance.com'

    def __init__(self, api_key, api_secret, request_params=None):
        self.API_KEY = api_key
        self.API_SECRET = api_secret
        self.session = self._init_session()

    def _init_session(self):
        session = requests.Session()
        session.headers.update({'Accept': 'application/json',
                                'User-Agent': 'binance/python',
                                'X-MBX-APIKEY': self.API_KEY})
        return session

    def get_server_time(self):
        response = self.session.get(self.API_URL + '/api/v1/time')
        print(response.content)

    def ping(self):
        response = self.session.get(self.API_URL + '/api/v1/ping')
        print(response.content)

    def get_exchange_info(self):
        response = self.session.get(self.API_URL + '/api/v1/exchangeInfo')
        print(response.content)

    def get_order_book(self, request_params):
        response = self.session.get(self.API_URL + '/api/v1/depth', params=request_params)
        print(response.content)
