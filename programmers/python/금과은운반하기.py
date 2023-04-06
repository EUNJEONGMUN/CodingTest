import math


def solution(a, b, g, s, w, t):
    # 최악의 경우 찾기
    # 최악의 경우는 각 지역에서 gold+silver를 모두 움직였을 때의 시간 중 가장 큰 값
    max_value = 0
    for i in range(len(t)):
        gs = g[i]+s[i]
        if gs <= w[i]:  # gold+silver의 값이 w[i] 보다 작다면 한 번에 옮길 수 있음
            max_value = max(max_value, t[i])
        else:
            max_value = max(max_value, (math.ceil(gs/w[i])*t[i])*2-t[i])

    start, end = 0, max_value
    answer = max_value
    while start <= end:
        mid = (start+end) // 2
        move_gold, move_silver, total = 0, 0, 0
        for i in range(len(t)):
            move_count = math.ceil((mid//t[i])/2)
            move_gold += min(g[i], move_count*w[i])  # gold 옮길 수 있는 최대
            move_silver += min(s[i], move_count*w[i])  # silver 옮길 수 있는 최대
            total += min(g[i]+s[i], move_count*w[i])  # gold+silver 옮길 수 있는 최대
        if (a <= move_gold and b <= move_silver and a+b <= total):
            end = mid-1
            answer = min(mid, answer)
        else:
            start = mid+1
    return answer


print(solution(10, 10, [100], [100], [7], [10]))
print(solution(90, 500, [70, 70, 0], [
      0, 0, 500], [100, 100, 2], [4, 8, 1]))
