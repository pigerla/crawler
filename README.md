crawler
=======

> 这是一个python爬虫项目，基于Scrapy框架，仅供学习。
> 准备知识：python语法知识，Scrapy框架知识，你常要跟网页打交道的，所以最好懂一些**前端知识**，再者，你要把数据存起来来吧，做持久化处理吧，所以还要懂数据库的知识，例如mongodb的读写。
> 项目环境：**Ubuntu 14.04 LTS** + **Python 2.7.6** + **Scrapy 0.24.4** + **MongoDB shell version: 2.4.9**
> IDE： PyCharm 3.4

## 配置项目环境

### 1.安装Python

就系统Ubuntu 14.04来说，自带了python环境，可以在终端输入命令：

    python --version

看有没有显示版本信息，若有，则不需要安装了；若无，则需要安装，请自行google安装。

### 2.安装Scrapy

    (sudo) pip install Scrapy
    
### 3.安装Mongodb

点击此链接：[http://docs.mongodb.org/manual/installation/](http://docs.mongodb.org/manual/installation/)，根据系统类型，点击进去，按照指示安装。

为了Scrapy能够连接Mongodb，需要安装一个中间件的模块`mongokit`， 安装命令如下：

    sudo pip install mongokit
    
或者

    sudo easy_install mongokit
    
## 知识准备

关于这点，其他不说，对于Scrapy小白来说，强烈建议看一下Scrapy官方文档，我推荐中文文档[https://scrapy-chs.readthedocs.org/zh_CN/0.24/topics/item-pipeline.html](https://scrapy-chs.readthedocs.org/zh_CN/0.24/topics/item-pipeline.html)，从开始看到[Link Extractors](https://scrapy-chs.readthedocs.org/zh_CN/0.24/topics/link-extractors.html)章节。看完再去实践，这样过程是比较适合的。
    
## 项目目录结构描述

下面就此项目目录结构来讲一下

    crawler/
    |— crawler/
    |   |- mongodb/           —— 这里存放各个model声明
    |   |   |- __init__.py    —— 连接mongodb初始化
    |   |   |- thjy.py        —— 初始化thjy数据表, 并声明增删查改的方法，例如insert , find , update等
    |   |- spiders/           —— 这里存放各个爬虫文件
    |   |   |- __init__.py
    |   |   |- thjy.py        —— 创建一个爬虫文件为'thjy' , 作用是去爬取指定网页。
    |   |- tools/             —— 放一些工具类文件              
    |   |   |- __init__.py
    |   |   |- exportDocx.py  —— 以此文件为例，exportDocx.py的作用就是从数据库读数据后，再导出docx文件
    |   |- __init__.py
    |   |- items.py           —— 这里声明存储数据的数据结构
    |   |- pipelines.py       —— 收集到数据之后进行管道处理
    |   |- settings.py        —— 全局配置，可以配置功能，插件等
    |- .gitignore
    |- README.md
    |- run_thjySpider.py      —— 启动一个爬虫，跑起来
    |- scrapy.cfg
    
## 启动项目

    python run_thiySpider.py
    
----------
    
## 导出docx知识的补充

### 安装python-docx模块

    pip install python-docx 或者  easy_install python-docx
    
如果这样安装不成功，只能手动安装了，从[https://pypi.python.org/pypi/python-docx](https://pypi.python.org/pypi/python-docx)下载安装包 **python-docx-{version}.tar.gz**

然后解压安装

    tar xvzf python-docx-{version}.tar.gz
    cd python-docx-{version}
    python setup.py install
    
安装完成即可。

文档链接：[https://python-docx.readthedocs.org/en/latest/](https://python-docx.readthedocs.org/en/latest/)

