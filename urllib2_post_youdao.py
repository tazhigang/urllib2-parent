import urllib.request as urllib2
import urllib
import time
import uuid

if __name__ == '__main__':
    i = input("请输入你要翻译的词语:")
    # 抓包获取请求头构造请求头
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    # 抓包获取请求地址
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule "
    # 构造请求的formdata数据
    timestamp = "%s" % int(time.time() * 1000)
    sign = str(uuid.uuid4()).replace("-", "")
    salt = "%s" % int(time.time() * 10000)
    formdata = {
        "i": i,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt": salt,
        "sign": sign,
        "ts": timestamp,
        "bv": "7bc3e056c1a81131c5d3435f6b9dc4c5",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
        "typoResult": "false"
    }
    # 将formdata数据转化为二进制的数据  网路传输只能支持二进制的数据传输
    data = bytes(urllib.parse.urlencode(formdata),encoding="utf8")
    print(type(data))
    # 构造请求 如果有data参数则表示是post请求
    request = urllib2.Request(url,data=data,headers=headers)
    response = urllib2.urlopen(request)
    # 将相应回来的数据输出
    response_json = str(bytes(response.read()).decode("utf-8")).replace(" ","")
    print(response_json)