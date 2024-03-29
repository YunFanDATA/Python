# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 00:41:07 2019
@author: 京道投资
本程序用于爬取天眼查企业的投资信息和该被投资企业主页的url
"""

# -*- coding:utf-8 -*-
# author: kevin
# CreateTime: 2018/8/16
# software-version: python 3.7


import time
from selenium import webdriver
from selenium.webdriver import Chrome
import os
import pandas as pd
import json
from selenium.webdriver.common.by import By  #引用网页选择器
from selenium.webdriver.support.ui import WebDriverWait  #引用设定显示等待时间
from selenium.webdriver.support import expected_conditions as EC
import sys

def get_company_info(company_name):
    """
    第一次进入天眼查公司的主页
    """
    index_input_company = driver.find_element_by_xpath('//input[@id="home-main-search"]')  # 主页搜索框
    index_input_company.send_keys(company_name)
    driver.find_element_by_xpath('//*[@id="web-content"]/div/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div').click()  # 点击搜索
    time.sleep(4)
    try:
        company_list = driver.find_element_by_xpath('.//div[contains(@class, "header")][1]/a[1]') # 获取当前页面所有公司的div
        href = company_list.get_attribute('href')
        driver.get(href)  # 进入公司详情页 //*[@id="company_web_top"]/div[2]/div[3]/div[1]/h1
        print('已进入%s主页' %(company_name))
    except:
        print('没有搜索到相应的公司')
        return company_name

def enter_company(company_name):
    """
    之后在其他公司页面进入公司的主页
    """
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[1]/img').click()
    index_input_company = driver.find_element_by_xpath('//*[@id="header-company-search"]')  # 主页搜索框
    index_input_company.send_keys(company_name)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div').click()  # 点击搜索
    time.sleep(6)
    company_list = driver.find_element_by_xpath('.//div[contains(@class, "header")][1]/a[1]') # 获取当前页面所有公司的div
    href = company_list.get_attribute('href')
    driver.get(href)  # 进入公司详情页
    print('已进入%s主页' %(company_name))

    

def get_company_invest():
    """
    得到公司全部投资信息
    """
    all_num = [2,4,5,6,7,8,9,10]
    try:
        '''
        head_name = driver.find_elements_by_xpath('//*[@id="_container_pastInverstCount"]/table/thead/tr/th')
        names = []
        for name in head_name:
            names.append(name.text)
        ''' 
        trs = driver.find_elements_by_xpath('//*[@id="_container_invest"]/div/table/tbody/tr')
        name = []
        percentage = []
        url = []
        for tr in trs:
            name.append(tr.find_element_by_css_selector('a.link-click').text)
            percentage.append(tr.find_element_by_xpath('td[6]/span').text)
            url.append(tr.find_element_by_css_selector('a.link-click').get_attribute('href'))
        invest_table = pd.DataFrame([name,percentage,url]).T
        #拼接多余表格
        try:
            num = int(driver.find_elements_by_css_selector('span.data-count')[2].text)//20+1
            num = num-1
            list_n = all_num[:num-1] 
        except:
            num = 1
        if num<2:
            pass
            #invest_table.columns = names
        else:
            for j in list_n:
                string = '//*[@id="_container_invest"]/div/div/ul/li[' +str(j)+ ']/a'
                submitBtn = driver.find_element_by_xpath(string)
                driver.execute_script("arguments[0].scrollIntoView(false)", submitBtn)
                driver.execute_script("window.scrollBy(0, 100)")
                driver.find_element_by_xpath(string).click()
                time.sleep(6)
                trs = driver.find_elements_by_xpath('//*[@id="_container_invest"]/div/table/tbody/tr')
                name = []
                percentage = []
                url = []
                for tr in trs:
                    name.append(tr.find_element_by_css_selector('a.link-click').text)
                    percentage.append(tr.find_element_by_xpath('td[6]/span').text)
                    url.append(tr.find_element_by_css_selector('a.link-click').get_attribute('href'))
                invest_table = invest_table.append(pd.DataFrame([name,percentage,url]).T)
        return invest_table
    except:
        print('没有对外投资名单')
        return pd.DataFrame()
    

if __name__ == '__main__':
    # tt = GetCompanyInfo()
    # 得到cookies
    with open('cookies.json', 'r', encoding='utf-8') as f:
        listCookies = json.loads(f.read())
    #启动浏览器
    driver = Chrome()
    start_url = 'https://www.tianyancha.com'
    driver.get(start_url)
    time.sleep(5)
    for cookie in listCookies:
        driver.add_cookie(cookie)
    driver.refresh()
    #开始程序
    company="深圳嘉道谷投资管理有限公司"
    get_company_info(company)
    time.sleep(6)
    head_names = ['invested_company','percentage','url']
    invest_table = get_company_invest()
    invest_table.columns = head_names
    invest_table['company'] = company
    all_company = []
    i = 1
    writer = pd.ExcelWriter('投资公司名单.xlsx')
    invest_table.to_excel(writer, sheet_name='第1级',index=False)
    while True:
        if invest_table.empty or i>10:
            break
        else:
            i += 1
            table = pd.DataFrame()
            for j in invest_table['invested_company']:
                if j not in all_company:
                    all_company.append(j)
                    time.sleep(6)
                    enter_company(j)
                    time.sleep(6)
                    data = get_company_invest()
                    if not data.empty:
                        data.columns = head_names
                        data['company'] = j
                    print(data)
                    table = table.append(data)
            invest_table = table
            sheet_name1 = '第' + str(i)+'级'
            invest_table.to_excel(writer, sheet_name=sheet_name1,index=False)   
    #writer.save()
    #writer.close()
    #driver.quit()
'''
#此部分程序用于获取cookie并通过json模块将dict转化成str
#运行程序前，需要手动登入天眼查账号和密码
#账号：18959203391
#密码：data2019
dictCookies = driver.get_cookies()
jsonCookies = json.dumps(dictCookies)
# 登录完成后，将cookie保存到本地文件
with open('cookies.json', 'w') as f:
    f.write(jsonCookies)
'''
