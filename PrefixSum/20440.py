import sys
input = sys.stdin.readline

start = []  # 시작 시간 리스트
end = []  # 끝 시간 리스트
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    start.append(a)
    end.append(b)
start.sort()
end.sort()


max_cnt = 0
cnt = 0
res = [-1, -1]
start_pt = 0
end_pt = 0
is_new = False

while True:
    if start_pt < n and end_pt < n:  # 시작 포인트와 끝 포인트가 범위를 넘지 않았을 때
        if start[start_pt] < end[end_pt]:  # 시작포인트가 더 빠르다면
            cnt += 1  # 모기 개수 추가

            if max_cnt < cnt:  # 모기의 개수가 더 많을 경우 갱신
                res[0] = start[start_pt]
                max_cnt = cnt
                is_new = True
            start_pt += 1

        elif start[start_pt] == end[end_pt]:  # 시작포인트와 끝 포인트가 같다면
            start_pt += 1
            end_pt += 1
        else:  # 끝 포인트가 더 빠르다면
            # max 카운트와 같다면 res의 end pont 갱신, 다만 가장 빠른 경우를 출력해야 하므로, 같은 max count를 구분해주기 위해 is_new를 활용했다.
            if max_cnt == cnt and is_new:
                res[1] = end[end_pt]
                is_new = False
            cnt -= 1  # 감소
            end_pt += 1
    elif start_pt >= n and end_pt < n:
        if max_cnt == cnt and is_new:
            res[1] = end[end_pt]
        break
    else:
        break
print(max_cnt)
print(*res)
