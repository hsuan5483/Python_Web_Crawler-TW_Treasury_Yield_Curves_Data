#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Pei-Hsuan Hsu
"""

import os
from os.path import join
import time

# 爬蟲套件
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# 當下資料夾路徑
path = os.getcwd()
# 輸出資料夾路徑
out = join(path, 'OTC treasury bill')

def set_browser(save_path):
    # 設定儲存位置
    options = webdriver.ChromeOptions() 
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': save_path}
    options.add_experimental_option('prefs', prefs)
    
    # chrome 模擬器位置
    driverpath = '/Users/hsuan/opt/selenium chrome driver/chromedriver'
    browser = webdriver.Chrome(executable_path=driverpath, chrome_options=options)#模擬瀏覽器
    
    #連上網頁
    link = "https://www.tpex.org.tw/web/bond/tradeinfo/govbond/GovBondDaily_02.php?l=zh-tw"#網址
    browser.get(link)#get方式進入網站
    time.sleep(2)#網站有loading時間
    
    return browser

for year in range(2009,2020):
    
    save_path = join(out, str(year))
    if not os.path.exists(save_path):
        os.makedirs(save_path)
        
    browser = set_browser(save_path)
    
    for mon in range(1,13):
        
        #選擇年份
        select_year = Select(browser.find_element_by_id('inputY'))#年份選單定位
        select_year.select_by_value(str(year))#年份選單項目定位
        
        #選擇月份
        select_mon = Select(browser.find_element_by_id('inputM'))#月份選單定位
        select_mon.select_by_value(str(mon))#月份選單項目定位
        
        #網頁資訊
#        page_source = browser.page_source
        
        #取得所有'下載XLS'按鈕
        Bottoms=browser.find_elements_by_link_text('下載XLS')#查詢按鈕定位
        for bottom in Bottoms:
            bottom.click()#模擬點擊
            time.sleep(2)
        
    browser.close()

