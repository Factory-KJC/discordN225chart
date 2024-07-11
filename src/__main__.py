import discordN225chart
import argparse
import os

# メインの処理
def main():
    discordN225chart()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A Discord bot that posts N225 chart at 15:30 on business days.")

    # help オプションの定義
    parser.add_argument('--help', action='store_true', help='Show help message')

    # settoken オプションの定義
    parser.add_argument('--settoken', type=str, metavar='TOKEN', help='Set token and save it to APP_TOKEN.txt')

    args = parser.parse_args()

    if args.help:
        parser.print_help()
    elif args.settoken:
        # APP_TOKEN.txt にトークンを書き込む
        token_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'APP_TOKEN.txt')
        with open('APP_TOKEN.txt', 'w') as f:
            f.write(args.settoken)
        print(f'Token has been saved to APP_TOKEN.txt: {args.settoken}')
    else:
        parser.print_usage()
        print("Error: Invalid option provided.")

    # help や settoken が指定されていない場合はメインの処理を実行する
    if not (args.help or args.settoken):
        main()
