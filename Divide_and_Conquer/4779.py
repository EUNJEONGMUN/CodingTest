def solution(s):
    if len(s) == 1:
        return s

    return solution(s[:len(s)//3]) + " "*(len(s)//3) + solution(s[len(s)//3*2:])


while True:
    try:
        n = int(input())
    except:
        break

    print(solution("-"*(3**n)))
