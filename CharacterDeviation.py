t = int(input())
for i in range(0,t):
    s = input()
    
    string = "amfoss"
    count = 0
    
    for i in range(0,6):
        if s[i] != string[i]:
            count += 1
            
    print(count)
