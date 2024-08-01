import helpers

def run():
    resp = helpers.open_url()
    if(resp.status_code == 200):
        # get books elements as a list
        elementsList = helpers.get_element_list(resp)

        # Store books as a list
        print('Storing books to a list ...')
        booksList = [helpers.extract_book_data(element) for element in elementsList]

        # Output to a CSV file
        helpers.export_to_csv(booksList)

        print('Done')

if __name__ == '__main__':
    run()
