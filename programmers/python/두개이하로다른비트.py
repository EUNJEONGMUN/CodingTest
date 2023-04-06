def solution(numbers):
    answer = []

    def change_bit(length):
        if length == 1:
            return "1"
        else:
            return "10"+"1"*(length-2)
    for number in numbers:
        bin_list = ["0"]+list(bin(number)[2:])
        for i in range(len(bin_list)-1, -1, -1):
            if bin_list[i] == "0":
                answer.append(
                    int("".join(bin_list[:i])+change_bit(len(bin_list)-i), 2))
                break
    return answer


print(solution([1, 2, 7]))
print(solution([1001, 337, 0, 1, 333, 673, 343, 221, 898, 997,
      121, 1015, 665, 779, 891, 421, 222, 256, 512, 128, 100]))
