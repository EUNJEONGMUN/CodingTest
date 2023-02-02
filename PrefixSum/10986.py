# 메모리초과
# from itertools import combinations

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))

# sum_arr = [0]*(n+1)
# for i in range(1, n+1):
#     sum_arr[i] = sum_arr[i-1]+arr[i-1]

# orders = list(combinations(range(0, n), 2))

# cnt = 0

# for i in arr:
#     if i % m == 0:
#         cnt += 1

# for x, y in orders:
#     if (sum_arr[y+1]-sum_arr[x]) % m == 0:
#         cnt += 1

# print(cnt)


# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))

# sum_arr = [0]*(n+1)
# for i in range(1, n+1):
#     sum_arr[i] = sum_arr[i-1]+arr[i-1]
# sum_set = set(sum_arr)

# count = 0
# for i in sum_arr[1:]:
#     for j in range(m, i+1, m):
#         if (i-j) in sum_set:
#             count += 1
# print(count)


# 시간초과
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))

# sum_arr = [0]*(n+1)
# for i in range(1, n+1):
#     sum_arr[i] = sum_arr[i-1]+arr[i-1]
# sum_set = set(sum_arr)

# count = 0
# for i in sum_arr[1:]:
#     for j in range(m, i+1, m):
#         if (i-j) in sum_set:
#             count += 1
# print(count)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0]+list(map(int, input().split()))

mod = [0]*m

for i in range(1, n+1):
    arr[i] += arr[i-1]
    mod[arr[i] % m] += 1

count = mod[0]  # 전체 -> [1, 2], [1, 2, 3], [1, 2, 3, 1, 2]

# 부분집합 구하기
# 한 부분(A)이 m으로 나눴을 때 나머지가 1이고
# 다른 부분(B)도 m으로 나눴을 때 나머지가 1이라면
# A에서 B를 빼면 나머지가 0인 구간이 생길 것이다.
# 이는 m으로 나눴을 때 나머지가 x인 부분들 중에 2개씩 뽑는 것과 같다.
# 조합 계산식으로 풀 수 있다.

# i == 0이면 [6] ([1, 3, 6] 에서 [1, 3] 뺀거), [3, 1, 2]([1, 2, 3, 1, 2] 에서 [1, 2] 뺀거), [1, 2]
# i == 1이면 [2, 3, 1]([1, 2, 3, 1] 에서 [1]뺀거)

for i in mod:
    count += i*(i-1)//2
print(count)
