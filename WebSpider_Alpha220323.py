import re
from time import sleep
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

class HtmlElement(str):
    def __init__(self, string):
        self.string = string

    def show(self):
        return self.string

    def choose_by_class(self, class_name):
        pattern = "<.* class=\"%s\" .*>?"%class_name
        result = re.search(pattern, self.string)
        if result == None:
            return None
        else:
            result_list = []
            try:
                num = 0
                while True:
                    result_list.append(result.group(num))
                    sleep(0.5)
                    num += 1
            except:
                pass
            return result_list

    def choose_by_id(self, id_name):
        pattern = "<.* id=\"%s\" .*>?" % id_name
        result = re.search(pattern, self.string)
        if result == None:
            return None
        else:
            result_list = []
            try:
                num = 0
                while True:
                    result_list.append(result.group(num))
                    sleep(0.5)
                    num += 1
            except:
                pass
            return result_list

    def choose_by_name(self, name):
        pattern = "<.* name=\"%s\" .*>?"%name
        result = re.search(pattern, self.string)
        if result == None:
            return None
        else:
            result_list = []
            try:
                num = 0
                while True:
                    result_list.append(result.group(num))
                    sleep(0.5)
                    num += 1
            except:
                pass
            return result_list

    def choose_by_href(self, href):
        pattern = "<.* href=\"%s\" .*>?" %href
        result = re.search(pattern, self.string)
        if result == None:
            return None
        else:
            result_list = []
            try:
                num = 0
                while True:
                    result_list.append(result.group(num))
                    sleep(0.5)
                    num += 1
            except:
                pass
            return result_list

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
            return True, HtmlElement(resp)     #读写正常
        except BaseException:
            return False, HtmlElement("")    #读写异常

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
            path = "Download\\TestedDownload\\%s.meta.html" % self.name  # 文件路径
            text = ""
            with open(path, "w") as file:
                for i in range(len(head)):
                    file.write(str(head[i]))
                    file.write("\n\n\n\n")
                    text = text + str(head[i])
                    text = text + "\n\n\n\n"
            return True, HtmlElement(text)  # 读写正常
        except BaseException:
            return False, HtmlElement("")    #读写异常

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
            path = "Download\\TestedDownload\\%s.meta.html" % self.name  # 文件路径
            text = ""
            with open(path, "w") as file:
                for i in range(len(title)):
                    file.write(str(title[i]))
                    file.write("\n\n\n\n")
                    text = text + str(title[i])
                    text = text + "\n\n\n\n"
            return True, HtmlElement(text)  # 读写正常
        except BaseException:
            return False, HtmlElement("")    #读写异常

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
            text = ""
            with open(path, "w") as file:
                for i in range(len(meta)):
                    file.write(str(meta[i]))
                    file.write("\n\n\n\n")
                    text = text + str(meta[i])
                    text = text + "\n\n\n\n"
            return True, HtmlElement(text)  # 读写正常
        except BaseException:
            return False, HtmlElement("")    #读写异常

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
            text = ""
            with open(path, "w") as file:
                for i in range(len(span)):
                    file.write(str(span[i]))
                    file.write("\n\n\n\n")
                    text = text + str(span[i])
                    text = text + "\n\n\n\n"
            return True, HtmlElement(text)     #读写正常
        except BaseException:
            return False, HtmlElement("")    #读写异常

    def catch_p(self, mode="text"):    #抓取网站<p>标签内容
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
        #抓取网站<p>标签
        soup = BeautifulSoup(resp, "html.parser")
        try:
            p = list(soup.find_all("p"))
        except BaseException:
            raise NoneElementsError("This page hasn't got a element with a \"<p>\" tag.")
        try:     #尝试读写
            path = "Download\\TestedDownload\\%s.p.html"%self.name     #文件路径
            text = ""
            with open(path, "w") as file:
                for i in range(len(p)):
                    file.write(str(p[i]))
                    file.write("\n\n\n\n")
                    text = text + str(p[i])
                    text = text + "\n\n\n\n"
            return True, HtmlElement(text)     #读写正常
        except BaseException:
            return False, HtmlElement("")    #读写异常

    def catch_h(self, h_num, mode="text"):    #抓取网站<h>标签内容
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
        #抓取网站<h~>标签
        soup = BeautifulSoup(resp, "html.parser")
        try:
            h = list(soup.find_all("h%s"%str(h_num)))
        except BaseException:
            raise NoneElementsError("This page hasn't got a element with a \"<h>\" tag.")
        try:     #尝试读写
            path = "Download\\TestedDownload\\%s.h%s.html"%(self.name, h_num)     #文件路径
            text = ""
            with open(path, "w") as file:
                for i in range(len(h)):
                    file.write(str(h[i]))
                    file.write("\n\n\n\n")
                    text = text + str(h[i])
                    text = text + "\n\n\n\n"
            return True, HtmlElement(text)     #读写正常
        except BaseException:
            return False, HtmlElement("")    #读写异常

    def catch_table(self, mode="text"):    #抓取网站<table>标签内容
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
        #抓取网站<table>标签
        soup = BeautifulSoup(resp, "html.parser")
        try:
            table = list(soup.find_all("table"))
        except BaseException:
            raise NoneElementsError("This page hasn't got a element with a \"<table>\" tag.")
        try:     #尝试读写
            path = "Download\\TestedDownload\\%s.table.html"%self.name     #文件路径
            text = ""
            with open(path, "w") as file:
                for i in range(len(table)):
                    file.write(str(table[i]))
                    file.write("\n\n\n\n")
                    text = text + str(table[i])
                    text = text + "\n\n\n\n"
            return True, HtmlElement(text)     #读写正常
        except BaseException:
            return False, HtmlElement("")    #读写异常

    def catch_div(self, mode="text"):    #抓取网站<div>标签内容
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
        #抓取网站<div>标签
        soup = BeautifulSoup(resp, "html.parser")
        try:
            div = list(soup.find_all("div"))
        except BaseException:
            raise NoneElementsError("This page hasn't got a element with a \"<div>\" tag.")
        try:     #尝试读写
            path = "Download\\TestedDownload\\%s.div.html"%self.name     #文件路径
            text = ""
            with open(path, "w") as file:
                for i in range(len(div)):
                    file.write(str(div[i]))
                    file.write("\n\n\n\n")
                    text = text + str(div[i])
                    text = text + "\n\n\n\n"
            return True, HtmlElement(text)     #读写正常
        except BaseException:
            return False, HtmlElement("")    #读写异常

    def catch_font(self, mode="text"):    #抓取网站<font>标签内容
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
        #抓取网站<font>标签
        soup = BeautifulSoup(resp, "html.parser")
        try:
            font = list(soup.find_all("font"))
        except BaseException:
            raise NoneElementsError("This page hasn't got a element with a \"<font>\" tag.")
        try:     #尝试读写
            path = "Download\\TestedDownload\\%s.font.html"%self.name     #文件路径
            text = ""
            with open(path, "w") as file:
                for i in range(len(font)):
                    file.write(str(font[i]))
                    file.write("\n\n\n\n")
                    text = text + str(font[i])
                    text = text + "\n\n\n\n"
            return True, HtmlElement(text)     #读写正常
        except BaseException:
            return False, HtmlElement("")    #读写异常

    def catch_body(self, mode="text"):    #抓取网站<body>标签内容
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
        #抓取网站<body>标签
        soup = BeautifulSoup(resp, "html.parser")
        try:
            body = list(soup.find_all("body"))
        except BaseException:
            raise NoneElementsError("This page hasn't got a element with a \"<body>\" tag.")
        try:     #尝试读写
            path = "Download\\TestedDownload\\%s.body.html"%self.name     #文件路径
            text = ""
            with open(path, "w") as file:
                for i in range(len(body)):
                    file.write(str(body[i]))
                    file.write("\n\n\n\n")
                    text = text + str(body[i])
                    text = text + "\n\n\n\n"
            return True, HtmlElement(text)     #读写正常
        except BaseException:
            return False, HtmlElement("")    #读写异常

    def catch_script(self, mode="text"):    #抓取网站<script>标签内容
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
        #抓取网站<script>标签
        soup = BeautifulSoup(resp, "html.parser")
        try:
            script = list(soup.find_all("script"))
        except BaseException:
            raise NoneElementsError("This page hasn't got a element with a \"<script>\" tag.")
        try:     #尝试读写
            path = "Download\\TestedDownload\\%s.script.html"%self.name     #文件路径
            text = ""
            with open(path, "w") as file:
                for i in range(len(script)):
                    file.write(str(script[i]))
                    file.write("\n\n\n\n")
                    text = text + str(script[i])
                    text = text + "\n\n\n\n"
            return True, HtmlElement(text)     #读写正常
        except BaseException:
            return False, HtmlElement("")    #读写异常

    def catch_svg(self, mode="text"):    #抓取网站<svg>标签内容
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
        #抓取网站<svg>标签
        soup = BeautifulSoup(resp, "html.parser")
        try:
            svg = list(soup.find_all("svg"))
        except BaseException:
            raise NoneElementsError("This page hasn't got a element with a \"<svg>\" tag.")
        try:     #尝试读写
            path = "Download\\TestedDownload\\%s.svg.html"%self.name     #文件路径
            text = ""
            with open(path, "w") as file:
                for i in range(len(svg)):
                    file.write(str(svg[i]))
                    file.write("\n\n\n\n")
                    text = text + str(svg[i])
                    text = text + "\n\n\n\n"
            return True, HtmlElement(text)     #读写正常
        except BaseException:
            return False, HtmlElement("")    #读写异常

    def catch_symbol(self, mode="text"):    #抓取网站<symbol>标签内容
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
        #抓取网站<symbol>标签
        soup = BeautifulSoup(resp, "html.parser")
        try:
            symbol = list(soup.find_all("symbol"))
        except BaseException:
            raise NoneElementsError("This page hasn't got a element with a \"<symbol>\" tag.")
        try:     #尝试读写
            path = "Download\\TestedDownload\\%s.symbol.html"%self.name     #文件路径
            text = ""
            with open(path, "w") as file:
                for i in range(len(symbol)):
                    file.write(str(symbol[i]))
                    file.write("\n\n\n\n")
                    text = text + str(symbol[i])
                    text = text + "\n\n\n\n"
            return True, HtmlElement(text)     #读写正常
        except BaseException:
            return False, HtmlElement("")    #读写异常

    def catch_main(self, mode="text"):    #抓取网站<main>标签内容
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
        #抓取网站<main>标签
        soup = BeautifulSoup(resp, "html.parser")
        try:
            main = list(soup.find_all("main"))
        except BaseException:
            raise NoneElementsError("This page hasn't got a element with a \"<main>\" tag.")
        try:     #尝试读写
            path = "Download\\TestedDownload\\%s.main.html"%self.name     #文件路径
            text = ""
            with open(path, "w") as file:
                for i in range(len(main)):
                    file.write(str(main[i]))
                    file.write("\n\n\n\n")
                    text = text + str(main[i])
                    text = text + "\n\n\n\n"
            return True, HtmlElement(text)     #读写正常
        except BaseException:
            return False, HtmlElement("")    #读写异常

    def catch_section(self, mode="text"):    #抓取网站<section>标签内容
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
        #抓取网站<section>标签
        soup = BeautifulSoup(resp, "html.parser")
        try:
            section = list(soup.find_all("section"))
        except BaseException:
            raise NoneElementsError("This page hasn't got a element with a \"<section>\" tag.")
        try:     #尝试读写
            path = "Download\\TestedDownload\\%s.section.html"%self.name     #文件路径
            text = ""
            with open(path, "w") as file:
                for i in range(len(section)):
                    file.write(str(section[i]))
                    file.write("\n\n\n\n")
                    text = text + str(section[i])
                    text = text + "\n\n\n\n"
            return True, HtmlElement(text)     #读写正常
        except BaseException:
            return False, HtmlElement("")    #读写异常

    def catch_iframe(self, mode="text"):    #抓取网站<iframe>标签内容
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
        #抓取网站<iframe>标签
        soup = BeautifulSoup(resp, "html.parser")
        try:
            iframe = list(soup.find_all("iframe"))
        except BaseException:
            raise NoneElementsError("This page hasn't got a element with a \"<iframe>\" tag.")
        try:     #尝试读写
            path = "Download\\TestedDownload\\%s.iframe.html"%self.name     #文件路径
            text = ""
            with open(path, "w") as file:
                for i in range(len(iframe)):
                    file.write(str(iframe[i]))
                    file.write("\n\n\n\n")
                    text = text + str(iframe[i])
                    text = text + "\n\n\n\n"
            return True, HtmlElement(text)     #读写正常
        except BaseException:
            return False, HtmlElement("")    #读写异常

    def catch_a(self, mode="text"):    #抓取网站<a>标签内容
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
        #抓取网站<a>标签
        soup = BeautifulSoup(resp, "html.parser")
        try:
            a = list(soup.find_all("a"))
        except BaseException:
            raise NoneElementsError("This page hasn't got a element with a \"<a>\" tag.")
        try:     #尝试读写
            path = "Download\\TestedDownload\\%s.a.html"%self.name     #文件路径
            text = ""
            with open(path, "w") as file:
                for i in range(len(a)):
                    file.write(str(a[i]))
                    file.write("\n\n\n\n")
                    text = text + str(a[i])
                    text = text + "\n\n\n\n"
            return True, HtmlElement(text)     #读写正常
        except BaseException:
            return False, HtmlElement("")    #读写异常

    def catch_link(self, mode="text"):    #抓取网站<link>标签内容
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
        #抓取网站<link>标签
        soup = BeautifulSoup(resp, "html.parser")
        try:
            link = list(soup.find_all("link"))
        except BaseException:
            raise NoneElementsError("This page hasn't got a element with a \"<link>\" tag.")
        try:     #尝试读写
            path = "Download\\TestedDownload\\%s.link.html"%self.name     #文件路径
            text = ""
            with open(path, "w") as file:
                for i in range(len(link)):
                    file.write(str(link[i]))
                    file.write("\n\n\n\n")
                    text = text + str(link[i])
                    text = text + "\n\n\n\n"
            return True, HtmlElement(text)     #读写正常
        except BaseException:
            return False, HtmlElement("")    #读写异常

def main():
    bilibili = WebSpider("https://www.bilibili.com/", name="bilibili")
    page = bilibili.catch_page()
    if page[0] == True:
        result = page[1].show()
    else:
        result = None
    print(result)

if __name__ == "__main__":
    main()
