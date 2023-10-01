import sys

def palindrome(num):
    return str(num) == str(num)[::-1]

def largest(n):
    largest = 0
    for i in range(999,99,-1):
        for j in range(i,99,-1):
            product = i*j
            if product<n and palindrome(product) and product>largest:
                largest = product
    return largest 


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = largest(n)
    print(result)
