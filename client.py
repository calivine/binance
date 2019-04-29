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

    def server_time(self):
        response = self.session.get(self.API_URL + self.PUBLIC + '/time')
        print(response.content)

    def ping(self):
        response = self.session.get(self.API_URL + self.PUBLIC + '/ping')
        print(response.content)

    def exchange_info(self):
        response = self.session.get(self.API_URL + self.PUBLIC + '/exchangeInfo')
        print(response.content)

    def get_order_book(self, request_params):
        response = self.session.get(self.API_URL + self.PUBLIC + '/depth', params=request_params)
        return response.json()

    def get_average_price(self, request_params):
        response = self.session.get(self.API_URL + self.PRIVATE + '/avgPrice', params=request_params)
        return response.json()

    def get_trades_list(self, request_params):
        response = self.session.get(self.API_URL + self.PUBLIC + '/trades', params=request_params)
        return response.json()

    def get_historical_trades(self, request_params):
        response = self.session.get(self.API_URL + self.PUBLIC + '/historicalTrades', params=request_params)
        return response.json()

    def get_aggregate_trades(self, request_params):
        response = self.session.get(self.API_URL + self.PUBLIC + '/aggTrades', params=request_params)
        return response.json()

    def get_candlesticks(self, request_params):
        response = self.session.get(self.API_URL + self.PUBLIC + '/klines', params=request_params)
        return response.json()

    def get_24_hr_price(self, request_params):
        try:
            response = self.session.get(self.API_URL + self.PUBLIC + '/ticker/24hr', params=request_params)
        except:
            print('Error. There was a problem with your request. Try again.')
        return response.json()

    def get_price_ticker(self, request_params):
        try:
            response = self.session.get(self.API_URL + self.PRIVATE + '/ticker/price', params=request_params)
        except:
            print('Error. There was a problem with your request. Try again.')
        return response.json()

    def get_book_ticker(self, request_params):
        try:
            response = self.session.get(self.API_URL + self.PRIVATE + '/ticker/bookTicker', params=request_params)
            return response.json()
        except:
            print('Error. There was a problem with your request. Try again.')
