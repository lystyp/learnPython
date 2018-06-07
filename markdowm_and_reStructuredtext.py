"""
要在程式中加入註釋，然後讓他自動生成說明文件，有兩種工具
1.markdowm
markdown是一種語法(或叫格式?)，有點像latex，
根據語法寫好內容存成.md檔之後，
接著就可以用 makdocs 這個工具來根據你的程式碼生成說明文件(做成html連排版都做好，還附加搜尋之類的功能)

2.reStructuredText 
reStructuredText 也是另一種語法，比markdown還要嚴格一點，但功能應該也更強大一點，
他用的是 sphinx 來生成說明文件
檔案是存成.rst檔

還有一個重點是，用markdowm要自己寫一個完整的.md檔，
而sphinx則可以直接在code裡面寫註釋，然後他可以去解析code跟註釋，
並生成.rst檔
p.s有人寫個外掛讓markdowm也可以從code生成.md檔，但我還沒試過
https://github.com/raghakot/markdown-apidocs

"""

"""
先來寫寫sphinx的步驟
https://myapollo.com.tw/2016/09/11/python-autodoc/

1.開個新的資料夾並cmd道路徑底下下指令
sphinx-quickstart
然後他會詢問一大堆設定專案相關的東西
其中有一個要不要新增電子書(epub)格式那個我選n
問要裝哪些套件部分
autodoc我選y > autodoc就是用來從程式碼分析轉成.rst的套件
要不要弄個github相關的檔我選n

接著照網站上繼續跑

注意
index.rst裡面的
.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   hello
這裡hello前面是3個空格的長度喔!!!
有時候用tab會是4個空格，跑會error

2.套用不同樣板
先安裝樣板
pip install sphinx_rtd_theme
接著去conf.py裡面
找到設定 html_theme 的地方把它改成下面這樣
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


"""