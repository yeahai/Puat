# 2022/12/29 17:42
# 你好，夜嗨大帅比
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import requests
import time

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options
import re



# selenmium设置

opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disbale-gpu")
path = "E:\\pythonProject1\\run_code\\venv\\Lib\\site-packages\\chromedriver.exe"

url = "https://www.exploit-db.com/"



# def get_html(de_url):
#     try:
#         web = webdriver.Chrome(executable_path=path)
#         web.get(de_url)
#         time.sleep(2)
#         return web
#     except WebDriverException as driver_error:
#         print("驱动失败："+driver_error)

web = webdriver.Chrome(executable_path=path)
web.maximize_window()
web.get(url)

# next_page.click()
while True:
    # next_page = WebDriverWait.until(web, 10).until(expected_conditions.element_to_be_clickable(web.find_element_by_xpath('//*[@id="exploits-table_next"]/a', True)))
    web.implicitly_wait(10)
    next_page = web.find_element_by_xpath('//*[@id="exploits-table_next"]/a')
    web.execute_script("$(arguments[0]).click()",next_page)
    time.sleep(3)
# Re模块设置
## 解析数据
# obj = re.compile(r'<td class=" text-center" tabindex="0" style>(?P<time>.*?)</td>',re.S)
# obj = re.compile(r'<tbody>(?P<body>.*?)</tbody>',re.S)
# obj_tbody = re.compile(r'<tbody>.*?</tbody>')
# obj_tr = re.compile(r'<tbody><tr role="row".*?<td class=" text-center" tabindex="0">(?P<time>.*?)</td>'
#                  r'<td class=" text-center"><a href=(?P<downl>.*?) aria-label=.*?'
#                  r'<td><a href=(?P<exploit>.*?)>(?P<title>.*?)</a></td>'
#                  r'<td class=" text-center"><a href="#" value=.*?>(?P<type>.*?)</a></td>')
# result = obj_tbody.findall(web.page_source)
# result = obj.finditer(web.page_source)
# result1 = obj_tr.finditer(result[0])
# print(result[0])
# for it in result1:
#     print(it.group("time"))
#     print(it.group("downl"))
#     # print(it.group("body"))
#     print(it.group("exploit"))
#     print(it.group("title"))
#     print(it.group("type"))



# page_num = int(web.find_element_by_xpath('//*[@id="exploits-table_paginate"]/ul/li[9]/a').text)
# for i in range(page_num):
#     tbody = web.find_element_by_xpath('//*[@id="exploits-table"]/tbody')
#     time.sleep(3)
# tbody = web.find_element_by_xpath('//*[@id="exploits-table"]/tbody')
# tr_ = web.find_elements_by_xpath('//*[@id="exploits-table"]/tbody/tr')
# print(tbody.text)
# print(tr_)

# for i in tr_:
#     result = obj.finditer(i.text)
#     for it in result:
#         print(it.group("time"))







# t = 1
# for i in tr_:
    # print(i.text)
    # print(t)
    # t = t + 1
    # # print(i.text)
    # time.sleep(1)
    # time_ = i.find_element_by_xpath('./td[1]').text
    # # '//*[@id="exploits-table"]/tbody/tr[1]/td[1]'
    # # '//*[@id="exploits-table"]/tbody/tr[15]/td[1]'
    # # href = i.find_element_by_xpath('./td[2]/a').get_attribute('href')
    # print(i)
    # title = i.find_element_by_xpath('./td[5]/a').text
    # type_ = i.find_element_by_xpath('./td[6]').text
    # platform = i.find_element_by_xpath('./td[7]').text
    # author = i.find_element_by_xpath('./td[8]').text
#
    # print(time_)
    # print(time_ + ' ' + title + ' ' + type_ + ' ' + platform + ' ' + author )
    # print(time_ + " " + href + " " + title)
# next_ = web.find_element_by_xpath('//*[@id="exploits-table_next"]/a')
# next_.click()
# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# opts = Options()
# opts.ignore_local_proxy_environment_variables()
# driver = webdriver.Firefox(options=opts)
# driver.get("https://stackoverflow.com/")


