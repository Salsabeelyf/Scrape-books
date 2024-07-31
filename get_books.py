import requests
from bs4 import BeautifulSoup

RATING = ['One', 'Two', 'Three', 'Four', 'Five']
url = 'http://books.toscrape.com/'

resp = requests.get(url)

print(resp.status_code)

booksList  = []

if(resp.status_code == 200):
    soup  = BeautifulSoup(resp.content, 'html.parser')
    elementsList = soup.find_all('article', attrs={'class':'product_pod'})

    for element in elementsList:
        # Get title
        title = element.find('h3').find('a')['title']
        # Get price
        price = float(element.find('div', attrs={'class': 'product_price'}).find('p').text[1:])
        # Get rating
        rating = element.find('p', attrs={'class': 'star-rating'})['class'][1]
        ratingInt = RATING.index(rating)+1

        # Create book dictionary
        book = {
            'title' : title,
            'price' : price,
            'rating' : ratingInt
        }
        
        # Store books as a list
        booksList.append(book)

        