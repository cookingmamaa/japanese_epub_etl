import os
import pandas as pd
import ebooklib
from ebooklib import epub
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    # def handle_starttag(self, tag, attrs):
    #     print("Encountered a start tag:", tag)

    # def handle_endtag(self, tag):
    #     print("Encountered an end tag :", tag)

    def __init__(self):
        super().__init__()
        self.data_collected = []  # List to store collected data

    def handle_data(self, data):
        if data.strip():
            print("Encountered some data  :", data)
            print("Length of data: ", len(data))
            self.data_collected.append({'type':'data', 'data':data})


# set file path for book
fp_input_epub = 'C:/Users/aches/Desktop/Stuff/ePubs/キチン・ばなな.epub'

# read in book
book = epub.read_epub(fp_input_epub)

# test retrieve metadata about book
book.get_metadata('DC', 'title')
book.get_metadata('DC', 'creator')
book.get_metadata('DC', 'language')
book.get_metadata('DC', 'publisher')

# try to read text??
book.get_items()

doc_gen = book.get_items_of_type(ebooklib.ITEM_DOCUMENT)

html1 = next(doc_gen)

html1.get_content()
html1.get_body_content().decode()

bytes_test = b'\xe3\x80\x80\xe7\xa7\x81\xe3\x81\xaf\xe3\x81\x84\xe3\x81\x8f\xe3\x81\xa4\xe3\x82\x82\xe3\x81\x84\xe3\x81\x8f\xe3\x81\xa4\xe3\x82\x82\xe3\x81\x9d\xe3\x82\x8c\xe3\x82\x92\xe3\x82\x82\xe3\x81\xa4\xe3\x81\xa0\xe3\x82\x8d\xe3\x81\x86\xe3\x80\x82\xe5\xbf\x83\xe3\x81\xae\xe4\xb8\xad\xe3\x81\xa7\xe3\x80\x81\xe3\x81\x82\xe3\x82\x8b\xe3\x81\x84\xe3\x81\xaf\xe5\xae\x9f\xe9\x9a\x9b\xe3\x81\xab\xe3\x80\x82\xe3\x81\x82\xe3\x82\x8b\xe3\x81\x84\xe3\x81\xaf\xe6\x97\x85\xe5\x85\x88\xe3\x81\xa7\xe3\x80\x82\xe3\x81\xb2\xe3\x81\xa8\xe3\x82\x8a\xe3\x81\xa7\xe3\x80\x81\xe5\xa4\xa7\xe3\x81\x9c\xe3\x81\x84\xe3\x81\xa7\xe3\x80\x81\xe4\xba\x8c\xe4\xba\xba\xe3\x81\x8d\xe3\x82\x8a\xe3\x81\xa7\xe3\x80\x81\xe7\xa7\x81\xe3\x81\xae\xe7\x94\x9f\xe3\x81\x8d\xe3\x82\x8b\xe3\x81\x99\xe3\x81\xb9\xe3\x81\xa6\xe3\x81\xae\xe5\xa0\xb4\xe6\x89\x80\xe3\x81\xa7\xe3\x80\x81\xe3\x81\x8d\xe3\x81\xa3\xe3\x81\xa8\xe3\x81\x9f\xe3\x81\x8f\xe3\x81\x95\xe3\x82\x93\xe3\x82\x82\xe3\x81\xa4\xe3\x81\xa0\xe3\x82\x8d\xe3\x81\x86\xe3\x80\x82'
print(bytes_test.decode()) # it works! we can decode part of the text, now need to just scrape through it

# this lets us store each of the html sections (perhaps chapters) into a dataframe
# next need to figure out how to separate them into individual words - maybe need to utilize a dictionary mapping
# and scan through each of the sentences / words here
parser = MyHTMLParser()
parser.feed(html1.get_body_content().decode())

df = pd.DataFrame(parser.data_collected)


