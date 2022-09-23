def main():
    currency_str = input("请输入带有符号的货币值（例：1USD，100RMB）：")
    try:
        if currency_str[-3:].lower() == "usd":
            print(f"转换结果是{eval(currency_str[:-3]) * 7:.2f}RMB")
        elif currency_str[-3:].lower() == "rmb":
            print(f"转换结果是{eval(currency_str[:-3]) / 7:.2f}USD")
        else:
            print("输入格式错误")
            main()
    except NameError:
        print("输入格式错误")
        main()


if __name__ == '__main__':
    main()
