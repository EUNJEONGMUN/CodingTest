tc = int(input())

operations = [" ", "+", "-"]


def calculate(nums):
    total = 0
    save = ""
    op = "+"
    for n in nums:
        if n == " ":
            continue
        elif n.isdigit():

            save += n
        else:
            if op == "+":
                total += int(save)
            elif op == "-":
                total -= int(save)
            save = ""
            op = n
    if op == "+":
        total += int(save)
    elif op == "-":
        total -= int(save)

    return total


def backtracking(n, remain, now):
    if len(now) == n*2-1:
        if calculate(now) == 0:
            print("".join(now))
            return
    for i, r in enumerate(remain):
        for op in operations:
            now.append(op)
            now.append(r)
            backtracking(n, remain[i+1:], now)
            now.pop()
            now.pop()


def solution(n):
    numbers = list(map(str, range(1, n+1)))
    backtracking(n, numbers[1:], [numbers[0]])


for _ in range(tc):
    m = int(input())
    solution(m)
    print()
