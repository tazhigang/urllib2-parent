import urllib.request as urllib2
from lxml import html
import re
import os


# 获取笑话的url:http://xiaohua.zol.com.cn/lengxiaohua/
#          第一页：http://xiaohua.zol.com.cn/lengxiaohua/
#          第二页：http://xiaohua.zol.com.cn/lengxiaohua/2.html
# 获取详情的url:http://xiaohua.zol.com.cn/detail60/59364.html


# 笑话内容链接列表: //span[@class="article-title"]/a/@href
# 获取单个链接的内容名称 //h1[@class="article-title"]
# 获取单个链接的内容 //div[@class="article-text"]

user_agent_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36"
}


class SpiderXiaoHua(object):
    def __init__(self,start_pagenum,end_pagenum,host):
        self.start_pagenum = start_pagenum
        self.end_pagenum = end_pagenum
        self.host = host

    def load_page(self,uri,category,pagenum):
        """
        加载列表页面，获取详情页的链接
        :param uri:
        :param category:
        :param pagenum:
        :return:
        """
        request = urllib2.Request("%s%s"%(self.host,uri),headers=user_agent_headers)
        print("%s%s"%(self.host,uri))
        response = urllib2.urlopen(request)
        # 将获取到的内容通过gbk解码以后，在转码成utf-8的字符串
        res_html = str((bytes(response.read()).decode("gbk")).encode("utf-8"))
        # lxml4.3.3中创建etree的方法变为 lxml.html.etree
        content = html.etree.HTML(res_html)
        # 获取详情页的；链接列表
        link_list = content.xpath('//span[@class="article-title"]/a/@href')
        for link in link_list:
            self.load_detail("%s%s"%(self.host,link),category,pagenum)

    def load_detail(self,url,category,pagenum):
        """
        加载详情页，获取详情页的标题与内容
        :param url:
        :param category:
        :param pagenum:
        :return:
        """
        request = urllib2.Request(url, headers=user_agent_headers)
        response = urllib2.urlopen(request)
        res_html = str(bytes(response.read()).decode("gbk"))
        content = html.etree.HTML(res_html)
        title = content.xpath('//h1[@class="article-title"]/text()')
        xiaohua_content = content.xpath('//div[@class="article-text"]')
        pattern = re.compile(" ")
        xiaohua_txt = pattern.sub("",r"%s"%str(xiaohua_content[0].xpath('string()')))
        self.write_txt(title[0],xiaohua_txt,category,pagenum)

    def write_txt(self,title,xiaohua_txt,category,pagenum):
        """
        将获取到的页面内容及标题写入目标文件夹及文件中
        :param title:
        :param xiaohua_txt:
        :param category:
        :param pagenum:
        :return:
        """
        xiaohua_bytes = bytes(xiaohua_txt, encoding="utf-8")
        txt_name = title.replace("?","").replace(":","")
        flag = os.path.exists("%s/%s"%(category,pagenum))
        if not flag:
            os.makedirs("%s/%s"%(category,pagenum))
        if not os.path.exists("%s/%s/%s.txt" %(category,pagenum,txt_name)):
            print("正在写入文件:%s.txt" % title)
            with open("%s/%s/%s.txt" % (category, pagenum, txt_name), "wb") as file:
                file.write(xiaohua_bytes)
            print("%s.txt写入完成" % title)
        else:
            print("%s.txt已经存在，跳过此文件的下载" % title)
        print("=" * 50)
    def start_work(self,uri,category):
        """
        爬取入口
        :param uri:
        :param category:
        :return:
        """
        for num in range(self.start_pagenum,self.end_pagenum+1):
            print("开始爬取%s的第%s页 地址:%s%s%s.html"%(category,num,self.host,uri,num))
            self.load_page("%s%s.html"%(uri,num),category,num)
            print("爬取%s的第%s页结束" % (category, num))

if __name__ == '__main__':
    print("""
        host:http://xiaohua.zol.com.cn
        1.lengxiaohua
        2.youmo
    """)
    category_dict = {
        "1":["lengxiaohua","/lengxiaohua/"],
        "2":["youmo","/youmo/"]
    }
    categoryId = input("请输入爬取的类别:1 or 2(提示:如果日选择其他则默认选择爬取冷笑话)")

    category_name = category_dict.get(categoryId)[0]
    category_uri = category_dict.get(categoryId)[1]
    try:
        start_pagenum = int(input("请输入爬取的起始页:(提示:如果输入非数字，则默认选择第一页)"))
        end_pagenum = int(input("请输入爬取的结束页:(提示:如果输入的不合法则默认只爬取第一页)"))
    except Exception:
        start_pagenum = 1
        end_pagenum = 1
    else:
        if start_pagenum > end_pagenum:
            start_pagenum = 1
            end_pagenum = 1

    spider_xiaohua = SpiderXiaoHua(start_pagenum,end_pagenum,"http://xiaohua.zol.com.cn")
    spider_xiaohua.start_work(category_uri,category_name)