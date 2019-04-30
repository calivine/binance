import requests
import hashlib
import hmac
import time
from operator import itemgetter


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

    """ Credit and thanks to [samchardy](https://github.com/sammchardy/python-binance/blob/master/binance/client.py)
        for _generate_signature and _order_params functions for user endpoint signing.
    """

    def _generate_signature(self, data):
        ordered_data = self._order_params(data)
        query_string = '&'.join(["{}={}".format(d[0], d[1]) for d in ordered_data])
        m = hmac.new(self.API_SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256)
        return m.hexdigest()

    def _order_params(self, data):
        """Convert params to list with signature as last element
        :param data:
        :return:
        """
        has_signature = False
        params = []
        for key, value in data.items():
            if key == 'signature':
                has_signature = True
            else:
                params.append((key, value))
        # sort parameters by key
        params.sort(key=itemgetter(0))
        if has_signature:
            params.append(('signature', data['signature']))
        return params

    def _get(self, path, signed=False, **kwargs):
        v = self.PRIVATE if signed else self.PUBLIC
        if (signed):
            kwargs['data']['timestamp'] = int(time.time() * 1000)
            kwargs['data']['signature'] = self._generate_signature(kwargs['data'])
            kwargs['data'] = self._order_params(kwargs['data'])
            kwargs['params'] = kwargs['data']
            response = self.session.get(self.API_URL + v + '/' + path, params=kwargs['params'])
        else:
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

    def get_account_info(self, **params):
        return self._get('account', signed=True, data=params)
