n = int(input())
arr = list(map(int, input().split()))

left, right = 0, n-1
res = 0

while left < right:
    val = (right-left-1)*min(arr[left], arr[right])
    if res < val:
        res = val
    if arr[right] < arr[left]:  # 더 작은 값을 줄여주기.
        right -= 1
    else:
        left += 1

print(res)

# n = int(input())
# arr = list(map(int, input().split()))
# new_arr = [(idx, val) for idx, val in enumerate(arr)]
# new_arr.sort(key=lambda x: x[1])
# res = 0
# for i in range(n-1):
#     for j in range(i+1, n):
#         val = new_arr[i][1] * (abs(new_arr[i][0]-new_arr[j][0])-1)
#         if res < val:
#             res = val
# print(res)
