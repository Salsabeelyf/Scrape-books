from bs4 import BeautifulSoup
import helpers

def run():
    resp = helpers.open_url()
    if(resp.status_code == 200):
        soup  = BeautifulSoup(resp.content, 'html.parser')

        # Get books elements list
        print('Finding all books elements ...')
        elementsList = soup.find_all('article', attrs={'class':'product_pod'})

        # Store books as a list
        print('Storing books to a list ...')
        booksList = [helpers.extract_book_data(element) for element in elementsList]

        # Output to a CSV file
        helpers.export_to_csv(booksList)

        print('Done')

if __name__ == '__main__':
    run()
