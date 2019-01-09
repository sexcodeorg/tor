#二分法
def bin_search(li, val):
    low = 0
    high = len(li) - 1
    while low < +high:  # 候选区还有值
        mid = (low + high) // 2
        if li[mid] == val:
            return mid  # 返回下标
        elif li[mid] > val:
            high = mid - 1
        else:  # li[mid]<val
            low = mid + 1
    return -1

li=list(range(0,1000,2))
print(bin_search(li,600))