numbers = input()

max_val = ""
min_val = ""

# k가 나오면 멈추기. k를 포함해서 최대한 길게 하기
cnt = 0
for i in range(len(numbers)):
    if numbers[i] == "K":
        if cnt:  # cnt가 0이 아닐 때
            max_val += str((10**cnt)*5)
            min_val += str(10**cnt+5)
        else:
            max_val += "5"
            min_val += "5"
        cnt = 0
    else:
        if i == len(numbers)-1:  # 맨 마지막이 M일 때
            max_val += "1"*(cnt+1)
            min_val += str(10**cnt)
        else:
            cnt += 1

print(max_val)
print(min_val)
