import sys
input = sys.stdin.readline
s = input().strip()
t = input().strip()


def solution(t):
    if t == s:
        print(1)
        exit()

    if len(t) > 0 and t[0] == "B":  # B를 제거할 수 있다면
        temp = t[1:]
        solution(temp[::-1])

    if len(t) > 0 and t[-1] == "A":  # A를 제거할 수 있다면
        solution(t[:-1])


if not solution(t):
    print(0)
else:
    print(1)
