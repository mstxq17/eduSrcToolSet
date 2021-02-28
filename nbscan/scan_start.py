#!/usr/bin/python
# -*- coding:utf-8 -*-

import threading
import Queue
from root_domain import root
from subdomain import subdomain

# 构建个队列
queue_ = Queue.Queue()
# 获取ip
def get_ip(url): 
    url1 = "http://www.ip138.com/ips138.asp?ip=%s&action=2" % url
    r = requests.get(url1,timeout=1).content
    b = BeautifulSoup(r, 'lxml')
    for i in b.find_all('font'):
        if url in str(i):
            return i.string.split('>>')[1].strip()
# 多线程类
class MyThread(threading.Thread):
	def __init__(self, func):
		super(MyThread, self).__init__()
		self.func = func
	def run(self):
		self.func()

def worker():
	global queue_
	while not queue_.empty():
		task = queue.get()
		url = task.split('+')[0]
		try:
			title = BeautifulSoup(requests.get('http://' + url, timeout=1).content, 'lxml').title
			ip = get_ip(url.split(':')[0])
			if title == None:
				title = 'None'
		except:
			pass

def thread_start(subdomain_total):
	global queue_
	thread_count = 100
	threads = []
	ports = [80, 8080, 8000, 8081, 7001, 8089]
	for domain in list(subdomain_total):
		for port in ports:
			# 存任务
			queue_.put(url + ':' + str(port))
	for i in range(thread_count):
		# 多线程实例
		thread = MyThread(worker)
		thread.start()
		threads.append(thread)
	for thread in threads:
		# 控制最后输出
		thread.join()


def scan_start(url):
	# 获取根资产
	total_rootdomain = root().get_root_url(url)
	# 获取子域名,保存在subdomain_total
	subdomain_total = set()
	for item in list(total_rootdomain):
		# 字符串处理
		item = str(item)
		subdomain_total = subdomain_total | subdomain(item).get_subdomain()
	# 多线程验证存活状态 多线程效率比较高,采用队列控制
	thread_start(subdomain_total)
	# 在多线程中处理数据库存储操作



if __name__ == '__main__':
	url = 'uc.cn'
	scan_start(url)