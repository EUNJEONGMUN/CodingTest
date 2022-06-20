n = int(input())
switch = [0]+list(map(int, input().split()))
k = int(input())


def woman(num):
    switch[num] = not switch[num]
    left, right = num, num
    # 중간에서 시작해서 양쪽으로 확인
    while True:
        left -= 1
        right += 1

        # 양쪽이 같으면 바꾸기
        if left > 0 and right <= n and switch[left] == switch[right]:
            switch[left] = not switch[left]
            switch[right] = not switch[right]
        else:
            break


def man(num):
    for i in range(num, n+1, num):
        switch[i] = not switch[i]


for _ in range(k):
    user, num = map(int, input().split())
    if user == 1:
        man(num)
    else:
        woman(num)

switch = switch[1:]
k = 0
while True:
    # 20개씩 출력
    # boolean을 int로 바꾸어 출력
    if k+20 > n:
        print(*list(map(int, switch))[k:])
        break
    else:
        print(*list(map(int, switch))[k:k+20])
        k += 20
