from spider import BiliBiliDamuSpider
import sys
from os.path import realpath, dirname
import json


def get_config(name):
    path = dirname(realpath(__file__)) + '/configs/' + name + '.json'
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())

def run():
    name = sys.argv[1]
    config = get_config(name)
    danmu_ids = config.get('danmu_ids')
    file_name = config.get('file_name')
    spider = BiliBiliDamuSpider(danmu_ids, file_name)
    spider.start_requests()

if __name__ == '__main__':
    run()