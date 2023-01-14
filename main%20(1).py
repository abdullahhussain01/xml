#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import xml.sax
import csv

class BookHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.book = ""
        self.author = ""
        self.title = ""
        self.genre = ""
        self.price = ""
        self.publish = ""
        self.description = ""
        self.book_list = []


    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "list":
            self.book = attributes["id"]
    def endElement(self, tag):
        if self.CurrentData == "author":
            self.author = self.CurrentData
        elif self.CurrentData == "title":
            self.title = self.CurrentData
        elif self.CurrentData == "genre":
            self.genre = self.CurrentData
        elif self.CurrentData == "price":
            self.price = self.CurrentData
        elif self.CurrentData == "publish_date":
            self.publish = self.CurrentData
        elif self.CurrentData == "description":
            self.description = self.CurrentData
        if tag == "list":
            self.book_list.append([self.book,self.author,self.title,self.genre,self.price,self.publish,self.description])
    def characters(self, content):
        self.CurrentData = content

if (__name__ == "__main__"):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = BookHandler()
    parser.setContentHandler(Handler)

    parser.parse("compiler.xml")

    with open('ss.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id','Author','Title','Genre','Price','Publish','Description'])
        for book in Handler.book_list:
            writer.writerow(book)

