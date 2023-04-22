def solution(word):
    alphabet = ['A', 'E', 'I', 'O', 'U']
    global answer
    answer = 0

    def bt(string):
        global answer
        answer += 1

        if word == string:
            return True
        if len(string) == 5:
            return False

        for i in range(5):
            if bt(string+alphabet[i]):
                return True
    for i in range(5):
        if bt(alphabet[i]):
            return answer


def solution2(word):
    alphabet = ['A', 'E', 'I', 'O', 'U']
    global answer
    answer = 0
    log = []

    def bt():
        global answer
        answer += 1

        if "".join(log) == word:
            return True
        if len(log) == 5:
            return False

        for i in range(5):
            log.append(alphabet[i])
            ret = bt()
            log.pop()
            if ret:
                return True
    bt()
    return answer-1


print(solution2("AAAAE"))
print(solution2("AAAE"))
print(solution2("I"))
print(solution2("EIO"))
