n, k = map(int, input().split())
left = 0
right = n
while left <= right:
    mid = (left+right)//2

    cnt = (mid+1)*(n-mid+1)

    if cnt == k:
        print("YES")
        break
    elif cnt > k:
        left = mid+1
    else:
        right = mid-1
else:
    print("NO")
