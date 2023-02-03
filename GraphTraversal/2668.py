n = int(input())
numbers = [0]+[int(input()) for _ in range(n)]
answer = set()

for i in range(1, n+1):
    if i not in answer:
        temp = set()
        idx = i
        while True:
            if numbers[idx] == i:
                temp.add(numbers[idx])
                answer.update(temp)
                break
            if numbers[idx] in temp:
                break
            else:
                temp.add(numbers[idx])
                idx = numbers[idx]
print(len(answer))
answer = sorted(list(answer))
for a in answer:
    print(a)
