n = int(input())
array = list(map(int, input().split()))
array.sort()

left, right, start, end = 0, n-1, 0, n-1

while left < right:
    if abs(array[start]+array[end]) > abs(array[left]+array[right]):
        start, end = left, right

    if abs(array[left+1]+array[right]) > abs(array[left]+array[right-1]):
        right -= 1
    else:
        left += 1

print(array[start], array[end])
