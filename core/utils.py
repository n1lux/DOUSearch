from bs4 import BeautifulSoup as bs


def source_soup(source):
    return bs(source, 'html.parser')