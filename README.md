# 猎鹰python爬虫
爬取【 "http://www.pss-system.gov.cn” 】 中华为公司的专利号

# 文件夹
- Google专利
  * 专利基本信息
    主要爬取google专利网站 【https://patents.google.com/】 ，包括专利号、IPC分类、申请国、pdf地址、申请日、公开日、引用、引用链接、被引用、被引用链接等信息；
  * 专利综合信息
    在基本信息的基础上，增加了 Patent Citations、Cited By、Similar Documents三张表
- 专利公开号
  在国家专利局网址上爬取，完整的各个公司专利号；
- 多层级投资公司
  * 投资公司名单
  在天眼查网站，爬取一家公司的一级、二级、三级...n级投资公司详情；
  * 补充程序
  在-投资公司名单-程序运行失败时，运行此程序；
- 工商信息
  * 企业工商信息
  在天眼查网站，爬取一家公司的全部工商信息，包括'公司名称','电话号码','公司网址','公司简介','经营状态','营业期限','实缴资本','地址','经营范围'等等；
  * 工商信息收集补充程序
   在-企业工商信息-程序运行失败时，运行此程序；
  

# 需要的python工具包
* time
* selenium
* chrome浏览器
* pandas

# 结果
返回Excel文件
