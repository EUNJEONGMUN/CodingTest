import sys
input = sys.stdin.readline
n = int(input())
array = [input().strip() for i in range(n)]
arr = sorted([(a, i) for i, a in enumerate(array)])


def get_same_prefix(x, y):
    cnt = 0
    for i in range(min(len(x), len(y))):
        if x[i] == y[i]:
            cnt += 1
        else:
            break
    return cnt


max_pre = [0]*n
max_length = 0
for i in range(n-1):
    pre_length = get_same_prefix(arr[i][0], arr[i+1][0])
    max_pre[arr[i][1]] = max(max_pre[arr[i][1]], pre_length)
    max_pre[arr[i+1][1]] = max(max_pre[arr[i+1][1]], pre_length)
    max_length = max(max_length, pre_length)

save_pre = ""
for i in range(n):
    if max_pre[i] == max_length:
        if save_pre == "":
            save_pre = array[i][:max_length]
            print(array[i])
        elif save_pre == array[i][:max_length]:
            print(array[i])
            break
