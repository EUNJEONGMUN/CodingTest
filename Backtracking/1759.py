l, c = map(int, input().split())
alpha = list(input().split())
alpha.sort()
answer = []


def bt(idx, log, a, b):
    if a+b == l:
        if a >= 1 and b >= 2:
            answer.append("".join(log))
        return
    for i in range(idx, len(alpha)):
        log.append(alpha[i])
        if alpha[i] in ["a", "i", "o", "u", "e"]:
            bt(i+1, log, a+1, b)
        else:
            bt(i+1, log, a, b+1)
        log.pop()


bt(0, [], 0, 0)
for a in answer:
    print(a)
