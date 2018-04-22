# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:15:12 2018

@author: 10566
"""

import requests
import re
login_url = 'http://jcjx.nuaa.edu.cn/EaWeb/Manager/login.aspx'
gpa_url= 'http://jcjx.nuaa.edu.cn/EaWeb/Manager/Module/NetEa/Score/View/List.aspx'
loginout_url = 'http://jcjx.nuaa.edu.cn/EaWeb/Manager/LogOut.aspx'
finaly_url = 'http://jcjx.nuaa.edu.cn/'
string = r'</td><td>.*?</td><td>.*?</td><td>.*?</td><td>(.*?)</td><td>.*?</td><td>.*?</td><td>.*?</td><td>.*?</td><td>.*?</td><td>.*?</td><td>.*?</td><td align=.*?>(.*?)</td><td>(.*?)</td><td>&nbsp;</td><td>.*?</td><td>&nbsp;</td><td class=.*?>.*?</td><td>.*?</td><td align=.*?></td>'

headers = {
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
         }
datas = {
         #需要用浏览器f12查看源码获得	
         '__VIEWSTATE':'/wEPDwUKMTk2MDIxNjYyMQ9kFgICAQ9kFg4CAw8PFgIeBFRleHQFDeeUqOaIt+S/oeaBrzpkZAIFDw8WAh8ABQrnlKjmiLflkI06ZGQCBw8PFgIeB1Rvb2xUaXAFC+eUqOaIt+WQjX4hZGQCCQ8PFgIfAAUZ5a+GJm5ic3A7Jm5ic3A7Jm5ic3A756CBOmRkAg0PDxYCHwEFEeivt+i+k+WFpeWvhueggX4hZGQCDw9kFgICAQ8PFgQfAAUK6aqM6K+B56CBOh4HVmlzaWJsZWhkZAIRDxYCHwJoFgICAw8PFgQfAAUf6L6T5YWl5LiK5Zu+5Lit5pi+56S655qE5a2X5q+NOh8BBSDovpPlhaXkuIrlm77kuK3mmL7npLrnmoTlrZfmr41+IWRkZLbz5krRVZpoIQP39w73tLag7aeQWNZH0vwLUvTwgaDg',
         '__VIEWSTATEGENERATOR':'F06ECFDD',
         '__EVENTTARGET':'',	
         '__EVENTARGUMENT':'',
         #需要用浏览器f12查看源码获得	
         '__EVENTVALIDATION':'/wEdAAiSmY8p09aB1nODv8JBWmnwlibaeQDnkgycOnwxQ9R8LpqoLZXC1IsNhYhq9lHZSM6RlF5bQv1uhLV/Y3hStNgePu7NRiPFoaVZ4Xq9PBqkCde8p0gLoFiQcHhKBp3osN4/PCZGtJJUspPJdVDDbJljHPhzIXC5UPjobxlXfltx2SEr8qvH68qwjZ7FCAgw0WvDNdH2NYZfPmfBVSYboj/J',
         'LocalIP':'171.118.93.132',
         'hfAccompanyLogin':'',	
         'Account':'学号md5码',#不确定使用了什么加密方式所以需要用浏览器f12查看源码获得
         'textName':'学号',
         'PwdStrengthLevel':'1',
         'LoginPass':'密码md5',#不确定使用了什么加密方式所以需要用浏览器f12查看源码获得
         'textPwd':'密码',
         'ButtonOK':'确定'
           }
sessions = requests.session()
def login():
    response = sessions.post(login_url,data=datas,headers = headers)
    print(response.url)
    #resp = sessions.get(response.url)
    #print (resp.text)
    
def auto_get():
    gpa_view = sessions.get(gpa_url)
    jd = re.search()
    while(1):
        return
        
        
    
def get_gpa(yxy):
    print (yxy.text)
    res = re.findall(string, yxy.text)
    
    class_name = []
    class_grade = []
    class_credit = []
    print (res)
    for item in res:
        class_name.append(item[0])
        class_grade.append(item[1])
        class_credit.append(item[2])
        print('科目:%s' % (item[0].strip()))
        print("成绩:%s%10s学分:%5s" % (item[1].strip(),' ', item[2].strip()))
        #print record
    return res
        
def loginout():
    out = sessions.get(loginout_url)
    if out.url == finaly_url:
        print('已成功退出教务网')
    sessions.close
    
def main():
    login()
    gpa_view = sessions.get(gpa_url)
    get_gpa(gpa_view)
    loginout()
    return
    
if __name__ == '__main__':
    main()
    
    
    
    


    















