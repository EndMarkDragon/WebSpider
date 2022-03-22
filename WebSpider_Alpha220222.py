import requests
from bs4 import BeautifulSoup

class ParameterError(Exception):    #参数错误（输入的参数有误）
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class URLError(Exception):     #网址错误（输入的网址有误）
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class ConnectError(Exception):      #连接错误（网络无法连接）
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class NoneElementsError(Exception):      #不存在目标元素
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class WebSpider:
    def __init__(self, url, name="unnamed", mode="get"):
        #防止参数错误
        if mode != "get" and mode != "post":
            raise ParameterError("Parameter \"mode\" could only be \"get\" or \"post\".")
        self.name = name
        self.url = url
        self.mode = mode

    def get_url(self):
        return self.url

    def get_name(self):
        return self.name

    def is_connected():     #是否连接（判断是否与url正常连接）
        #判断状态码
        try:
            if self.mode == "get":
                status = requests.get(self.url).status_code
            else:
                status = requests.post(self.url).status_code
        except:
            raise URLError("URLError:Please use the correct url.")
        if status == 200:
            return True     #连接正常
        else:
            return False    #连接异常

    def catch_page(self, mode="text"):    #抓取网站（抓取网站页面内容）
        """
        #确认网络连接正常
        connected = self.is_connected
        if connected:
            raise ConnectError("ConnectError:Unable to connect to the network.")
        """
        #防止参数错误
        if mode == "text":
            resp = requests.get(self.url).text.encode("raw_unicode_escape")
        elif mode == "content":
            resp = requests.get(self.url).content.encode("raw_unicode_escape")
        else:
            raise ParameterError("ParameterError:Parameter \"mode\" could only be \"text\" or \"content\".")
        #再编码
        resp = resp.decode(errors="ignore")
        try:     #尝试读写
            path = "Download\\TestedDownload\\%s.html"%self.name     #文件路径
            with open(path, "w") as file:
                file.write(resp)
            return True, resp     #读写正常
        except BaseException:
            return False, None    #读写异常

    def catch_head(self, mode="text"):    #抓取网站<head>标签内容
        """
        #确认网络连接正常
        connected = self.is_connected
        if connected:
            raise ConnectError("ConnectError:Unable to connect to the network.")
        """
        #防止参数错误
        if mode == "text":
            resp = requests.get(self.url).text.encode("raw_unicode_escape")
        elif mode == "content":
            resp = requests.get(self.url).content.encode("raw_unicode_escape")
        else:
            raise ParameterError("ParameterError:Parameter \"mode\" could only be \"text\" or \"content\".")
        #再编码
        resp = resp.decode(errors="ignore")
        #抓取网站<head>标签
        soup = BeautifulSoup(resp, "html.parser")
        try:
            head = list(soup.find_all("head"))
        except BaseException:
            raise NoneElementsError("This page hasn't got a element with a \"<head>\" tag.")
        try:     #尝试读写
            path = "Download\\TestedDownload\\%s.head.html"%self.name     #文件路径
            with open(path, "w") as file:
                for i in range(len(head)):
                    file.write(str(head[i]))
                    file.write("\n\n\n\n")
            return True, "\n\n".join(head)     #读写正常
        except BaseException:
            return False, None    #读写异常

    def catch_title(self, mode="text"):    #抓取网站<title>标签内容
        """
        #确认网络连接正常
        connected = self.is_connected
        if connected:
            raise ConnectError("ConnectError:Unable to connect to the network.")
        """
        #防止参数错误
        if mode == "text":
            resp = requests.get(self.url).text.encode("raw_unicode_escape")
        elif mode == "content":
            resp = requests.get(self.url).content.encode("raw_unicode_escape")
        else:
            raise ParameterError("ParameterError:Parameter \"mode\" could only be \"text\" or \"content\".")
        #再编码
        resp = resp.decode(errors="ignore")
        #抓取网站<title>标签
        soup = BeautifulSoup(resp, "html.parser")
        try:
            title = list(soup.find_all("title"))
        except BaseException:
            raise NoneElementsError("This page hasn't got a element with a \"<title>\" tag.")
        try:     #尝试读写
            path = "Download\\TestedDownload\\%s.title.html"%self.name     #文件路径
            with open(path, "w") as file:
                for i in range(len(title)):
                    file.write(str(title[i]))
                    file.write("\n\n\n\n")
            return True, "\n\n".join(title)     #读写正常
        except BaseException:
            return False, None    #读写异常

    def catch_meta(self, mode="text"):    #抓取网站<meta>标签内容
        """
        #确认网络连接正常
        connected = self.is_connected
        if connected:
            raise ConnectError("ConnectError:Unable to connect to the network.")
        """
        #防止参数错误
        if mode == "text":
            resp = requests.get(self.url).text.encode("raw_unicode_escape")
        elif mode == "content":
            resp = requests.get(self.url).content.encode("raw_unicode_escape")
        else:
            raise ParameterError("ParameterError:Parameter \"mode\" could only be \"text\" or \"content\".")
        #再编码
        resp = resp.decode(errors="ignore")
        #抓取网站<meta>标签
        soup = BeautifulSoup(resp, "html.parser")
        try:
            meta = list(soup.find_all("meta"))
        except BaseException:
            raise NoneElementsError("This page hasn't got a element with a \"<meta>\" tag.")
        try:     #尝试读写
            path = "Download\\TestedDownload\\%s.meta.html"%self.name     #文件路径
            with open(path, "w") as file:
                for i in range(len(meta)):
                    file.write(str(meta[i]))
                    file.write("\n\n\n\n")
            return True, "\n\n".join(meta)     #读写正常
        except BaseException:
            return False, None    #读写异常

    def catch_span(self, mode="text"):    #抓取网站<span>标签内容
        """
        #确认网络连接正常
        connected = self.is_connected
        if connected:
            raise ConnectError("ConnectError:Unable to connect to the network.")
        """
        #防止参数错误
        if mode == "text":
            resp = requests.get(self.url).text.encode("raw_unicode_escape")
        elif mode == "content":
            resp = requests.get(self.url).content.encode("raw_unicode_escape")
        else:
            raise ParameterError("ParameterError:Parameter \"mode\" could only be \"text\" or \"content\".")
        #再编码
        resp = resp.decode(errors="ignore")
        #抓取网站<span>标签
        soup = BeautifulSoup(resp, "html.parser")
        try:
            span = list(soup.find_all("span"))
        except BaseException:
            raise NoneElementsError("This page hasn't got a element with a \"<span>\" tag.")
        try:     #尝试读写
            path = "Download\\TestedDownload\\%s.span.html"%self.name     #文件路径
            with open(path, "w") as file:
                for i in range(len(span)):
                    file.write(str(span[i]))
                    file.write("\n\n\n\n")
            return True, "\n\n".join(span)     #读写正常
        except BaseException:
            return False, None    #读写异常
