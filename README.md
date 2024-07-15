# 概要
Discord上で日経平均株価のチャートを表示するbotです．

適当に素人がググりながら作ったので何が起こっても保証しません．

自身で利用するにはDiscord Developer Portalでアプリを作成する必要があります．

# 利用方法

Pythonが実行できる環境で動作します．

## 動作確認
* Python -> Python3.12.4
* OS ->
  * Windows11
  * Raspberry Pi OS(Debian GNU/Linux 12)

## インストール

```
$ git clone https://github.com/Factory-KJC/discordN225chart.git
$ pip install -e ./discordN225chart
```

## 各種設定


権限は"Send Messages"と"Attach Files"が必要です.

環境変数`DISCORDN225TOKEN`にDiscord Developer Portalで取得したトークンを設定してください．

毎日15時25分に「本日の日経平均」という名前のテキストチャンネルに投稿されます．ご自身で作成してください．

# Contact

緊急連絡は [X](x.com/KJC_UEC) までお願いします．
