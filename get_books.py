import requests
from bs4 import BeautifulSoup
import re


url = 'http://books.toscrape.com/'

def map_rating(rating):
    rating_map = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    return rating_map[rating]

def clean_price(price):
    price = re.sub("[^0-9.]","", price)
    return float(price)

def extract_book_data(element):
    # Get title
    title = element.find('h3').find('a')['title']
    # Get price
    price = clean_price(element.find('div', attrs={'class': 'product_price'}).find('p').text)
    # Get rating
    rating = element.find('p', attrs={'class': 'star-rating'})['class'][-1]
    ratingInt = map_rating(rating)

    # Create book dictionary
    return {
        'title' : title,
        'price' : price,
        'rating' : ratingInt
    }

resp = requests.get(url)

print(resp.status_code)

booksList  = []

if(resp.status_code == 200):
    soup  = BeautifulSoup(resp.content, 'html.parser')

    # Get books elements list
    elementsList = soup.find_all('article', attrs={'class':'product_pod'})

    # Store books as a list
    booksList = [extract_book_data(element) for element in elementsList]
