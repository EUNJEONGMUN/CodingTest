from collections import defaultdict
n = int(input())
table = defaultdict(int)
for idx in range(1, n+1):
    input_string = list(map(int, list(input().split())))
    time, k, tasks = input_string[0], input_string[1], input_string[2:]

    if k == 0:
        table[idx] = time
    else:
        table[idx] = max([table[t] for t in tasks])+time
print(max(table.values()))
