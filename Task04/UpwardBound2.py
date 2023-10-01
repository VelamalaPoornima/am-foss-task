def minOperation(arr):
    n = len(arr)
    flag = False
    count = 0
    for i in range(n-2,-1,-1):
        if arr[i + 1] == 0:
            flag = True
            break
        while arr[i] >= arr[i+1]:
            count += 1
            arr[i] = arr[i]//2
    if flag:
        return -1
    return count
    
t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(minOperation(arr))
