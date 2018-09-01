from selenium import webdriver
import time

url = 'https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&enc=utf-8&wq=%E7%AC%94%E8%AE%B0%E6%9C%ACdiannao&pvid=b0422ede8d934fd3a306617a4cf566e9'
browser = webdriver.Chrome()
browser.get(url)
s_input = browser.find_element_by_css_selector('.p-skip input.input-txt')
s_input.clear()
time.sleep(3)
s_input = browser.find_element_by_css_selector('.p-skip input.input-txt')
s_input.clear()
s_input.send_keys(5)
# with open('test.txt', 'w', encoding='utf-8') as f:
#     f.write(browser.page_source)
# print(browser.find_element_by_css_selector('div.info-evaluate a').text)
