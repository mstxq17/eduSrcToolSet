#! /usr/bin/python
# -*- coding:utf-8 -*-
# 通过接口去反查注册域名获取根资产

import urllib2,requests
import time
from bs4 import  BeautifulSoup

class root(object):
    def __init__(self):
        self.set_aizhan = set()
        self.set_aizhan2 = set()
        self.set_aizhan3 = set()
        self.set_bugscaner = set()

    # 统一调用接口
    def get_root_url(self,url):
    	self.aizhan(url)
    	self.aizhan2(url)
    	self.aizhan3(url)
    	self.bugscaner(url)
    	# 取并集
    	total_rootdomain = self.set_aizhan | self.set_aizhan2 | self.set_aizhan3 | self.set_bugscaner
    	# 返回总结果
    	return total_rootdomain


    def aizhan(self,url):
        print '[+]Record number reverse checking'
        self.set_aizhan.add(url)
        url1 = 'https://icp.aizhan.com/%s/'%url
        try:
            r = urllib2.urlopen(url1).read()
            b = BeautifulSoup(r,'lxml')
            for i in b.find_all('span',class_='blue'):
                if '<br/>' in str(i):
                        a = str(i).replace('\t','').replace('<br/>','\n').replace('<span class="blue">\n','').replace('</span>','').split()
                        for i in a:
                            self.set_aizhan.add(i.strip('www.'))
                else:
                    try:
                        self.set_aizhan.add(i.string.strip().strip('www.'))
                    except:pass
                continue
            return self.set_aizhan
        except:print '[-]aizhan:error'

    def aizhan2(self,url):
        try:
            print '[+]Email reverse checking'
            url = 'https://www.aizhan.com/cha/%s/'%url
            r = urllib2.urlopen(url).read()
            b = BeautifulSoup(r,'lxml')
            for i in b.find_all('a', target='_blank'):
                if 'reverse-whois' in str(i) and 'emailCode' in str(i):
                    urla = i['href']
                    r = urllib2.urlopen(urla).read()
                    b1 = BeautifulSoup(r,'lxml')
                    for a in b1.find_all('a', rel='nofollow'):
                        if 'www.miibeian.gov.cn' not in str(a):
                            self.set_aizhan2.add(a.string)
                    for x in b1.find_all('a'):
                        if 'whois.aizhan.com/reverse-whois' in str(x):
                            url1 = x['href']
                            url = urllib2.urlopen(url1)
                            time.sleep(1)
                            b = BeautifulSoup(url.read(), 'lxml')
                            for q in b.find_all('a', rel='nofollow'):
                                if 'www.miibeian.gov.cn' not in str(q):
                                    self.set_aizhan2.add(q.string)
        except:print '[-]aizhan2:error'
        return self.set_aizhan2

    def aizhan3(self,url):
        print '[+]registrant reverse checking'
        try:
            url = 'https://www.aizhan.com/cha/%s/'%url
            r = urllib2.urlopen(url).read()
            b = BeautifulSoup(r,'lxml')
            for i in b.find_all('a',target='_blank'):
                if 'reverse-whois' in str(i) and 'registrant' in str(i):
                    url1 = i['href']
                    r = requests.get(url1).text
                    b1 = BeautifulSoup(r,'lxml')
                    for a in b1.find_all('a',rel='nofollow'):
                        if 'www.miibeian.gov.cn' not in str(a):
                            self.set_aizhan3.add(a.string)
        except:print '[-]aizhan3:error'
        return self.set_aizhan3

    def bugscaner(self,url):
        print '[+]bugscaner Email reverse checking'
        try:
            rurl = 'http://whois.bugscaner.com/'
            r = requests.get(url=rurl + url).content
            b = BeautifulSoup(r, 'lxml')
            for i in b.find_all('a', class_='btn btn-success'):
                if 'email' in i['href']:
                    emailurl = rurl + i['href']
                    r1 = requests.get(emailurl).content
                    b1 = BeautifulSoup(r1, 'lxml')
                    tbody = b1.find_all('tbody')
                    for url in BeautifulSoup(str(tbody), 'lxml').find_all('a'):
                        if '/register/' not in url['href'] and '/email/' not in url['href']:
                            self.set_bugscaner.add(url.string)
        except:print '[-]bugscaner error'
        return self.set_bugscaner