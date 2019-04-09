import urllib.request as urllib2
import urllib
import random

# http://tieba.baidu.com/f?kw=%E4%B8%83%E9%BE%99%E7%8F%A0&ie=utf-8&pn=100
user_agent_list = [
    # "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
    # "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
    # "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    # "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    # "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36"
]
def load_url_page(full_url,filename):
    """
    爬取页面的
    :param url:目标页面的url
    :return: 返回爬取的页面内容
    """
    print("正在爬取页面:%s" % urllib.parse.unquote(full_url))
    user_agent = random.choice(user_agent_list)
    request = urllib2.Request(full_url)
    request.add_header("User-Agent",user_agent)
    print("正在下载%s" %filename)
    response = urllib2.urlopen(request)
    print("下载%s完成" % filename)
    return response.read()

def save_html_to_local(html,filename):
    """
    将下载好的页面保存到本地
    :param html:
    :param filename:
    """
    print("正在保存%s" % filename)
    with open("baidu/tieba/%s" %filename,"wb") as file:
        file.write(html)
    print("保存%s完成" % filename)
    print("="*50)
def tieba_spider(url,begin_page,end_page):
    """
    百度贴吧爬取工具
    :param url:
    :param begin_page: 起始页
    :param end_page: 结束页
    """
    print(url)
    for page in range(begin_page,end_page + 1):
        pn = (page-1)*50
        pn_key_value = "&pn=%d" % pn
        full_url = url + pn_key_value
        html = load_url_page(full_url,"page%d.html" % page)
        save_html_to_local(html,"page%d.html" % page)

    print("感谢使用爬虫......")


if __name__ == '__main__':
    kw = input("请输入爬取的贴吧名:")
    begin_page = int(input("请输入爬取的起始页:"))
    end_page = int(input("请输入爬取的结束页:"))

    url="https://tieba.baidu.com/f?"
    kw_value = urllib.parse.quote(kw)
    kw_key_value = "kw=%s" % kw_value
    append_url = url + kw_key_value
    tieba_spider(append_url,begin_page,end_page)