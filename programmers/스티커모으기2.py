def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    # 첫 번째 반드시 포함
    dp1 = [0]*(len(sticker))
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    for i in range(2, len(sticker)):
        dp1[i] = max(sticker[i]+dp1[i-2], dp1[i-1])

    # 첫 번째 반드시 미포함
    dp2 = [0]*len(sticker)
    dp2[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp2[i] = max(sticker[i]+dp2[i-2], dp2[i-1])

    return max(dp1[-2], dp2[-1])


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))
