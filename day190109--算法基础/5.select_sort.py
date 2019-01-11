import random

# 无序区位置,最小数位置

#找最小数
def select_sort(li):
    li_val = li[0]
    for i in range(1, len(li)):
        if li_val > li[i]:
            li_val = li[i]
    return li_val

#选择排序
def select_sort2(li):
    # 无序区位置 i,n-i
    for i in range(len(li) - 1):
        min_pos = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_pos]:
                min_pos = j
        li[i], li[min_pos] = li[min_pos], li[i]
        print(li)

li = list(range(10))
random.shuffle(li)
print(select_sort2(li))
