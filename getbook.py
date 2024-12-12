from utils.getPrice import extractPrice
def extractBook(book):
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
    