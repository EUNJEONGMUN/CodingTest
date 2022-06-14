import sys
input = sys.stdin.readline

s = input().strip()
start, end = 0, 0
res = ""
while end < len(s):
    if s[start] == "<":  # <와 > 사이는 그대로
        while end < len(s) and s[end] != ">":
            end += 1
        res += s[start:end+1]
        start, end = end+1, end+1
    elif s[start].isalnum():  # 알파벳과 숫자 뒤집기
        while end < len(s) and s[end].isalnum():
            end += 1
        temp = list(s[start:end])
        res += "".join(temp[::-1])
        start = end
    else:  # 공백은 pass
        res += s[start]
        start += 1
        end += 1
print(res)
