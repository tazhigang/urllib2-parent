import urllib.request as urllib2
if __name__ == '__main__':
    # 向指定的url发送数据请求，并返回服务器响应的类文件对象
    response = urllib2.urlopen("http://www.baidu.com")
    # 服务器返回的文件对象对象支持python程序对其操作
    # read()读取返回的文件内容  返回值是一个bytes类型的数据
    html = response.read()
    with open("baidu/index.html","wb") as file:
        file.write(html)