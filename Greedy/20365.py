n = int(input())
s = input()

blue = 0
red = 0
cnt = 0
if s[0] == "B":
    blue += 1
else:
    red += 1
for i in range(1, n):
    if s[i-1] != s[i]:
        if s[i] == "B":
            blue += 1
        else:
            red += 1
print(min(blue, red)+1)
