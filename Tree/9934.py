def solution(arr, index):
    global result
    if len(arr) == 1:
        result[index].append(arr[0])
        return
    result[index].append(arr[len(arr)//2])  # 리스트의 가운데에 있는 것이 root
    solution(arr[:len(arr)//2], index+1)  # 왼쪽
    solution(arr[len(arr)//2+1:], index+1)  # 오른쪽


k = int(input())
tree = list(map(int, input().split()))
result = [[] for _ in range(k)]
solution(tree, 0)


for i in result:
    print(' '.join(map(str, i)))

# 여러 가지 출력 방법
# for i in range(len(result)):
#     print(*result[i])
# for i in result:
#     print(*i)
