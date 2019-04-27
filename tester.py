from client import Client
from setup import BINANCE_KEY, SECRET_KEY

client = Client(BINANCE_KEY, SECRET_KEY)

client.get_server_time()

client.ping()

client.get_order_book({'symbol': 'BTCUSDT', 'limit': 5})
