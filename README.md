# 概要
Discord上で日経平均株価のチャートを表示するbotを動かすためのスクリプトです．

自身で利用するにはDiscord Developer Portalでアプリを作成する必要があります．

# 利用方法

Python3が実行できる環境で動作します．

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

### Discord Developper Portalの設定

権限は"Send Messages"と"Attach Files"が必要です.

トークンを取得してください．

### サーバー側の設定

環境変数`DISCORDN225TOKEN`にDiscord Developer Portalで取得したトークンを設定してください．

### チャンネルの設定
毎日15時25分に「本日の日経平均」という名前のテキストチャンネルに投稿されます．ご自身で作成してください．

## 実行

```
$ python3 discordn225chart
```
