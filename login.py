# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author:      datadt
@DateTime:    2018-07-24 12:21:34
'''


from selenium import webdriver
import re
import urllib.request
import time
from  PIL import Image
from pytesseract import *
import requests
from PIL import ImageGrab
from retrying import retry


#全局变量
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')
browser = webdriver.Chrome(chrome_options=chrome_options)

def initTable(threshold=140):
	table = []#降噪，图片二值化
	for i in range(256):
		if i < threshold:
			table.append(0)
		else:
			table.append(1)
	return table

def login(url):
	browser.get(url)

#如果验证码识别错误登录就会有问题，重新执行输入用户名、密码及验证码功能,允许试错3次
@retry(stop_max_attempt_number=3)
def log():
	browser.find_element_by_id("username").clear()
	browser.find_element_by_id("username").send_keys('xxxxxx')#用户名
	browser.find_element_by_id("password").clear()
	browser.find_element_by_id("password").send_keys('******')#密码
	vcode=image_to_string(ImageGrab.grab((1460,525,1532,558)).convert('L').point(initTable(66), '1'),config='-psm 7')#注意截图位置(与分辨率有关)，ID=7是输出模式之一
	while len(vcode)!=4:#逻辑判断
		browser.find_element_by_css_selector('#form_group_validatecode > div > div > img').click()#刷新验证码
		time.sleep(1)
		vcode=image_to_string(ImageGrab.grab((1460,525,1532,558)).convert('L').point(initTable(66), '1'),config='-psm 7')
	
	browser.find_element_by_id("validatecode").clear()
	browser.find_element_by_id("validatecode").send_keys(vcode)#输入验证码
	browser.find_element_by_css_selector("body > table > tbody > tr > td > div > div > div > div > div > form > button").submit()#登陆按钮确认
	return browser.current_url#跳转后，返回当前网址

def dzt():
	try:
		login(url)
		while log()!='https://www.dianzhentan.com/member/':
			log()#登陆成功会跳转的网址
	except:
		print("重置中……")
	finally:
		time.sleep(55)
		browser.quit()#close只会关闭当前窗口,quit退出驱动并关闭所关联的所有窗口


if __name__ == '__main__':
	url='https://www.dianzhentan.com/base/'
	dzt()
