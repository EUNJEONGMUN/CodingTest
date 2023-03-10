import sys
input = sys.stdin.readline

n = int(input())
strings = dict()
for i in range(n):
    string = input().strip()
    if string not in strings:
        strings[string] = i

sorted_strings = sorted(list(strings.items()), key=lambda x: (x[1], x[0]))
max_value = -1
S = sorted_strings[0]
T = sorted_strings[1]

for i in range(n-1):
    cnt = 0
    s, t = sorted_strings[i][0], sorted_strings[i+1][0]
    for j in range(min(len(s), len(t))):
        if s[j] != t[j]:
            break
        cnt += 1

    if cnt > max_value:
        S, T = sorted_strings[i], sorted_strings[i+1]
        max_value = cnt
    elif cnt == max_value:
        if min(S[1], T[1]) > min(sorted_strings[i][1], sorted_strings[i+1][1]) and max(S[1], T[1]) > max(sorted_strings[i][1], sorted_strings[i+1][1]):
            S, T = sorted_strings[i], sorted_strings[i+1]


if S[1] < T[1]:
    print(S[0])
    print(T[0])
else:
    print(T[0])
    print(S[0])
