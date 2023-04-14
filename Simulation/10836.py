import sys
input = sys.stdin.readline

N, D = map(int, input().split())
growth = [1]*(2*N-1)
for _ in range(D):
    zero, one, two = map(int, input().split())
    for i in range(zero, zero+one):
        growth[i] += 1
    for i in range(zero+one, 2*N-1):
        growth[i] += 2

for i in range(N-1, -1, -1):
    print(growth[i], *growth[N:])
