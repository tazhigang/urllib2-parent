import urllib.request as urllib2

if __name__ == '__main__':
    # 是否开启代理
    proxy_switch =True
    # 代理的处理兑现创建
    # 如果是购买的代理有用户名与密码的时候需要 重新拼接例如{"http/https":"username:password@代理ip:代理端口"}
    # 如:{"https":"aaaaa:123456@163.125.157.173:8888"}
    proxy_handler = urllib2.ProxyHandler({"http":"163.125.157.173:8888"})
    # 空代理
    null_proxy_handler = urllib2.ProxyHandler({})

    if proxy_switch:
        opener = urllib2.build_opener(proxy_handler)
    else:
        opener = urllib2.build_opener(null_proxy_handler)
    # 发送请求
    request = urllib2.Request("http://www.baidu.com/")
    response = opener.open(request)
    # 打印响应数据
    print(str(bytes(response.read()).decode("utf-8")))