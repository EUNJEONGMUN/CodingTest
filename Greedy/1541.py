# 1541

s = input().split("-")  # '-' 로 나누기
res = 0
for i in range(len(s)):
    temp = sum(map(int, s[i].split("+")))  # '+'로 연결된 부분 계산하기
    if i == 0:  # 첫 번째에 있는 요소일 때 더해주기
        res += temp
    else:  # 나머지는 다 빼주기
        res -= temp
print(res)
