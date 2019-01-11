import random

def insert_sort(li):
    for i in range(1,len(li)):
        j=i-1
        tmp=li[i]
        while j>=0 and li[j]>tmp:
            li[j+1]=li[j]
            j-=1
        li[j+1]=tmp
        print(li)

li=list(range(10))
random.shuffle(li)
insert_sort(li)


2413
1243