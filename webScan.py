#coding = utf-8
#auth 暗
#create 2021-11-14
import requests
import urllib.request
from urllib import error
import random
#随机获取一个代理
def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()
#删除代理
def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))
#获取代理总数
def get_proxy_count():
    return requests.get("http://127.0.0.1:5010/count/").json()
#初始化
def init():
    #随机ua
    user_agent_list = [
        # Firefox
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        # Safari
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        # QQ浏览器
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0)",
    ]
    user_agent = random.choice(user_agent_list)
    url = input("输入你要扫描到的网址：(http://www.baidu.com)")
    dir = input("输入字典的完整路径：")
    get_scan(user_agent,url,dir);

def get_scan(url_agent,url,dir):
    #请求头
    headers = {
        "User-Agent":url_agent
    }
    url_list =[]
    if dir !="":
        try:
            with open(dir,'r')as f:
                for a in f:
                    a = a.replace('\n','')
                    url_list.append(a)
                f.close()
        except Exception as e:
            print(e)
    for data in url_list:
        ip = get_proxy().get("proxy")
        dst_url = url + data
        try:
            response = requests.get(dst_url,headers=headers, proxies = {'http' : 'http://'+ip})
            print("%s-----%s" %(dst_url,response)+'代理ip：'+ip)
            delete_proxy(ip)
        except Exception as e:
            print("%s-----%s" %(dst_url,e))  
if __name__ == '__main__':
    init()

