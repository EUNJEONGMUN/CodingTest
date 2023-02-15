n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

answer = [A[i]*B[i] for i in range(n)]
print(sum(answer))
