import sys
input = sys.stdin.readline

array = list(input())
result = 0
stack = []

for idx in range(len(array)):
    if array[idx] == ")":  # ")" 이라면 stack에서 pop
        temp = stack.pop()
        if array[idx-1] == "(":  # 바로 전이 "("라면 레이저로 절단해야 하므로 stack에 있는 막대기 들을 1씩 증가
            for i in range(len(stack)):
                stack[i] += 1
        else:  # 막대기의 끝
            result += temp  # 결과에 잘린 개수 추가
    else:  # "("이라면 stack에 추가
        stack.append(1)

print(result)
