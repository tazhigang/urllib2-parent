from urllib import request as urllib2

if __name__ == '__main__':
    ua_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36"
    }
    # 通过urllib2中的Request构造一个请求对象
    request = urllib2.Request("http://www.baidu.com",headers=ua_headers)
    response = urllib2.urlopen(request)
    # 读取服务器返回的文件
    html = response.read()
    html_txt = str(bytes(html).decode("utf-8"))
    with open("imooc.html","wb") as file:
        file.write(html)
    print(html_txt)