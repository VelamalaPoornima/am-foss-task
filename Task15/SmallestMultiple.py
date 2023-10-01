import sys
import math
def lcm(n):
    count = 1
    for i in range(1,n+1):
        count = int((count*i)/math.gcd(count,i))
    return count


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(lcm(n))
