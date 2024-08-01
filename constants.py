URL = 'http://books.toscrape.com/'
BOOK_ELEMENT_XPATH = "//article[@class='product_pod']"
TITLE_XPATH = './h3/a'
PRICE_XPATH = './div[@class="product_price"]/p'
RATING_XPATH = "./p[contains(@class,'star-rating')]"

RATING_MAP = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

FILE_NAME = 'books.csv'
