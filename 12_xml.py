#-*-coding:utf-8-*-

from lxml import etree
import urllib2
import random
import time
import os

class TeiBa_spider(object):
    def __init__(self):

        self.header_list = [
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        ]

        self.proxy_ip = [


            ]


    def open_url(self,h_url):
        html_requset = urllib2.Request(url=h_url,headers={"User-Agent":random.choice(self.header_list)})
        html_respon  = urllib2.urlopen(html_requset)
        #print html_respon.read()
        return html_respon.read()

    def fil_url(self,html_re):
        html_data = etree.HTML(html_re)
        html_data_url_list = html_data.xpath('//img[@class="BDE_Image"]/@src')
        #print html_data_url
        return html_data_url_list

    def dload_jpg(self,Url_list):
        url_list = Url_list
        os.mkdir('./picture')
        for i in url_list:
            print i
            jpg_data = self.open_url("%s"%i)
            file_name ='./picture/'+ i[-9:]
            #print file_name
            try:
                with open(file_name,'wb+') as file_jpg:
                    file_jpg.write(jpg_data)

######################出现错误时生成log日志
            except Exception as result:
                file_name_log = 'log'+ str(time.gmtime()[0:3]) + ".txt"
                with open(file_name_log,'a+') as log:
                    result =str(result) + '\r'
                    log_time = str(time.gmtime()[0:3])
                    log.write(log_time + result)
                print (result)



    def save_jpg(self):
        pass

def test():
    url_list = []
    test_fun = TeiBa_spider()
    for i in range(1,39):
        data =test_fun.open_url("https://tieba.baidu.com/p/3185527263?pn=%d"%i)
        list = test_fun.fil_url(data)
        for i in list:
            url_list.append(i)

    test_fun.dload_jpg(url_list)


if __name__ == "__main__":
    test()
