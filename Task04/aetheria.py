n = int(input())
time = list(map(int,input().split()))

minimum = min(time)

count = time.count(minimum)

if count == 1:
    index = time.index(minimum) + 1
    print(index)
else:
    print("Still Aetheria")
