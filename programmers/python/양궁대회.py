# from collections import defaultdict
# res = defaultdict(list)
# def dfs(info, arr, cnt, idx):
#     if cnt == 0 or idx == len(arr):
#         if cnt:
#             arr[-1] = cnt
#         # print(arr)
#         lion = 0
#         appeach = 0
#         for i in range(11):
#             if info[i] == 0 and arr[i] == 0:
#                 continue
#             elif info[i] >= arr[i]:
#                 appeach += 10-i
#             else:
#                 lion += 10-i
#         if lion > appeach:
#             res[lion-appeach].append(arr[:])
#         arr[-1] = 0
#         return

#     # 해당 점수를 이기도록
#     if cnt-(info[idx]+1) >= 0:
#         arr[idx] = info[idx]+1
#         dfs(info, arr, cnt-(info[idx]+1), idx+1)
#         arr[idx] = 0

#     # 해당 점수를 지도록
#     dfs(info, arr, cnt, idx+1)


# def solution(n, info):
#     dfs(info, [0]*11, n, 0)
#     if res:
#         res_sort = sorted(res.items(), key=lambda x: (x[0]))[-1][1]
#         res_sort.sort(key=lambda x: (-x[10], -x[9], -x[8], -
#                       x[7], -x[6], -x[5], -x[4], -x[3], -x[2], -x[1], -x[0]))
#         return res_sort[0]
#     else:
#         return [-1]


answer = [-1]
result = 0


def dfs(info, arr, cnt, idx):
    global answer, result
    if cnt == 0 or idx == len(arr):
        if cnt:
            arr[-1] = cnt
        # print(arr)
        lion = 0
        appeach = 0
        for i in range(11):
            if info[i] == 0 and arr[i] == 0:
                continue
            elif info[i] >= arr[i]:
                appeach += 10-i
            else:
                lion += 10-i
        if result <= (lion-appeach):
            result = lion-appeach
            answer = arr[:]
        arr[-1] = 0
        return

    # 해당 점수를 이기도록
    if cnt-(info[idx]+1) >= 0:
        arr[idx] = info[idx]+1
        dfs(info, arr, cnt-(info[idx]+1), idx+1)
        arr[idx] = 0

    # 해당 점수를 지도록
    dfs(info, arr, cnt, idx+1)


def solution(n, info):
    dfs(info, [0]*11, n, 0)
    return answer


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
