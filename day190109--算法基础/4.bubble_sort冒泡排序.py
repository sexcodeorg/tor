import random
def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]

#优化 某趟没有任何交换,即跳出.已经是有序
def bubble_sort2(li):
    for i in range(len(li)-1):
        exchange=False
        for j in range(len(li)-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
                exchange=True
        if not exchange:
            break

li=list(range(10))
random.shuffle(li)
print(li)
bubble_sort2(li)
print(li)
