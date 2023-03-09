numbers = [0b1101111, 0b0001001, 0b1011110, 0b1011011, 0b0111001,
           0b1110011, 0b1110111, 0b1001001, 0b1111111, 0b1111011]

N, K, P, X = map(int, input().split())


def get_diff_count(a, b):
    result = bin(numbers[a] ^ numbers[b])
    return result.count("1")


print(get_diff_count(0, 3))


def solution(num, remain_p, depth):
    if int(num) > N:
        return

    for i in range(0, 10):
        diff_count = get_diff_count(i, X[depth])
        if remain_p - diff_count >= 0:
            solution(, remain_p, depth)