'''
        <tr role="row" class="odd"><td class=" text-center" tabindex="0">2022-11-11</td><td class=" text-center"><a href="/download/51031" aria-label="Download51031"><i class="mdi mdi-download mdi-18px" style="color: #132f50"></i></a></td><td class=" text-center"></td><td class=" text-center"><i class="mdi mdi-close mdi-18px" style="color: #ec5e10"></i></td><td><a href="/exploits/51031">SmartRG Router SR510n 2.6.13 - Remote Code Execution</a></td><td class=" text-center"><a href="#" value="remote">Remote</a></td><td class=" text-center"><a href="#" value="hardware">Hardware</a></td><td class=" text-center"><a href="#">Yerodin Richards</a></td></tr>
        <tr role="row" class="even"><td class=" text-center" tabindex="0">2022-11-11</td><td class=" text-center"><a href="/download/51030" aria-label="Download51030"><i class="mdi mdi-download mdi-18px" style="color: #132f50"></i></a></td><td class=" text-center"></td><td class=" text-center"><i class="mdi mdi-close mdi-18px" style="color: #ec5e10"></i></td><td><a href="/exploits/51030">CVAT 2.0 - Server Side Request Forgery</a></td><td class=" text-center"><a href="#" value="webapps">WebApps</a></td><td class=" text-center"><a href="#" value="python">Python</a></td><td class=" text-center"><a href="#">Emir Polat</a></td></tr>
        <tr role="row" class="odd"><td class=" text-center" tabindex="0">2022-11-11</td><td class=" text-center"><a href="/download/51029" aria-label="Download51029"><i class="mdi mdi-download mdi-18px" style="color: #132f50"></i></a></td><td class=" text-center"></td><td class=" text-center"><i class="mdi mdi-close mdi-18px" style="color: #ec5e10"></i></td><td><a href="/exploits/51029">IOTransfer V4 - Unquoted Service Path</a></td><td class=" text-center"><a href="#" value="local">Local</a></td><td class=" text-center"><a href="#" value="windows">Windows</a></td><td class=" text-center"><a href="#">BLAY ABU SAFIAN</a></td></tr>
        <tr role="row" class="even"><td class=" text-center" tabindex="0">2022-11-11</td><td class=" text-center"><a href="/download/51028" aria-label="Download51028"><i class="mdi mdi-download mdi-18px" style="color: #132f50"></i></a></td><td class=" text-center"></td><td class=" text-center"><i class="mdi mdi-close mdi-18px" style="color: #ec5e10"></i></td><td><a href="/exploits/51028">AVEVA InTouch Access Anywhere Secure Gateway 2020 R2 - Path Traversal</a></td><td class=" text-center"><a href="#" value="remote">Remote</a></td><td class=" text-center"><a href="#" value="hardware">Hardware</a></td><td class=" text-center"><a href="#">Jens Regel</a></td></tr>
        <tr role="row" class="odd"><td class=" text-center" tabindex="0">2022-11-11</td><td class=" text-center"><a href="/download/51027" aria-label="Download51027"><i class="mdi mdi-download mdi-18px" style="color: #132f50"></i></a></td><td class=" text-center"></td><td class=" text-center"><i class="mdi mdi-close mdi-18px" style="color: #ec5e10"></i></td><td><a href="/exploits/51027">MSNSwitch Firmware MNT.2408 - Remote Code Execution</a></td><td class=" text-center"><a href="#" value="remote">Remote</a></td><td class=" text-center"><a href="#" value="hardware">Hardware</a></td><td class=" text-center"><a href="#">Eli Fulkerson</a></td></tr>
        <tr role="row" class="even"><td class=" text-center" tabindex="0">2022-11-11</td><td class=" text-center"><a href="/download/51026" aria-label="Download51026"><i class="mdi mdi-download mdi-18px" style="color: #132f50"></i></a></td><td class=" text-center"></td><td class=" text-center"><i class="mdi mdi-close mdi-18px" style="color: #ec5e10"></i></td><td><a href="/exploits/51026">Open Web Analytics 1.7.3 - Remote Code Execution</a></td><td class=" text-center"><a href="#" value="webapps">WebApps</a></td><td class=" text-center"><a href="#" value="php">PHP</a></td><td class=" text-center"><a href="#">Jacob Ebben</a></td></tr>
        <tr role="row" class="odd"><td class=" text-center" tabindex="0">2022-10-17</td><td class=" text-center"><a href="/download/51025" aria-label="Download51025"><i class="mdi mdi-download mdi-18px" style="color: #132f50"></i></a></td><td class=" text-center"></td><td class=" text-center"><i class="mdi mdi-close mdi-18px" style="color: #ec5e10"></i></td><td><a href="/exploits/51025">Wordpress Plugin ImageMagick-Engine 1.7.4 - Remote Code Execution (RCE) (Authenticated)</a></td><td class=" text-center"><a href="#" value="webapps">WebApps</a></td><td class=" text-center"><a href="#" value="php">PHP</a></td><td class=" text-center"><a href="#">ABDO10</a></td></tr>
        <tr role="row" class="even"><td class=" text-center" tabindex="0">2022-10-06</td><td class=" text-center"><a href="/download/51024" aria-label="Download51024"><i class="mdi mdi-download mdi-18px" style="color: #132f50"></i></a></td><td class=" text-center"></td><td class=" text-center"><i class="mdi mdi-close mdi-18px" style="color: #ec5e10"></i></td><td><a href="/exploits/51024">Wordpress Plugin Zephyr Project Manager 3.2.42 - Multiple SQLi</a></td><td class=" text-center"><a href="#" value="webapps">WebApps</a></td><td class=" text-center"><a href="#" value="php">PHP</a></td><td class=" text-center"><a href="#">Rizacan Tufan</a></td></tr>
        <tr role="row" class="odd"><td class=" text-center" tabindex="0">2022-09-23</td><td class=" text-center"><a href="/download/51023" aria-label="Download51023"><i class="mdi mdi-download mdi-18px" style="color: #132f50"></i></a></td><td class=" text-center"></td><td class=" text-center"><i class="mdi mdi-close mdi-18px" style="color: #ec5e10"></i></td><td><a href="/exploits/51023">Testa 3.5.1 Online Test Management System - Reflected Cross-Site Scripting (XSS)</a></td><td class=" text-center"><a href="#" value="webapps">WebApps</a></td><td class=" text-center"><a href="#" value="php">PHP</a></td><td class=" text-center"><a href="#">Ashkan Moghaddas</a></td></tr>
        <tr role="row" class="even"><td class=" text-center" tabindex="0">2022-09-23</td><td class=" text-center"><a href="/download/51022" aria-label="Download51022"><i class="mdi mdi-download mdi-18px" style="color: #132f50"></i></a></td><td class=" text-center"></td><td class=" text-center"><i class="mdi mdi-close mdi-18px" style="color: #ec5e10"></i></td><td><a href="/exploits/51022">Aero CMS v0.0.1 - SQLi</a></td><td class=" text-center"><a href="#" value="webapps">WebApps</a></td><td class=" text-center"><a href="#" value="php">PHP</a></td><td class=" text-center"><a href="#">nu11secur1ty</a></td></tr>
        <tr role="row" class="odd"><td class=" text-center" tabindex="0">2022-09-23</td><td class=" text-center"><a href="/download/51021" aria-label="Download51021"><i class="mdi mdi-download mdi-18px" style="color: #132f50"></i></a></td><td class=" text-center"></td><td class=" text-center"><i class="mdi mdi-close mdi-18px" style="color: #ec5e10"></i></td><td><a href="/exploits/51021">Wordpress Plugin 3dady real-time web stats 1.0 - Stored Cross Site Scripting (XSS)</a></td><td class=" text-center"><a href="#" value="webapps">WebApps</a></td><td class=" text-center"><a href="#" value="php">PHP</a></td><td class=" text-center"><a href="#">UnD3sc0n0c1d0</a></td></tr>
        <tr role="row" class="even"><td class=" text-center" tabindex="0">2022-09-23</td><td class=" text-center"><a href="/download/51020" aria-label="Download51020"><i class="mdi mdi-download mdi-18px" style="color: #132f50"></i></a></td><td class=" text-center"></td><td class=" text-center"><i class="mdi mdi-close mdi-18px" style="color: #ec5e10"></i></td><td><a href="/exploits/51020">Wordpress Plugin WP-UserOnline 2.88.0 - Stored Cross Site Scripting (XSS)</a></td><td class=" text-center"><a href="#" value="webapps">WebApps</a></td><td class=" text-center"><a href="#" value="php">PHP</a></td><td class=" text-center"><a href="#">UnD3sc0n0c1d0</a></td></tr>
        <tr role="row" class="odd"><td class=" text-center" tabindex="0">2022-09-23</td><td class=" text-center"><a href="/download/51019" aria-label="Download51019"><i class="mdi mdi-download mdi-18px" style="color: #132f50"></i></a></td><td class=" text-center"></td><td class=" text-center"><i class="mdi mdi-close mdi-18px" style="color: #ec5e10"></i></td><td><a href="/exploits/51019">Teleport v10.1.1 - Remote Code Execution (RCE)</a></td><td class=" text-center"><a href="#" value="remote">Remote</a></td><td class=" text-center"><a href="#" value="multiple">Multiple</a></td><td class=" text-center"><a href="#">Brandon Roach</a></td></tr>
        <tr role="row" class="even"><td class=" text-center" tabindex="0">2022-09-23</td><td class=" text-center"><a href="/download/51018" aria-label="Download51018"><i class="mdi mdi-download mdi-18px" style="color: #132f50"></i></a></td><td class=" text-center"></td><td class=" text-center"><i class="mdi mdi-close mdi-18px" style="color: #ec5e10"></i></td><td><a href="/exploits/51018">Feehi CMS 2.1.1 - Remote Code Execution (Authenticated)</a></td><td class=" text-center"><a href="#" value="webapps">WebApps</a></td><td class=" text-center"><a href="#" value="php">PHP</a></td><td class=" text-center"><a href="#">yuyudhn</a></td></tr>
        <tr role="row" class="odd"><td class=" text-center" tabindex="0">2022-09-23</td><td class=" text-center"><a href="/download/51017" aria-label="Download51017"><i class="mdi mdi-download mdi-18px" style="color: #132f50"></i></a></td><td class=" text-center"></td><td class=" text-center"><i class="mdi mdi-close mdi-18px" style="color: #ec5e10"></i></td><td><a href="/exploits/51017">TP-Link Tapo c200 1.1.15 - Remote Code Execution (RCE)</a></td><td class=" text-center"><a href="#" value="webapps">WebApps</a></td><td class=" text-center"><a href="#" value="hardware">Hardware</a></td><td class=" text-center"><a href="#">hacefresko</a></td></tr>
        

'''