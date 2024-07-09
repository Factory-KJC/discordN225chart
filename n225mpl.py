import io
import urllib.request
from PIL import Image

def n225plot():
    #yfinanceとpandasをインポート
    import yfinance as yf
    import pandas as pd
    #mplfinanceとdatetimeをインポート
    import mplfinance as mpf
    import datetime as dt

    buffer = io.BytesIO()

    #取得するデータ詳細
    name = '^N225'
    today = dt.datetime.now()
    start = today - dt.timedelta(days=1)
    end = dt.datetime.now()
    interval = '1m'

    #データのダウンロード
    df = yf.download(tickers=name, start=start, end=end, interval=interval)
    df.head()

    mpf.plot(df, type="candle", figratio = (3, 2), volume=False, style="yahoo",returnfig=True, closefig=True, savefig = buffer)
    return buffer
