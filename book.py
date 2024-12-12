import requests as rq

from bs4 import BeautifulSoup
from bs4.element import NavigableString

import pandas as pd

from getbook import extractBook 
bookUrl='https://books.toscrape.com/'

bookHeader ={
    'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36'
}

bookResp=rq.get(url=bookUrl,headers=bookHeader)
bookSoup=BeautifulSoup(bookResp.content,'html.parser')

ratings=bookSoup.find_all('p',attrs={'class':'star-rating'})

for r in ratings:
    print(r.attrs['class'][1])


prices=bookSoup.find_all('p',attrs={'class':'price clour'})

for r in prices:
    print(r.attrs['class'][0])


for book in bookSoup.find_all('artical',{'class':"product_pod"}):
    img=book.find('div',attrs={'class':'image_container'}).a.img
    #print(img.attrs)
    imgData={
        'src':img.attrs['src'],
        'alt':img.attrs['alt']
    }
    price=book.find('p',attrs={'class':'price_clour'}).text
    rating=book.find('p',attrs={'class':'star-rating'}).attrs['class'][1]

    title=book.find('h3').a.attrs['title']
    bookData={
        'imgData':imgData,
        'price':price,
        'rating':rating,
        'title':title
    }
    print(bookData)
    print()
    print()
    
books=[extractBook(book)for book in bookSoup.find_all('artical',{'class':"product_pod"})]
bookDf=pd.DataFrame(books)

bookDf.to_csv('books.csv')
#print(book)