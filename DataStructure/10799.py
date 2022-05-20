# array = list(input())
# result = 0
# stack = [1]

# for idx in range(1, len(array)):
#     if array[idx] == ")":
#         temp = stack.pop()
#         if array[idx-1] == "(":
#             for i in range(len(stack)):
#                 stack[i] += 1
#         else:
#             result += temp
#     else:
#         stack.append(1)

array = list(input())
result = 0
stack = 1

for idx in range(1, len(array)):
    if array[idx] == ")":
        if array[idx-1] == "(":
            stack -= 1
            result += stack

    else:
        stack += 1

print(result)
