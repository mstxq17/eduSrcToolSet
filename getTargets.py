#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import json
import os
from selenium import webdriver

# host = "https://api.eol.cn:443/"
# query_url = "gkcx/api/?access_token=&admissions=&central=&department=&dual_class=&f211=&f985=&is_doublehigh=&is_dual_class=&keyword=&nature=&page={page}&province_id=&request_type=1&school_type=&signsafe=&size={size}&sort=view_total&type=&uri=apidata/api/gk/school/lists"

# command = """curl -i -s -k -X $'POST' \
#     -H $'Host: api.eol.cn' -H $'Connection: close' -H $'Content-Length: 299' -H $'Accept: application/json, text/plain, */*' -H $'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36' -H $'Content-Type: application/json;charset=UTF-8' -H $'Origin: https://gkcx.eol.cn' -H $'Sec-Fetch-Site: same-site' -H $'Sec-Fetch-Mode: cors' -H $'Sec-Fetch-Dest: empty' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: zh-CN,zh;q=0.9,ja;q=0.8' \
#     --data-binary $'{{\"access_token\":\"\",\"admissions\":\"\",\"central\":\"\",\"department\":\"\",\"dual_class\":\"\",\"f211\":\"\",\"f985\":\"\",\"is_doublehigh\":\"\",\"is_dual_class\":\"\",\"keyword\":\"\",\"nature\":\"\",\"page\":1,\"province_id\":43,\"request_type\":1,\"school_type\":\"\",\"size\":15,\"sort\":\"view_total\",\"type\":\"\",\"uri\":\"apidata/api/gk/school/lists\"}}' \
#     $'https://api.eol.cn/gkcx/api/?access_token=&admissions=&central=&department=&dual_class=&f211=&f985=&is_doublehigh=&is_dual_class=&keyword=&nature=&page={page}&province_id=43&request_type=1&school_type=&signsafe=&size={size}&sort=view_total&type=&uri=apidata/api/gk/school/lists'"""
# school_dict = {}
# for p in range(0, 10):
#     response_text = os.popen(command.format(page=p, size=15)).read().split("\n")
#     body_text = response_text[-1]
#     school_list = json.loads(body_text)['data']['item']
#     for sl in school_list:
#         school_name,school_id = sl['name'], sl['school_id']
#         school_dict[school_id] = school_name
# print(len(school_dict))
# print(school_dict)

# # 获取主域名
# _host = 'https://gkcx.eol.cn/school/'
# shool_url = []
# for key in school_dict.keys():
#     shool_url.append(_host + str(key))
# print(shool_url)
url = "https://gkcx.eol.cn/school/2479"
browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver2.3')
browser.get(url)
# print(browser.page_source)
# soup = BeautifulSoup(browser.page_source, 'html.parser')
# print(soup.find)
elem = browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div[2]/div/div/div[3]/div[2]/div[4]/div[1]/span[2]/a[1].href')
print(elem)
browser.close()


