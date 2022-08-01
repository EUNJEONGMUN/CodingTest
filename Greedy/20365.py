n = int(input())
s = input()

blue = 0
red = 0
cnt = 0
if s[0] == "B":
    blue += 1
else:
    red += 1
for i in range(1, n):  # 구역의 갯수 세기
    if s[i-1] != s[i]:  # 앞과 뒤가 다를 때
        if s[i] == "B":  # B면 blue 추가
            blue += 1
        else:  # R이면 red 추가
            red += 1
print(min(blue, red)+1)
