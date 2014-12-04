crawler
=======

Website Crawler

## Run ThjySpider

    python run_thiySpider.py
    
This is a demo which shows how to crawl web page to get the content you want. let me explain what exactly every file is.

    crawler/
    |— crawler/
    |   |- mongodb/
    |   |   |- __init__.py
    |   |   |- thjy.py        —— The model of thjy, which can operate mongodb , such as insert , find , update , etc
    |   |- spiders/
    |   |   |- __init__.py
    |   |   |- thjy.py        —— Necessary：A spider named 'thjy' , which crawl page and get the specify data from the page
    |   |- tools/
    |   |   |- __init__.py
    |   |   |- exportDocx.py  —— A tool called exportDocx , which can export data that read from mongodb into words file
    |   |- __init__.py
    |   |- items.py           —— Where can define your data schema
    |   |- pipelines.py       —— where define the class to process the "item" data
    |   |- settings.py        —— Global setting , functional setting , plugin setting
    |- .gitignore
    |- README.md
    |- run_thjySpider.py      —— To run specified spider , like 'thjy'
    |- scrapy.cfg
    
### Preparation for exporting into doc file

Install **python-docx** module

    pip install python-docx OR  easy_install python-docx
    
Of course , you have to install **pip** or **easy_install** before you start installing **python-docx**

If it doesn't work above , it can be installed manually , download **python-docx-{version}.tar.gz** from [https://pypi.python.org/pypi/python-docx](https://pypi.python.org/pypi/python-docx)

And then :

    tar xvzf python-docx-{version}.tar.gz
    cd python-docx-{version}
    python setup.py install
    
you can enjoy **python-docx** now.

#### Some examples for practice ? 

- **exportDocx.py**
- [https://python-docx.readthedocs.org/en/latest/](https://python-docx.readthedocs.org/en/latest/)

