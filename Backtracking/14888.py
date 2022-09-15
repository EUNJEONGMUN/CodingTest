# 14888

from itertools import permutations

from sys import stdin
input = stdin.readline

N = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

op_list = []
op_list.extend(['+']*add)
op_list.extend(['-']*sub)
op_list.extend(['*']*mul)
op_list.extend(['/']*div)

order = set(permutations(op_list, len(op_list)))

result = []

for elem in order:
    temp = num[0]
    for i in range(N-1):
        temp_str = str(temp) + elem[i] + str(num[i+1])
        temp = int(eval(temp_str))
    result.append(temp)

print(max(result))
print(min(result))
