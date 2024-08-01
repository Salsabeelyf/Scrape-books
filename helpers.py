import requests
import re
import pandas as pd
import constants as c

def map_rating(rating):
    return c.RATING_MAP[rating]

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

def open_url():
    print('Sending request to %s ...' % c.URL)
    resp = requests.get(c.URL)
    print('Response Status Code: %d' % resp.status_code)
    return resp

def export_to_csv(booksList):
    # Output to a CSV file
    print('Exporting books to %s ...' % c.FILE_NAME)
    df = pd.DataFrame(booksList)
    df.to_csv(c.FILE_NAME, index=False)
