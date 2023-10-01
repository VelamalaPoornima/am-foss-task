def calculate_quality(X, Y):
    strX = str(X)
    strY = str(Y)
    maxlen = max(len(strX),len(strY))
    strX = strX.zfill(maxlen)
    strY = strY.zfill(maxlen)
    quality = 0
    for i in range(maxlen):
        quality += abs(int(strX[i]) - int(strY[i]))
    return quality

t = int(input())
for i in range(t):
    L,R = map(int,input().split())
    maxquality = -1
    for X in range(L, R+1):
        for Y in range(L, R+1):
            quality = calculate_quality(X, Y)
            if quality > maxquality:
                maxquality = quality
    print(maxquality)
