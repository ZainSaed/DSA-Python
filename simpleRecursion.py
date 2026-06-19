## Factorial
def fac(n):
    if n <= 1 :
        return 1
    return n * fac(n-1)
print(fac(5))

## Fibonacci with recursive
def fib(n):
    if n <= 1 :
        return 1
    return fib(n-1) + fib(n-2)
print(fib(5))

## Fibonacci with iterative
def fib(n):
    a,b = 1,1
    for i in range(n):
        a,b = b,a+b
    return a
print(fib(4))

## Fibonacci with recursive(fast)
def fib(n,a=0,b=1):
    if n == 0:
        return a
    return fib(n-1,b,a+b)
print(fib(7))

## Tower of Hanoi
def toh(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    toh(n-1, source, destination, auxiliary)

    print(f"Move disk {n} from {source} to {destination}")

    toh(n-1, auxiliary, source, destination)


toh(3, "A", "B", "C")

## Sum over a List(Iterative)
def sum_list(l):
    sum = 0
    for i in l :
        sum+=i
    return sum
l = [1,2,3]
print(sum_list(l))

## Sum over a List(Recursive)
def sum_list_recursive(l):
    if len(l) == 0:
        return 0
    return l[0] + sum_list_recursive(l[1:])
l = [1,3,4,5]
print(sum_list_recursive(l))


    
