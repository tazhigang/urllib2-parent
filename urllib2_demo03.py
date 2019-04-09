import urllib.request as urllib2
if __name__ == '__main__':
    useragent_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36"
    }
    # 向指定的url发送数据请求，并返回服务器响应的类文件对象
    request = urllib2.Request("http://www.baidu.com/", headers=useragent_headers)
    response = urllib2.urlopen(request)
    # 服务器返回的文件对象对象支持python程序对其操作
    # read()读取返回的文件内容  返回值是一个bytes类型的数据
    code = response.getcode() # 获取响应的状态码
    print("code:%s"%code)
    print("*"*50)
    url = response.geturl() # 获取请求的url
    print("url:%s" % url)
    print("*" * 50)
    response_headers = response.info() # 获取响应的headers信息 返回值类型<class 'http.client.HTTPMessage'>
    print(type(response_headers))
    print("headers\n%s" % response_headers)
    print("*" * 50)
    response_headers_list = response.getheaders() # 获取响应的headers信息 返回值类型<class 'list'>
    print(type(response_headers_list))
    for header in response_headers_list:
        print(header)
    # 获取请求的报文信息
