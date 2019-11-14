'''
爬取花千骨小说
'''
#导入爬取网页模块
from urllib import request
from bs4 import BeautifulSoup
#设置用户代理
header = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
}
for page in range(268,497):
    # 1.设置URL地址
    url = "https://www.23wx.so/55_55628/30242%d.html"%page
    # 3.设置请求
    req = request.Request(url, headers=header)
    # 打开网页
    response = request.urlopen(req)
    # 读取网页信息
    html = response.read()
    '''内容解析'''
    # 7.解析网页内容
    soup = BeautifulSoup(html, "html.parser")
    # 8.获取信息内容
    soup_title = str(soup.find('title'))
    soup_text = str(soup.find('div', id="content"))
    flag = soup_text.find("<br/>")
    context = soup_text[flag + 10:]
    context = context.replace("<br/>", "")
    context = context.replace("<br>", "")
    context = context.replace("</br>", "")
    context = context.replace("</div>", "")
    soup_title = soup_title[7:-18]
    file = open("hqg/%s" % soup_title, "w", encoding="utf-8")
    file.write(context)
    file.close()
