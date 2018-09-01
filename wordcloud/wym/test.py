import pymongo
import re


MONGO_URI = 'localhost'
MONGO_DB = 'spider'

class WymCommentWordCloud(object):

    def __init__(self):
        self.mongo_uri = MONGO_URI
        self.mongo_db = MONGO_DB
       
    def get_data(self):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        items = self.db['wym'].find()
        data = ''
        for item in items:
            data = data + item.get('content') + '\n'
        with open('test.txt', 'w', encoding='utf-8') as f:
            f.write(data)
    
if __name__ == '__main__':
    test = WymCommentWordCloud()
    test.get_data()
