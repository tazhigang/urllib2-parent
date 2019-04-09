import urllib.request as urllib2

if __name__ == '__main__':
    # 构造header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36",
    }
    # 构造url地址
    url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20"
    # 构造请求
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    data_txt = str(bytes(response.read()).decode("utf-8"))
    print(data_txt)
    with open("douban/data.json", "wb") as file:
        file.write(html)