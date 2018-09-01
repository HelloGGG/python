import requests
import xml.etree.ElementTree as ET 

class BiliBiliDamuSpider(object):
    """
    :param damu_ids 弹幕id号 \n
    :param file_name 保存数据txt文件名
    """
    _BASE_URL = 'https://comment.bilibili.com/{}.xml'

    def __init__(self, damu_ids, file_name='bilidamu.txt'):
        self.base_url = self._BASE_URL
        self.damu_ids = damu_ids
        self.damu_text = ''
        self.file_name = file_name

    def start_requests(self):
        for damu_id in self.damu_ids:
            response = requests.get(self.base_url.format(damu_id))
            response.encoding = 'utf-8'
            self.parse_xml(response.text)
        self.save_to_txt()  
            
    def parse_xml(self, response):
        root = ET.fromstring(response)
        ds = root.findall('d')
        for d in ds:
            self.damu_text = self.damu_text + d.text + '\n'

    def save_to_txt(self):   
        with open(self.file_name, 'w', encoding="utf-8") as f:
            f.write(self.damu_text)

