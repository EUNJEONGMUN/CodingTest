import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())

cuts = [int(input()) for _ in range(m)]


def cutting(space):
    point = 0
    count = 0

    flag = False
    for cut in cuts:
        if cut-point >= space:
            count += 1
            point = cut
            flag = True

    # 마지막 계산
    if (flag and l-point < space):
        count -= 1

    return count


for _ in range(n):
    count = int(input())

    start = 0
    end = l
    answer = 0

    while start <= end:
        space = (start+end)//2

        cut_count = cutting(space)
        if cut_count >= count:
            answer = space
            start = space+1
        else:
            end = space-1
    print(answer)
