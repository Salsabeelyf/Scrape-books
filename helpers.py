import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
from lxml import etree
import constants as c

def map_rating(rating):
    return c.RATING_MAP[rating]

def clean_price(price):
    price = re.sub("[^0-9.]","", price)
    return float(price)

def extract_book_data(element):
    # Get title
    title = element.find(c.TITLE_XPATH).attrib['title']

    # Get price
    price = clean_price(element.find(c.PRICE_XPATH).text)

    # Get rating
    rating = map_rating(element.xpath(c.RATING_XPATH)[0].attrib['class'].split(' ')[-1])

    # Create book dictionary
    return {
        'title' : title,
        'price' : price,
        'rating' : rating
    }

def open_url():
    print('Sending request to %s ...' % c.URL)
    resp = requests.get(c.URL)
    print('Response Status Code: %d' % resp.status_code)
    return resp

def get_element_list(resp):
    soup  = BeautifulSoup(resp.content, 'html.parser')
    dom = etree.HTML(str(soup))

    # Get books elements list
    print('Finding all books elements ...')
    return dom.xpath(c.BOOK_ELEMENT_XPATH)


def export_to_csv(booksList):
    # Output to a CSV file
    print('Exporting books to %s ...' % c.FILE_NAME)
    df = pd.DataFrame(booksList)
    df.to_csv(c.FILE_NAME, index=False)
