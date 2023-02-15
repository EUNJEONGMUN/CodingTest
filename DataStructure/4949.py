def solution(string):
    stack = []

    for s in string:
        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif s == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
    return False if stack else True


while True:
    s = input()
    if s == ".":
        break
    answer = solution(s)
    print("yes" if answer else "no")
