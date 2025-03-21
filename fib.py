def fib(n):
    it += 1
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(6))
# fib(5) + fib(4)
# fib(5) + fib(3) + fib(2)
# fib(5) + fib(3) + fib(1) + fib(0)
# fib(5) + fib(3) + 1 + 0
# fib(5) + fib(2) + fib(1) + 1
# fib(5) + fib(1) + fib(0) + fib(1) + 1
# fib(5) + 1 + 0 + 1 + 1
# fib(4) + fib(3) + 1 + 1 + 1
# fib(4) + fib(2) + fib(1) + 1 + 1 + 1
# fib(4) + fib(1) + fib(0) + 1 + 1 + 1 + 1
# fib(3) + fib(2) + 1 + 0  + 1 + 1 + 1 + 1
# fib(3) + fib(1) + fib(0) + 1 + 0  + 1 + 1 + 1 + 1
# fib(2) + fib(1) + 1 + 0 + 1 + 0  + 1 + 1 + 1 + 1
# fib(1) + fib(0) + 1 + 1 + 0 + 1 + 0  + 1 + 1 + 1 + 1
# 1 + 0  + 1 + 1 + 0 + 1 + 0  + 1 + 1 + 1 + 1