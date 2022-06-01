n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

# 가장 양이 적은 에너지 드링크를 가장 양이 많은 에너지 드링크에 붓는다.
while len(arr) > 1:
    drink = arr.pop()
    arr[0] += (drink/2)

print(arr[0])
