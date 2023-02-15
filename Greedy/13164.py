import sys
input = sys.stdin.readline

n, k = map(int, input().split())
students = list(map(int, input().split()))
diff = [students[i]-students[i-1] for i in range(1, n)]
diff.sort()
print(sum(diff[:n-k]))
