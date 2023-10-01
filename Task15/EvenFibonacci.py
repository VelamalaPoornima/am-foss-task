def fib(n):
    a,b = 1,2
    even = 0
    
    while b<=n:
        if b%2==0:
            even = even + b
        a,b = b,a+b
    return even



t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = fib(n)
    print(result)
