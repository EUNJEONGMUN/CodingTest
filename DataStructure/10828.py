import sys
input = sys.stdin.readline

n = int(input())
stack = []


def solution(commend):
    if commend.startswith("push"):
        num = commend.split()[1]
        stack.append(int(num))
    elif commend == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif commend == "size":
        print(len(stack))
    elif commend == "empty":
        print(1 if len(stack) == 0 else 0)
    elif commend == "top":
        print(-1 if len(stack) == 0 else stack[-1])


for _ in range(n):
    commend = input().strip()
    solution(commend)
