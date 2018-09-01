from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait 
import time
import pymongo

MONGO_URI = 'localhost' 
MONGO_DB = 'spider'
MONGO_COLLECTION = 'wym'
MAX_PAGE = 100
URL = 'https://music.163.com/#/song?id=513791211'

class WymusicComment(object):

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        self.browser.get(URL)
        self.browser.switch_to.frame('g_iframe')
        self.wait = WebDriverWait(self.browser, 10)
       
        self.client = pymongo.MongoClient(MONGO_URI)
        self.db =self.client[MONGO_DB]
        print('初始化完成')

    def start_request(self):
        for i in range(1, MAX_PAGE + 1):
            print('正在爬取第{}页评论'.format(i))
            comments = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.itm')))
            self.request(comments=comments, callback=self.parse)
            self.browser.execute_script("document.querySelector('.zbtn.znxt').click();")

    def parse(self, comments):
        for comment in comments:
            item = {}
            item['user'] = comment.find_element_by_css_selector('div.cnt.f-brk a').text
            item['content'] = comment.find_element_by_css_selector('div.itm div.cnt.f-brk').text
            item['time'] = comment.find_element_by_css_selector('div.time.s-fc4').text
            item['zan'] = comment.find_element_by_css_selector('div.rp a').text
            print(item)
            self.save_mongo(item)

    def request(self, comments, callback):
        callback(comments)

    def save_mongo(self, item):
        if self.db[MONGO_COLLECTION].insert(dict(item)):
            print('存入mongodb成功')
        else:
            print('存入mongodb失败')

if __name__ == '__main__':
    spider = WymusicComment()
    spider.start_request()