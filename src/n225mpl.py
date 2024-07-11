import io
#yfinanceをインポート
import yfinance as yf
#mplfinanceとdatetimeをインポート
import mplfinance as mpf
import datetime as dt

def n225plot():

    buffer = io.BytesIO()

    # 取得するデータ詳細
    name = '^N225'
    today = dt.datetime.now()
    start = today - dt.timedelta(days=1)
    end = dt.datetime.now()
    interval = '1m'

    # データのダウンロード
    df = yf.download(tickers=name, start=start, end=end, interval=interval)
    df.head()

    # プロットしてBytesIOとして返す
    mpf.plot(df, type="candle", title='日経平均株価', ylabel='株価', figratio = (3, 2), volume=False, style="yahoo",returnfig=True, closefig=True, savefig = buffer)
    return buffer
