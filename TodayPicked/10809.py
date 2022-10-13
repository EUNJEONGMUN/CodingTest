dic = [-1]*26
s = input()

for i in range(len(s)):
    if dic[ord(s[i])-97] == -1:
        dic[ord(s[i])-97] = i


print(*dic)
