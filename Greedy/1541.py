s = input().split("-")
res = 0
for i in range(len(s)):
    temp = sum(map(int, s[i].split("+")))
    if i == 0:
        res += temp
    else:
        res -= temp
print(res)
