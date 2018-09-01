from spider.BiliSpider import BiliBiliDamuSpider
from BiliWordCloud import DrawWordCloud
import sys
from os.path import realpath, dirname
import json


def get_config(name):
    path = dirname(realpath(__file__)) + '/configs/' + name + '.json'
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())

def run(name, danmu_ids, back_img):

    file_name = './results/txts/{}.txt'.format(name)
    wordcloud_name = './static/imgs/{}.png'.format(name)
    stopwords_source = "custom_stopwords.txt"

    spider = BiliBiliDamuSpider(danmu_ids, file_name)
    data_source = spider.start_requests()
    wc_img = DrawWordCloud(data_source, back_img, stopwords_source, wordcloud_name)
    wc_img.start_draw()
    return name + '.png'
