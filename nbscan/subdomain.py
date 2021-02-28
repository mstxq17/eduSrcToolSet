#!/usr/bin/python
# -*- coding:utf-8 -*-
# 遍历根资产的子域名

import sys
import requests
import threading
import time,json,re
from bs4 import BeautifulSoup

class subdomain(object):
    def __init__(self,url):
        self.url = url
        self.set_dns = set()
        self.set_ip138 = set()
        self.set_crt = set()
        self.set_baidu = set()
        self.set_find = set()

    # 统一调用接口
    def get_subdomain(self):
        # 调用5个线程
        threads = []
        threads.append(threading.Thread(target=self.dns))
        threads.append(threading.Thread(target=self.ip138))
        threads.append(threading.Thread(target=self.crt))
        threads.append(threading.Thread(target=self.baidu))
        threads.append(threading.Thread(target=self.find))
        for i in threads:
        	i.start()
        for i in threads:
        	i.join()
    	subdomain_total =  self.set_dns | self.set_ip138 | self.set_crt | self.set_baidu | self.set_find
    	return subdomain_total

    def dns(self):
        url = 'https://www.virustotal.com/vtapi/v2/domain/report?apikey=0ad3c01b1ff7952bc8cbb4370ef4a0c53201d2daffe113efb1d2fef484e16e58&domain=' + self.url
        try:
            r = requests.get(url)
            time.sleep(10)
            r_dict = json.loads(r.text)
            for i in r_dict['subdomains']:
                 set_dns.add(i)
            print '[!]subdomain:'+str(len(dns_set))
            return set_dns
        except:
            print '[-]subdomains:error'
            return 
    #virustotal dns

    def ip138(self):
        url1 = 'http://site.ip138.com/%s/domain.htm'%self.url
        try :
            r = requests.get(url1)
            b = BeautifulSoup(r.content,'lxml')
            for i in b.find_all('a',href=re.compile('%s'%self.url),target='_blank',rel=''):
                self.set_ip138.add(i.string)
            print '[!]ip138:'+ str(len(ip138_set))
            return self.set_ip138
        except:
            print '[-]IP137 interface failed'
            return 

    #ip137 interface

    def crt(self):
        url1 = 'https://crt.sh/?q=%25.' + self.url
        try:
            r = requests.get(url1).content
            b = BeautifulSoup(r,'lxml')
            for i in b.find_all('td',class_='',style=''):
                if '</a>' not in str(i) and '*.' not in str(i):
                    self.set_crt.add(i.string)
            print '[!]crt:' + str(len(crt_set))
            return self.set_crt
        except:
            print '[-]crt interface failed'
            return 

    def baidu(self):
        url_r = 'http://ce.baidu.com/index/getRelatedSites?site_address=%s' % self.url
        try:
            r = requests.get(url_r).content
            jr = json.loads(r)
            urls = jr['data']
            for url in urls:
                url = url['domain']
                self.set_baidu.add(url)
            print '[!]baidu:%s' % str(len(baidu_set))
            return self.set_baidu
        except:
            print 'Baidu interface failed'
            return 
    def find(self):
        url = 'https://findsubdomains.com/subdomains-of/%s'%self.url
        try:
            r = requests.get(url).content
            b = BeautifulSoup(r, 'lxml')
            for c in b.find_all(attrs={'class': 'js-domain-name domains', 'class': 'domains js-domain-name'}):
                self.set_find.add(c.string.strip())
            print '[!]find:' + str(len(find_set))
            return self.set_find
        except:
            print '[-]find interface failed'
            return 