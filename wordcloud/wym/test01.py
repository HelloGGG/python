from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import matplotlib.pyplot as plt
import jieba
from scipy.misc import imread 

back_color = imread('./mask/mask.jpeg')

wc = WordCloud(
    background_color = '#fff',
    mask = back_color,
    max_words = 1000,
    stopwords = STOPWORDS,
    font_path = './fonts/wqymicrohei.ttf ',
    max_font_size = 50,
    random_state= 50
)


with open('test.txt', 'r', encoding='utf-8') as f:
    text = f.read()

wc.generate(text)
# 基于彩色图像生成相应彩色
image_colors = ImageColorGenerator(back_color)
# 显示图片
plt.imshow(wc)
# 关闭坐标轴
plt.axis('off')
# 绘制词云
plt.figure()
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis('off')
# 保存图片
wc.to_file('test.png')