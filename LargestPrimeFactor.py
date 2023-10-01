import sys

def isprime(i):
    for j in range(2,i):
        if (i%j==0):
            return False
    return True


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    largest = 0
    for i in range(2,n+1):
        if (n%i==0):
            if(isprime(i)):
                largest = i
    print(largest)
