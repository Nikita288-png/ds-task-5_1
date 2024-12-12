import re


def extractPrice(book):
    price=book.find('p',attrs={'class':'price clour'}).text
    floatPrice=re.sub(r'[^\d]','',price)

    return float(floatPrice)