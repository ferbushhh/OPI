import requests as req
from bs4 import BeautifulSoup as bs


def getRub(amount, rate):
    return amount * rate


def getRate(currency):
    res = ""
    try:
        request = req.get("https://www.banki.ru/products/currency/cb/")
        if request.status_code == 200:  # OK
            res = bs(request.text, "html.parser")
    except Exception:
        return None
    if res == "":
        return None
    amount = int(res.find("tr", {"data-currency-code": currency}).find_all("td")[1].text)
    rate = float(res.find("tr", {"data-currency-code": currency}).find_all("td")[3].text)
    return rate / amount


def checkCurrency(currency):
    curs = ["USD", "EUR", "BYN", "KZT"]
    if currency not in curs:
        return False
    else:
        return True


def checkAmount(amount):
    correct = True
    for c in amount:
        if not (c == '.' or c.isdigit()):
            correct = False
            break
    if not correct:
        return " "
    else:
        return float(amount)


def main():
    currency = input("Enter the name of the currency you want to convert from (USD, EUR, BYN, KZT): ")
    if not checkCurrency(currency):
        print("!Wrong format!")
        return

    amount = input("Enter the amount to be converted: ")
    if checkAmount(amount) == " ":
        print("!Wrong amount!")
        return

    rate = getRate(currency)
    if rate:
        print(f"Total in rubles {getRub(float(amount), rate)} RUB.")
    else:
        print("!Error!")


if __name__ == '__main__':
    main()
