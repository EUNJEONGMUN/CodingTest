n = int(input())
nums = [int(input()) for _ in range(n)]  # input
point = 0  # 현재 nums를 나타내는 point
stack = []
operation = []  # 결과를 담는 리스트
i = 0  # 1부터~n까지
while point < len(nums) and i <= n:  # 아직 정렬해야할 수열이 남았고, i가 n을 넘어가지 않았을 때
    if stack and stack[-1] == nums[point]:
        stack.pop()  # pop
        operation.append("-")
        point += 1  # nums point 증가

    else:
        i += 1
        stack.append(i)  # stack에 append
        operation.append("+")


if point == len(nums):  # 마지막까지 수열을 정렬했다면 정답
    for op in operation:
        print(op)
else:
    print("NO")
