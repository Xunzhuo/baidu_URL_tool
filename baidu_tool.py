#!/usr/bin/python
# -*- coding: UTF-8 -*-
# tool used for repeat submit urls
__author__ = '1900'

import os
import time
import logging

post_time = 1

re_try = 50 # 服务器错误之后重新尝试的次数 默认50次
Your_website = "www.liuxunzhuo.tech" # the url record in your baidu_website
Your_token = "ek5T1WJ6SXqZgoKU" # find it in your baidu_token
sleep_time = 1 # 默认每隔1秒请求一次

logging.basicConfig(level = logging.INFO, format = '%(asctime)s -%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

while 1:	
	response = os.popen("curl -H 'Content-Type:text/plain' --data-binary @urls.txt \"http://data.zz.baidu.com/urls?site="+Your_website+"&token="+Your_token+"\"").readlines()

	logger.info("The "+str(post_time)+"`s request" + str(response))
	if "over quota" in str(response):
		logger.error("Today post max URLS , See You Tomorrow ~ ")
		break
	elif "empty content" in str(response):
		logger.error("Make sure tool.py and url.txt in the same Directory ~ ")
		break
	elif "only 2000 urls are allowed once" in str(response):
		logger.error("Only 2000 urls are allowed once, resize your urls.txt ")
		break
	elif "site error"  in str(response):
		logger.error("Y")
	elif "401" or "404" in str(response):
		logger.error("Token or Your_website is not valid , Check your Token  or Your_website")
		break
	elif "500" in str(response):
		logger.warning("Server Problems , Automatically Re-Try")
		if re_try > 0:
			re_try = re_try - 1 
			pass
		else:
			break
	time.sleep(sleep_time)
	post_time = post_time + 1

logger.info("Finished")
