# 2022/12/29 17:42
# 你好，夜嗨大帅比

from selenium import webdriver
import time
import text
from table_init import Table
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options

# selenmium设置

opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disbale-gpu")
path = "E:\\pythonProject1\\run_code\\venv\\Lib\\site-packages\\chromedriver.exe"



def get_html(de_url):
    try:
        web = webdriver.Chrome(executable_path=path)
        web.get(de_url)
        time.sleep(2)
        return web
    except WebDriverException as driver_error:
        print("驱动失败："+ driver_error)


def get_one_page(web):

    brk = 0
    # tbody = web.find_element_by_xpath('//*[@id="exploits-table"]/tbody')
    # '//*[@id="exploits-table"]/tbody/tr[1]/td[1]'
    table = Table()
    tr_ = web.find_elements_by_xpath('//*[@id="exploits-table"]/tbody/tr')
    for i in tr_:
        data = ()
        if brk == 12:
            break
        else:
            brk = brk + 1
            table.published_time = i.find_element_by_xpath('./td[1]').text
            table.title = i.find_element_by_xpath('./td[5]').text
            table.download_url = i.find_element_by_xpath('./td[2]/a').get_attribute('href')
            table.author = i.find_element_by_xpath('./td[8]/a').text
            table.platform = i.find_element_by_xpath('./td[7]/a').text
            table.exploit_type = i.find_element_by_xpath('./td[6]/a').text
            table.exploit_url = i.find_element_by_xpath('./td[5]/a').get_attribute('href')
            table.eid = table.exploit_url.split('/')[-1]
            save_data(table)
            # print(table.title,table.published_time,table.exploit_type,table.exploit_url,table.author,table.platform)

            # print(table.exploit_url)
def save_data(table):
    db = text.DB()
    if db.is_exist_eid(table.eid):
        pass
        # print(1)
    else:
        data = (table.eid, table.title, table.exploit_type, table.exploit_url, table.platform, table.author, table.published_time,table.download_url)
        db.add_data(data)
        print("ok save!!!")




# get_one_page()
def main() :
    url = "https://www.exploit-db.com/"
    web = get_html(url)
    while True:
        # next_page = WebDriverWait.until(web, 10).until(expected_conditions.element_to_be_clickable(web.find_element_by_xpath('//*[@id="exploits-table_next"]/a', True)))
        time.sleep(3)
        get_one_page(web)
        web.implicitly_wait(10)
        next_page = web.find_element_by_xpath('//*[@id="exploits-table_next"]/a')
        web.execute_script("$(arguments[0]).click()", next_page)
        time.sleep(4)
#     # 下一页
#     next_page = web.find_element_by_xpath('//*[@id="exploits-table_next"]/a')
#     # 循环点击下一页
#     for page_num in range(3000):
#         time.sleep(2)
#         table = get_one_page(web)
#         if db.is_exist_eid(table.eid):
#             pass
#         else:
#             data = (table.eid,table.title,table.exploit_type,table.exploit_url,table.platform,table.author,table.published_time,table.download_url)
#             db.add_data(data)
#         web.execute_script("$(arguments[0]).click()", next_page)
#         time.sleep(3)
if __name__ == '__main__':
    main()