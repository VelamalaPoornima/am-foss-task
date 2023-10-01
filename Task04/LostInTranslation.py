s = input()
string = "hello"
i = 0
for letter in s:
    if letter == string[i]:
        i += 1
    if i == len(string):
        break
if i == len(string):
    print("YES")
else:
    print("NO")
