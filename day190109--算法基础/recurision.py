def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 递归  o(2^n)

def fib2(n):
    res = [1, 1]
    for i in range(2, n + 1):
        res.append(res[-1] + res[-2])
    return res[-1]


# o(n) , 空间复杂度

def fib3(n):
    if n == 0 or n == 1:
        return 1
    a = 1
    b = 1
    c = 0
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return c


# 空间复杂度1

print(fib(11))
print(fib2(11))
print(fib3(11))
