import time

def fib1(n):
    if n <= 1:
        return 1
    else:
        return fib1(n-2) + fib1(n-1)

def fib2(m):
    x = 1
    y = 1
    for i in range(m):
        x, y = y, x + y
    return x

# Measure fib1
start = time.perf_counter()
print(fib1(20))
end = time.perf_counter()
time_fib1 = (end - start) * 1000
print("Time of fib1 (ms):", time_fib1)

# Measure fib2
start = time.perf_counter()
print(fib2(20))
end = time.perf_counter()
time_fib2 = (end - start) * 1000
print("Time of fib2 (ms):", time_fib2)