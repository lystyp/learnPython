# in 跟 not in 可以用在任何類似array的格式
print (1 in [1,2,3]);
print ("s" not in "asd");

# while 可以搭配else使用，當while是因為判斷式而跳出，不是因為break的時候，會進else
i = 0;
while i < 1:
    print("In while!")
    i += 1;
else:
    print("In else!")

j = 0;
while j < 1:
    print("Do break in while!")
    break;
else:
    print("In else!")
