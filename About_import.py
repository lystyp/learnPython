"""
1.
絕對路徑寫法以執行檔路徑為主

python2 絕對找不到則會以import的那個檔案的路徑當作目前路徑再找一次，
如果寫絕對路徑，但以執行檔為絕對路徑找不到的話
就會自動
import a.b.c
看成 from . import a.b.c

但python3
寫成絕對的話，就是要看執行檔路徑為主，沒得商量

關於相對路徑
不能往上爬到跟執行檔同一層，因為相對路徑僅限於用在module內，是這樣嗎?跟執行檔同一層就不算module層啦
會出現ValueError: Attempted relative import in non-package的error
但絕對路徑就沒差
就是說在執行檔跟a同一層的情況下
from a import b	可以
但
from .a import b 會error
或是應該說，有相對路徑的.py檔，不能直接執行，只能用來import
http://kuanghy.github.io/2016/07/21/python-import-relative-and-absolute
寫很讚

-----------------------
from .. import XX.XX 這個寫法感覺就有問題，
都已經from了
import 應該只能放一層吧?

---------
關於python -m xxx.xxx
意思就相當於跑一個 python main.py
然後main.py裡面import xxx.xxx

"""