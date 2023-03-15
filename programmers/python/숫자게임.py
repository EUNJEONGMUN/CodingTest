def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    point = 0
    idxB = 0
    for idxA in range(len(A)):
        if A[idxA] < B[idxB]:  # B가 A보다 더 클 때만
            idxB += 1  # B의 인덱스를 오른쪽으로 옮김. 그래야 그나마 큰 값하고 A의 값하고 비교하여 이길 수 있음
            point += 1
    return point


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
