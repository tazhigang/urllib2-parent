import urllib.request as urllib2

if __name__ == '__main__':
    # 创建一个httphandler的处理对象，支持处理http请求
    http_handler = urllib2.HTTPHandler()
    # 构建一个人opener对象
    opener = urllib2.build_opener(http_handler)

    request = urllib2.Request("http://www.baidu.com/")
    # 发送请求，获取响应对象
    response = opener.open(request)
    print(response.read())
    