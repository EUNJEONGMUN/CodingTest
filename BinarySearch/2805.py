# 나무자르기
import sys
input = sys.stdin.readline

n, target = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
answer = 0
while start <= end:
    mid = (start+end)//2

    # 나무 길이 계산
    remain = 0
    for tree in trees:
        if tree-mid > 0:
            remain += tree-mid

    if target <= remain:  # 나무가 충분하다면, 높이 올리기
        start = mid+1
        answer = mid
    else:  # 나무가 부족하다면, 높이 내리기
        end = mid-1

print(answer)
