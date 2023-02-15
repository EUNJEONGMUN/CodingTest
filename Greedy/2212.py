import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
sensors.sort()
diff = [sensors[i]-sensors[i-1] for i in range(1, n)]
diff.sort()
print(sum(diff[:n-k]))
