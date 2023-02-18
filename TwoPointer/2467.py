import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

left, right = 0, n-1
min_value = sys.maxsize
min_answer = [0, 0]

while left < right:
    if abs(numbers[left]+numbers[right]) < min_value:
        min_answer = [numbers[left], numbers[right]]
        min_value = abs(numbers[left]+numbers[right])

    if numbers[left]+numbers[right] > 0:
        right -= 1
    else:
        left += 1
print(*min_answer)
