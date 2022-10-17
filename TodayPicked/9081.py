# from itertools import permutations

# tc = int(input())
# for _ in range(tc):
#     s = input()
#     arr = sorted(set(permutations(list(s))))
#     arr = ["".join(i) for i in arr]
#     idx = arr.index(s)
#     if idx == len(arr)-1:
#         print(arr[-1])
#     else:
#         print(arr[idx+1])


# tc = int(input())


# def solution(s):
#     flag = False
#     for i in range(len(s)-1, 0, -1):
#         base = s[i]
#         for j in range(i-1, -1, -1):
#             if base > s[j]:
#                 s[i], s[j] = s[j], s[i]
#                 return s[:j+1]+sorted(s[j+1:])
#     return s


# for _ in range(tc):
#     s = list(input())
#     answer = solution(s)
#     print("".join(answer))


tc = int(input())


def solution(s):
    k = -1
    for i in range(len(s)-2, -1, -1):
        # 뒤에서 부터 돌면서, i가 i+1보다 작은 문자를 찾는다.
        if s[i] < s[i+1]:
            k = i
            break

    if k == -1:
        # 그러한 문자가 없다면, 원래 문자가 가장 큰 것.
        return s

    for i in range(len(s)-1, k, -1):
        # 역순으로 돌면서
        # k번째보다 뒤에 있는 문자들 중에서 s[k]보다 큰 값을 찾는다.
        if s[k] < s[i]:
            m = i
            break

    s[k], s[m] = s[m], s[k]  # 스와이프
    return s[:k+1]+list(reversed(s[k+1:]))  # k이후의 문자열을 역순을 취하고 리턴한다.

    # 왜 스와이프 후에 역순을 취하면 될까?
    # k 이후의 문자열은 내림차순으로 정렬되어 있는 상태이다.
    # 그러한 상태에서 뒤에서 부터 돌면서 k보다 큰 수를 찾으면, 그 수가 k 자리에 올 수 있는 가장 작은 수가 되는 것이다.
    # 스와이프 후 k 이후의 문자열을 역순을 취하면 k 다음으로 가장 작은(빠른) 문자열이 된다.
    # 1 3 4 6 5 2
    # 이 경우를 보면 s[k]는 우선 4이다.
    # s[k]보다 뒤에 있는 숫자 중에서 뒤에서 부터 볼때 s[k]보다 큰 것은 5이다.
    # 4와 5를 스와이프하면 1 3 5 6 4 2 가 된다.
    # 5 6 4 2 를 잘 보자.
    # 원래는 뒤의 세 자리가 6 5 2였다. 이게 지금 6 4 2가 되었다. 이 숫자를 뒤집으면 2 4 6이 되고, 이는 6, 4, 2를 가지고 만들 수 있는 수 중에 가장 작은 수일 것이다.
    # 근데 만약에 앞에서 부터 찾았다고 하면 1 3 6 4 5 2가 될 것이고, k의 자리에 올 수 있는 4보다 크고 6보다 작은 5가 존재함에도 불구하고 6이 오게 된다.


for _ in range(tc):
    s = list(input())
    answer = solution(s)
    print("".join(answer))
