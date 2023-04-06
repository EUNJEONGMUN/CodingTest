def is_correct(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True


def find_balance(s):
    if s == "":
        return -1
    left, right = 0, 0

    for i in range(len(s)):
        if s[i] == "(":
            left += 1
        else:
            right += 1

        if left == right:
            return i


def recursion(p):
    if is_correct(p):
        return p

    idx = find_balance(p)
    u = p[:idx+1]
    v = p[idx+1:]

    if is_correct(u):
        return u+recursion(v)
    else:
        reverse = ""
        for r in u[1:-1]:
            if r == ")":
                reverse += "("
            else:
                reverse += ")"

        return "("+recursion(v)+")"+reverse


def solution(p):
    return recursion(p)


# print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
