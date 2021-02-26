#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 用于获取一级域名

import tldextract
from urllib.parse import urlparse


def Test():
    url = 'm.windowscentral.com'
    # 一级域名
    domain = tldextract.extract(url).domain
    # 二级域名
    subdomain = tldextract.extract(url).subdomain
    # 后缀
    suffix = tldextract.extract(url).suffix
    print("获取到的一级域名:{}".format(domain))
    print("获取到二级域名:{}".format(subdomain))
    print("获取到的url后缀:{}".format(suffix))

def main():
    Test()
    main_domains = []
    filename  = "target.txt"
    with open(filename, 'r') as f1, open("ok.txt", 'w') as f2:
        for url in f1:
            u = urlparse(url.strip()).netloc
            domain = tldextract.extract(u).domain + '.' +tldextract.extract(url).suffix
            f2.write(domain + '\n')
    print("Done!")
if __name__ == '__main__':
    main()