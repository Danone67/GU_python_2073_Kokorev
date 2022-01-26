from datetime import datetime

import requests


def currency_rates(currency_code="", url="http://www.cbr.ru/scripts/XML_daily.asp"):

    if not (currency_code and url):
        return None
    
    currency_code = currency_code.upper()
    respond = requests.get(url)
    if respond.ok:
        text = respond.text
        cur = text.split(currency_code)
        if currency_code.isdigit() or len(cur) == 1:
            return None
        value = cur[1].split("</Value>")[0].split("<Value>")[1]
        value = float(value.replace(",", "."))
        date_search = text[text.find('Date="') + 6:text.find('"', text.find('Date="') + 6)].split('.')
        day, month, year = map(int, date_search)
        return f"Курс {currency_code}: {value:.2f} руб, на {datetime(day=day, month=month, year=year).date()}"
    else:
        return None

if __name__ == '__main__':
    print(currency_rates('usD'))
    print(currency_rates("eUR"))
    print(currency_rates("ььь"))
