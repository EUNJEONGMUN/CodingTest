n = int(input())

count = -1
answer = -1


def solution(radix, number):
    global answer, count

    if len(number) == radix:
        count += 1
        if n == count:
            answer = int(number)
        return

    for i in range(10):
        if len(number) == 0 or int(number[-1]) > i:
            solution(radix, number+str(i))
            if answer != -1:
                break
        else:
            break


radix = 1
while count <= n:
    before = count
    solution(radix, "")
    radix += 1

    if answer != -1:  # 정답이 update 되면 출력 후 break
        print(answer)
        break

    if count == before:  # solution 메서드를 하기 전과 후의 count 수가 같다면 더이상 감소하는 수가 없다는 뜻
        print(answer)
        break
