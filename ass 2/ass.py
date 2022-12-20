import pandas as panda
li=[]
for x in range(5):
    num=int(input())
    li.append(num**2)
pow=panda.Series(li)
print(pow)