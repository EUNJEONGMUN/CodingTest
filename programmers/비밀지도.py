# def solution(n, arr1, arr2):
#     answer = []

#     for a, b, i in zip(arr1, arr2, range(n)):
#         row1 = bin(a)[2:].zfill(n)
#         row2 = bin(b)[2:].zfill(n)
#         row_str = ""
#         for k in range(n):
#             if int(row1[k])+int(row2[k]) == 0:
#                 row_str += " "
#             else:
#                 row_str += "#"
#         answer.append(row_str)
#     return answer

def solution(n, arr1, arr2):
    answer = []

    for a, b in zip(arr1, arr2,):
        row = bin(a | b)[2:].zfill(n).replace("1", "#").replace("0", " ")
        answer.append(row)
    return answer


print(solution(5, [9, 20, 28, 18, 11], 	[30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
