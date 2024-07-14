# ioをインポート
import io
# フォントファイルのパスを取得するためのimportlibをインポート
import importlib.resources
#yfinanceをインポート
import yfinance as yf
#matplotlibのfont_managerとmplfinanceとdatetimeをインポート
from matplotlib import font_manager as fm
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

    # スタイルの指定
    font_path = importlib.resources.files('discordN225chart.fonts_and_licenses').joinpath('NotoSansJP-VariableFont_wght.ttf')
    fm.fontManager.addfont(font_path)
    cs = mpf.make_mpf_style(base_mpf_style='yahoo', rc={"font.family":'Noto Sans JP', 'font.size':30})

    # プロットしてBytesIOとして返す
    mpf.plot(df, type="candle", title='日経平均株価', ylabel='株価', figratio = (18, 12), volume=False, style=cs , tight_layout=True, returnfig=True, closefig=True, savefig=buffer)
    return buffer
