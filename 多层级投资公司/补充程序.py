# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 23:13:07 2019

@author: 京道基金
本程序作为补充程序，出现机器人页面时候或者程序出错中断时，运行此程序
"""
import pandas as pd

'''
i = 1 #填入开始丢失的前一级
company = '陕西科强军民融合创新研究院有限公司' #填入开始丢失的公司名称

order = '第'+str(i) +'级'
order2 = '第'+str(i+1) +'级'
sheet = pd.read_excel('投资公司名单.xlsx',sheet_name=order,header=0)
n = list(sheet['invested_company']).index(company) #
invest_table = sheet.iloc[(n+1):,:]
table = pd.read_excel('投资公司名单.xlsx',sheet_name=order2,header=0)

with open('cookies.json', 'r', encoding='utf-8') as f:
    listCookies = json.loads(f.read())
#启动浏览器
driver = Chrome()
driver.get(start_url)
for cookie in listCookies:
    driver.add_cookie(cookie)
driver.refresh()
get_company_info('华为')
#writer = pd.ExcelWriter('投资公司名单.xlsx')
'''
company = j 
sheet = invest_table
n = list(sheet['invested_company']).index(company)
invest_table = sheet.iloc[n:,:]
i = i-1

while True:
    if invest_table.empty or i>10:
        break
    else:
        i += 1
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
        table = pd.DataFrame()
        sheet_name1 = '第' + str(i)+'级'
        invest_table.to_excel(writer, sheet_name=sheet_name1,index=False)   

#writer.save()
#writer.close()
#driver.quit()