# n, m, l = map(int, input().split())
# highway = sorted(list(map(int, input().split())))
# if n == 0:
#     left, right = 0, l-1
# else:
#     between = [highway[i]-highway[i-1]
#                for i in range(1, len(highway))]+[highway[0]-0]+[l-highway[-1]]
#     left, right = 0, max(between)


# def set_highway(dist):
#     set_highway_count = 0
#     now_location = 0
#     idx = 0
#     while idx < len(highway):
#         if highway[idx]-now_location <= dist:
#             now_location = highway[idx]
#             idx += 1
#         else:
#             set_highway_count += 1
#             now_location += dist
#     if l-now_location > dist:
#         set_highway_count += (l-1-now_location)//dist
#     return set_highway_count


# answer = l
# while left <= right:
#     mid = (left+right)//2

#     count = set_highway(mid)

#     if count <= m:
#         right = mid - 1
#         # answer = min(mid, answer)
#         answer = mid

#     else:
#         left = mid + 1


# print(answer)

n, m, l = map(int, input().split())
highway = [0]+sorted(list(map(int, input().split())))+[l]
left, right = 1, l  # left를 0으로 설정하면 ZeroDivisionError 발생
# 밑에 mid로 나누는 경우가 있음으로 잘 체크해야 함.


answer = 0
while left <= right:
    mid = (left+right)//2
    count = 0

    for i in range(1, len(highway)):
        if highway[i]-highway[i-1] > mid:
            count += (highway[i]-highway[i-1]-1)//mid

    if count <= m:
        right = mid - 1
        answer = mid

    else:
        left = mid + 1

print(answer)
