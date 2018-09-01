from wordcloud import WordCloud,ImageColorGenerator
from scipy.misc import imread
import matplotlib.pyplot as plt 
import jieba
from spider.BiliSpider import BiliBiliDamuSpider


class DrawWordCloud(object):
    """
    Parameters
    -----------
    data_source: 词云数据源 \n
    back_img: mask图片 \n
    stopwords_source: 屏蔽词数据源 \n
    pic: 图片名 \n
    """
    def __init__(self, data_source, back_img, stopwords_source=None, pic='test.png'):
        self.data_source = data_source
        self.back_img = back_img
        self.stopwords_source = stopwords_source
        self.pic = pic

    def make_stopwords(self):
        custom_stopwords = set()
        with open(self.stopwords_source, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                custom_stopwords.add(line.strip('\n'))
        return custom_stopwords

    def start_draw(self):
        back_color = imread(self.back_img)

        wc = WordCloud(
            font_path = './fonts/wqymicrohei.ttf ',
            prefer_horizontal=0.7,
            max_words=1000,
            stopwords=self.make_stopwords(),
            mask=back_color,
            background_color='#fff',
            random_state=50,
            scale=1.5
        )
        text = self.data_source

        wc.generate(text)
        # 基于彩色图像生成相应彩色
        image_colors = ImageColorGenerator(back_color)
        # 源
        plt.imshow(wc)
        # 关闭坐标轴
        plt.axis('off')
        # 绘制词云
        plt.figure()
        plt.imshow(wc.recolor(color_func=image_colors))
        plt.axis('off')
        # 保存图片
        wc.to_file(self.pic)
