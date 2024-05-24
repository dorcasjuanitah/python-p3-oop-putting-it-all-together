#!/usr/bin/env python3

class Book:
    def __init__(self, title ='Goodness', page_count ='0'):

        self.page_count = page_count
        self.title = title

    @property    
    def page_count(self):
        return self._page_count 

    @page_count.setter 
    def page_count(self, page_count):
        if isinstance(page_count, str):
            self._page_count = page_count
        else:
            raise ValueError (
                 "page_count must be an integer"
                 )
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        print ("Flipping the page...wow, you read fast!")
Book()

    
        