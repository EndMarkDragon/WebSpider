这是`WebSpider`的简体中文帮助文档，英语版本在下方。

It's the Simplified Chinese help documentation of `WebSpider`. The English version is  below.


# `WebSpider`库`Alpha`版本说明文档（简体中文）

## 简介
`WebSpider`是一款基于`requests` `BeautifulSoup4` `re`三个库的轻量化、便捷化python第三方库，`WebSpider`库提供了多种方法，以提供python在爬虫方面的简便和快捷。

## 历史更新记录
以下各历史版本中带有`BV`或`BugVersion`标签的是`WebSpider`的不稳定版本，在使用过程中可能会出现崩溃现象，请谨慎使用。

以下各历史版本中带有`IU`或`InternalUse`标签的是`WebSpider`的内部版本，不会对外发布，但确有此版本。

以下各历史版本中带有`HL`或`HaveLost`标签的是`WebSpider`的已丢失版本，该版本由于管理不当等原因丢失，但历史上确有此版本。

以下各历史版本中带有`FML`或`Formal`标签的是`WebSpider`的正式版本（在大版本号下的推荐版本），已确认无BUG，可以放心使用。

### `WebSpider`库`Alpha`版本更新记录
`WebSpider` `Alpha`版是`WebSpider`研发的初步版本，所支持的功能非常有限（初期版本为初二时制作）。

|           版本号           |    制作日期    |                                                                                       说明                                                                                       |
|:-----------------------:|:----------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| `WebSpider_Alpha220222` | 2022年2月22日 |                                                                `BV`;这是`WebSpider`的第一个版本，自此萌发了开启`WebSpider`工程的想法                                                                |
| `WebSpider_Alpha220314` | 2022年3月14日 |         `IU`;这是`WebSpider`第二个版本，静态页面基础功能已经较为完善，新增了多个函数和一个`HtmlString`类，用于根据其id，类名，快速查找，修复了`WebSpider-Alpha220222`版本中抓取页面部分同标签元素返回值错误的BUG，但在抓取动态页面上仍有所欠缺(注：不支持`path`标签)         |
| `WebSpider_Alpha220323` | 2022年3月23日 | 这是`WebSpider`的第三个版本，将`HtmlString`更名为`HtmlElement`，以保证翻译的准确性，并且将`HtmlElement`对Html的支持更换为对Html数个元素与Html页面的支持，增加`HtmlElement`的一个函数，并更改`WebSpider`类的函数返回值为`HtmlElement`，向文件中添加了注释。 |

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

# `WebSpider` Library `Alpha` Version Description Document(English)

I'm a chinese student of Grade Eight, and my English isn't very well, so the help documentation of `WebSpider` is translated by translation software. Please understand.

## Introduction

`WebSpider` is a lightweight and convenient third-party Python Library Based on `requests` `BeautifulSoup4` `re`. The`WebSpider` library provides a variety of methods to provide python with simplicity and quickness in terms of crawlers.

## History update record

Among the following historical versions, those labeled with `BV` or `BugVersion` are unstable versions of `WebSpider`, which may crash during use. Please use them with caution.

The `IU` or `InternalUse` labels in the following historical versions are the internal versions of `WebSpider`, which will not be released to the public, but this version does exist.

In the following historical versions, the missing version of `WebSpider` with the label of `HL` or `HaveLost` is the version lost due to improper management and other reasons, but this version does exist in history.

Among the following historical versions, the official version of `WebSpider` (the recommended version under the large version number) with the label of `FML` or `formal` has been confirmed to be free of bugs and can be used safely.

### `Webspider` Library `Alpha` version update record

The `Alpha` version of `WebSpider` is a preliminary version developed by 'webspider', which supports very limited functions (the initial version is made in the second day of junior high school).



|      Version number      |  production date  |                                                                                                                                                                                                                                description                                                                                                                                                                                                                                |
|:------------------------:|:-----------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| `WebSpider_Alpha220222`  | February 22, 2022 |                                                                                                                                                                         `BV`; This is the first version of `WebSpider`, and the idea of starting the `WebSpider` project has sprouted since then                                                                                                                                                                          |
| `WebSpider_Alpha220314 ` |  March 14, 2022   | `IU`; This is the second version of `WebSpider`. The basic functions of static pages have been improved. Several functions and a `HtmlString` class have been added to quickly find and fix the bug in the version of `WebSpider_Alpha220222` that grabs the wrong return value of the same tag element in the page part according to its ID and class name. However, there are still some deficiencies in grabbing dynamic pages (Note: the `path` tag is not supported) |
| `WebSpider_Alpha220323 ` |  March 23, 2022   |                                   this is the third version of `WebSpider`. Change the name of `HtmlString` to `HtmlElement` to ensure the accuracy of translation, and replace the support of `HtmlElement` for HTML with the support of several HTML elements and HTML pages . Add a function of `HtmlElement`，and change the return value of the function of the `WebSpider` class to `HtmlElement`, added comments to the file.                                       |
