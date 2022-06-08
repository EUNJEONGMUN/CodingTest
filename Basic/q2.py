def solution(arr, n):
    arr.sort()
    left, right = 0, len(arr)-1

    while left < right:
        if arr[left]+arr[right] == 100:
            return 1
        elif arr[left]+arr[right] < 100:
            left += 1
        else:
            right -= 1
    return 0


print(solution([1, 52, 48], 3))
print(solution([50, 42], 2))
print(solution([4, 13, 67, 87], 4))
