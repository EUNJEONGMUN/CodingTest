# def solution(numbers):
#     answer = []
#     for number in numbers:
#         fix = ""
#         while True:
#             index_110 = number.find("110")
#             index_111 = number.find("111")
#             if index_110 == -1 or index_111 == -1:
#                 break
#             if (index_110 < index_111):
#                 fix += number[:index_110+3]
#                 number = number[index_110+3:]
#             else:
#                 fix += number[:index_111]+"110"
#                 number = number[index_111:index_110]+number[index_110+3:]

#         answer.append(fix+number)

#     return answer

def solution(numbers):
    answer = []
    for number in numbers:
        cnt_110 = ""
        stack = []
        idx = 0
        while idx < len(number):
            if len(stack) < 2:
                stack.append(number[idx])
            else:
                if (stack[-1] == "1" and stack[-2] == "1" and number[idx] == "0"):
                    cnt_110 += "110"
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(number[idx])
            idx += 1
        index_0 = -1
        for i in range(len(stack)-1, -1, -1):
            if stack[i] == '0':
                index_0 = i
                break
        if index_0 == -1:
            answer.append(cnt_110+"".join(stack))
        else:
            answer.append("".join(stack[:index_0+1]) +
                          cnt_110+"".join(stack[index_0+1:]))
    return answer


print(solution(["1100111011101001"]))
# ["0101101101101101"]
