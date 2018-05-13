# python 的 coding style
# https://www.ptt.cc/bbs/Translate-CS/M.1368435529.A.D7F.html

# ----------------------------------------------------------
# in 跟 not in 可以用在任何類似array的格式
print (1 in [1,2,3])
print ("s" not in "asd")

# ----------------------------------------------------------
# while 可以搭配else使用，當while是因為判斷式而跳出，不是因為break的時候，會進else
i = 0
while i < 1:
    print("In while!")
    i += 1
else:
    print("In else!")

j = 0
while j < 1:
    print("Do break in while!")
    break
else:
    print("In else!")

# ----------------------------------------------------------
# raw_input 跟 input的差別
# python2是input(XXX)，python3 改成eval(input(XXX))
print(eval(input("show result : Key 1+1 in input   "))) # show 2
# python2是raw_input(XXX)，python3 改成input(XXX)
print(input("show result : Key 1+1 in raw_input   ")) # show 1+1，就是單純截字串

# ----------------------------------------------------------
# print 裡面有很多參數可以用
print("asd",end = "")

# ----------------------------------------------------------
# enumerate 跟for功能很像，但會多回傳index
choices = [(1,2), (3,4), (5,6)]
for index, item in enumerate(choices):
  print( index , item )

# ----------------------------------------------------------
3 ** 2 # 3的2次方
8 / 5 # = 1.6
8 // 5 # = 1 (就是商)

# ----------------------------------------------------------
# 兩個int相除
5 / 2 # = 2.5 in Python3
5 / 2 # = 2 in Python2

# ----------------------------------------------------------
# 把dictionary 轉成 list 包 tuple
d = {
  "Name": "Guido",
  "Age": 56,
  "BDFL": True
}
print (d.items())
# => [('BDFL', True), ('Age', 56), ('Name', 'Guido')]
# dict[XXX] XXX放的只能是key不能是index，因為dictionary沒有順序的概念

# ----------------------------------------------------------
# 這什麼奇怪的用法？
# named " list comprehension "
# http://codingpy.com/article/python-list-comprehensions-explained-visually/
# 主要的用法是用來把list轉換成另一個list，用for遍歷原本的list根據條件是產生新的list
evens_to_10 = [i for i in range(11) if i % 2 == 0] # [2,4,6,8,10]

# ----------------------------------------------------------
l = [1,2,3,4,5,6,7,8,9]
# l[x:y:z]
# 從x開始往y方向根據步階z一個一個取出來丟到新的list，一直取到y的前一個，如果y-x跟z的正負號不同，會直接回傳空list
# z < 0 : x預設最後一個，y預設第一個
# z > 0 : 反之亦然

# ----------------------------------------------------------
# Python特殊语法：filter、map、reduce、lambda 
# https://www.cnblogs.com/longdouhzt/archive/2012/05/19/2508844.html

# ----------------------------------------------------------
# dictionary to list[(tuple), (tuple), ...]
dic = {......}
dicToList = dic.items();

# ----------------------------------------------------------
# 位元操作
print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT
bin(x) # 用string回傳x的２進位表示式
oct(x) # 用string回傳x的８進位表示式
hex(x) # 用string回傳x的16進位表示式

# ----------------------------------------------------------
int("10") # 回傳十進位整數10
int("10", 2) # 回傳十進位整數2，後面參數2表示第一個參數是用什麼進位來表示的
# int("10", X) # 回傳X進位的10轉成10進位後的值