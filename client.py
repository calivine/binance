import requests
import hashlib
import hmac


class Client(object):

    API_URL = 'https://api.binance.com/api/'

    PUBLIC = 'v1'

    PRIVATE = 'v3'

    def __init__(self, api_key=None, api_secret=None):
        self.API_KEY = api_key
        self.API_SECRET = api_secret
        self.session = self._init_session()

    def _init_session(self):
        session = requests.Session()
        session.headers.update({'Accept': 'application/json',
                                'User-Agent': 'binance/python',
                                'X-MBX-APIKEY': self.API_KEY})
        return session

    def _get(self, path, signed=False, **kwargs):
        print(kwargs['data'])
        v = self.PRIVATE if signed else self.PUBLIC
        response = self.session.get(self.API_URL + v + '/' + path, params=kwargs['data'])
        return response.json()

    def server_time(self):
        response = self.session.get(self.API_URL + self.PUBLIC + '/time')
        print(response.content)

    def ping(self):
        response = self.session.get(self.API_URL + self.PUBLIC + '/ping')
        print(response.content)

    def exchange_info(self):
        response = self.session.get(self.API_URL + self.PUBLIC + '/exchangeInfo')
        print(response.content)

    def get_order_book(self, **params):
        return self._get('depth', data=params)

    def get_average_price(self, **params):
        return self._get('avgPrice', signed=True, data=params)

    def get_trades_list(self, **params):
        return self._get('trades', signed=True, data=params)

    def get_historical_trades(self, **params):
        return self._get('historicalTrades', signed=False, data=params)

    def get_aggregate_trades(self, **params):
        return self._get('aggTrades', signed=False, data=params)

    def get_candlesticks(self, **params):
        return self._get('klines', signed=False, data=params)

    def get_24_hr_price(self, **params):
        return self._get('ticker/24hr', signed=False, data=params)

    def get_price_ticker(self, **params):
        return self._get('ticker/price', signed=True, data=params)

    def get_book_ticker(self, **params):
        return self._get('ticker/bookTicker', signed=True, data=params)
