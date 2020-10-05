from binance.client import Client
from datetime import datetime
from pandas import DataFrame as df
import os

api_key = os.environ.get('PUBLIC_KEY')
secret_key = os.environ.get('SECRET_KEY')

def binance_price():
    client = Client(api_key=api_key, api_secret=secret_key)

    candles = client.get_klines(symbol='LTCUSDT', interval=Client.KLINE_INTERVAL_1HOUR)

    candlesDF = df(candles)
    candlesDF

    candlesDF_date = candlesDF[0]
    final_date = []

    candlesDF.pop(0)
    candlesDF.pop(11)

    candlesDF.dtypes

    for times in candlesDF_date:
        readable = datetime.fromtimestamp(int(times/1000))
        final_date.append(readable)

    len(final_date)

    final_dateDF=df(final_date)

    final_dateDF.columns=['datetime']

    candlesDF_final = candlesDF.join(final_dateDF)

    candlesDF_final.set_index('datetime',inplace=True)
    
    candlesDF_final.columns=['open','high','low','close','volume','close_time','asset_volume',
                             'trade_number','taker_buy_base','taker_buy_quote']
    
    return candlesDF_final