string = input()
boom = input()
stack = []
idx = 0
while idx < len(string):
    stack.append(string[idx])
    if len(stack) >= len(boom):
        if "".join(stack[-len(boom):]) == boom:
            for _ in range(len(boom)):
                stack.pop()
    idx += 1

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))
