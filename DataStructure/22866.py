# 시간 초과
# n = int(input())
# buildings = [(i, b)
#              for i, b in enumerate(list(map(int, input().split())), start=1)]
# buildings.sort(key=lambda x: x[1], reverse=True)

# answer = [[] for _ in range(n+1)]
# IDX, HEIGHT = 0, 1
# for idx, height in buildings:
#     left_dist, left_height, right_dist, right_height = 0, 0, 0, 0

#     for building in buildings:
#         if building[HEIGHT] <= height:
#             break

#         if building[IDX] < idx:
#             if (left_height == 0 or left_height > height) and (left_dist == 0 or left_dist > idx-building[IDX]):
#                 answer[idx].append(building[IDX])
#                 left_dist = idx-building[IDX]
#                 left_height = building[HEIGHT]
#         else:
#             if (right_height == 0 or right_height > height) and (right_dist == 0 or right_dist > building[IDX]-idx):
#                 answer[idx].append(building[IDX])
#                 right_dist = building[IDX]-idx
#                 right_height = building[HEIGHT]

# answer = [sorted(a, key=lambda x:(abs(i-x), x)) for i, a in enumerate(answer)]

# for a in answer[1:]:
#     if not a:
#         print(0)
#     else:
#         print(len(a), a[0])
