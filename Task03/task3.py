def isprime(i):
    for j in range(2,i):
        if(i%j==0):
            return False
    return True
n=int(input())
for i in range(2,n+1):
    if(isprime(i)):
        print(i)