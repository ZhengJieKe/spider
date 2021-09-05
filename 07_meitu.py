import re

import requests,re,random  ##导入requests
from bs4 import BeautifulSoup  ##导入bs4中的BeautifulSoup
import os
import time



ROBOTSTXT_OBEY = False
COOKIES_ENABLED = False
# 爬取代理的url地址，选择的是西祠代理
url_ip = "http://www.xicidaili.com/nt/"

# 设定等待时间
set_timeout = 10

# 爬取代理的页数，2表示爬取2页的ip地址
num = 2

# 代理的使用次数
count_time = 5

# 构造headers
UserAgent_List = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]


def header(referer):
    headers = {
        'User-Agent': random.choice(UserAgent_List),
        'Referer': '{}'.format(referer),
    }
    return headers


def ip_test(ip, url_for_test='https://www.baidu.com', set_timeout=10):
    '''
    检测爬取到的ip地址可否使用，可以返回True，不可以返回False
    '''
    try:
        r = requests.get(url_for_test, headers=headers, proxies={'http': ip[0] + ':' + ip[1]}, timeout=set_timeout)
        if r.status_code == 200:
            return True
        else:
            return False
    except:
        return False


def scrawl_ip(url, num, url_for_test='https://www.baidu.com'):
    '''
    爬取代理ip地址，代理的url是西祠代理
    :param url:
    :param num:
    :param url_for_test:
    :return:
    '''
    ip_list = []
    for num_page in range(1, num + 1):
        url = url + str(num_page)
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        content = response.text
        pattern = re.compile('<td class="country">.*?alt="Cn" />.*?</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>', re.S)
        items = re.findall(pattern, content)
        for ip in items:
            if ip_test(ip[1], url_for_test):  # 测试爬取到ip是否可用，测试通过则加入ip_list列表之中
                print('测试通过，IP地址为' + str(ip[0]) + ':' + str(ip[1]))
                ip_list.append(ip[0] + ':' + ip[1])
        return ip_list
    time.sleep(5)  # 等待5秒爬取下一页


def get_random_ip():  # 随机获取一个IP
    ind = random.randint(0, len(total_ip) - 1)
    return total_ip[ind]


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
# headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
all_url = 'http://www.mzitu.com/all'  ##开始的URL地址

#all_url = 'https://www.4bnbn.net/all'
start_html = requests.get(all_url,headers=headers)  ##使用Requests中的get方法来获取all_url（就是：http://www.mzitu.com/all 这个地址）的内容，headers为上面设置的请求头，务必参考Requests官方文档解释
print(start_html.text)  ##打印出start_html(content是二进制的数据，一般用于下载图片、视频、音频等
Soup = BeautifulSoup(start_html.text, 'lxml')  ##使用BeautifulSoup来解析我们获取到的网页（‘lxml’是指定的解析器）
all_a1 = Soup.find('div', class_='all').find_all('a')
all_a1.remove(all_a1[0])
all_a = all_a1
total = 'total3'
# 爬取IP代理
total_ip = scrawl_ip(url_ip, num)
kkk=2# 这里的数字可以进行更换，初始为1，每次本段代码不能爬取图片了，结束运行，重新填写
turn=False
for lll in range(0,10000):
  if turn==False:
    mmm=kkk
    try:
      os.makedirs(os.path.join(total))  # 创建一个存放套图的文件夹
      os.chdir(total)  # 切换到上面创建的文件夹
      for kkk in range(mmm,len(all_a)):
          a=all_a[kkk]
          title = a.get_text() ##取出a标签文本
          #path=str(title).strip() #去掉空格
          path=title
          href= a['href'] #取出a标签的href属性
          #print title,href

          headers=header(href)
          html=requests.get(href,headers=headers)
          html_Soup=BeautifulSoup(html.text,'lxml')
          max_span=html_Soup.find('div',class_='pagenavi').find_all('span')[-2].get_text()
          for page in range(1,int(max_span)+1):
               page_url=href + '/'+ str(page)
               try_time=0
               proxy_flag=False
               if not proxy_flag:
                   try:
                        headers=header(page_url)
                        img_html =requests.get(page_url,headers=headers,timeout=10)
                        img_Soup=BeautifulSoup(img_html.text,'lxml')
                        img_url=img_Soup.find('div',class_='main-image').find('img')['src']
                        name =path + ' ' + img_url[-9:-4] #取url 倒数第四到第九位，加上a标签名作为名字
                        img= requests.get(img_url,headers = headers)
                        f = open(name+'.jpg','ab') #多媒体文件要用content
                        f.write(img.content) #多媒体文件要用content
                        f.close()
                   except:
                        proxy_flag=True
               else:
                    if try_time<count_time:
                        try:
                            print('尝试第'+str(try_time+1)+'次使用代理下载')
                            img_html =requests.get(page_url,headers=headers, proxies={'http': get_random_ip()},timeout=10)
                            img_Soup=BeautifulSoup(img_html.text,'lxml')
                            img_url=img_Soup.find('div',class_='main-image').find('img')['src']
                            name =path + ' ' + img_url[-9:-4] #取url 倒数第四到第九位，加上a标签名作为名字
                            img= requests.get(img_url,headers = headers)
                            if html.status_code==200:
                                print('图片通过IP代理处理成功！')
                                f = open(name+'.jpg','ab') #多媒体文件要用content
                                f.write(img.content) #多媒体文件要用content
                                f.close()
                            else:
                                try_time=(try_time + 1)
                        except:
                            print ('error')
               #f = open(name+'.jpg','ab') #多媒体文件要用content
               #f.write(img.content) #多媒体文件要用content
               #f.close()
    except:
      turn=False
