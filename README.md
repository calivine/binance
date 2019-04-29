# Python Binance API
By: *Alex Caloggero*

> Python wrapper to work with the [Binance](https://www.binance.com/en) API.

----
## General Information
* Pass string queries in the form: {key: value, key: value, ...}.
* Methods prefixed with 'get_' return a JSON object.
* No authentication required for public requests.
* Be mindful of API limits.
* For detailed information on Binance's REST API visit [here](https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md).

----
## Initialize
#### Public API Endpoints

    client = Client()
    client.ping()
    b'{}'

----
## Methods for public Endpoints
* server_time()
* ping()
* exchange_info()
* get_order_book(symbol, limit)
* get_average_price(symbol)
* get_trades_list(symbol, limit)
* get_historical_trades(symbol, limit, fromId)
* get_aggregate_trades(symbol, fromId, startTime, endTime, limit)
* get_candlesticks(symbol, interval, startTime, endTime, limit)
* get_24_hr_price(symbol)
* get_price_ticker(symbol)
* get_book_ticker(symbol)
