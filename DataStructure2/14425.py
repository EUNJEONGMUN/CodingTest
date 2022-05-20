# n, m = map(int, input().split())
# d = {}

# for _ in range(n):
#     i = input()
#     d[i] = 0
# cnt = 0
# for _ in range(m):
#     i = input()
#     if i in d:
#         cnt += 1
# print(cnt)
n, m = map(int, input().split())
d = set()

for _ in range(n):
    i = input()
    d.add(i)
cnt = 0
for _ in range(m):
    i = input()
    if i in d:
        cnt += 1
print(cnt)
