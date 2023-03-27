from collections import deque


def solution(order):
    order = deque(order)
    num = deque(range(1, len(order)+1))
    stack = []
    answer = 0
    while order:
        if num:
            if order[0] == num[0]:
                answer += 1
                order.popleft()
                num.popleft()
            elif order[0] > num[0]:
                stack.append(num.popleft())
            elif order[0] < num[0]:
                if stack and order[0] == stack[-1]:
                    answer += 1
                    stack.pop()
                    order.popleft()
                else:
                    break

        while stack and order:
            if order[0] == stack[-1]:
                answer += 1
                stack.pop()
                order.popleft()
            else:
                break

    return answer


print(solution([4, 3, 1, 2, 5]))
print(solution([2, 3, 1, 5, 4]))
print(solution([5, 4, 3, 2, 1]))
