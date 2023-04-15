def solution(depth, idx):
    if depth == 6:
        print(*log)
        return
    for i in range(idx, len(numbers)):
        log[depth] = numbers[i]
        solution(depth+1, i+1)


while True:
    numbers = list(map(int, input().split()))[1:]
    if len(numbers) == 0:
        break
    log = [0]*6
    solution(0, 0)
    print()
