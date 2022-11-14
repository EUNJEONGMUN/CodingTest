def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    temp = ""
    for s in new_id:
        if s.isalnum() or s in ['-', '_', '.']:
            temp += s
    # 3단계
    while True:
        original = temp
        new = temp.replace("..", ".")

        if len(original) == len(new):
            break
        temp = new

    # 4단계
    if len(temp) > 0 and temp[0] == '.':
        temp = temp[1:]
    if len(temp) > 0 and temp[-1] == '.':
        temp = temp[:-1]

    # 5단계
    if len(temp) == 0:
        temp = 'a'

    # 6단계
    if len(temp) > 15:
        temp = temp[:15]
    if temp[-1] == '.':
        temp = temp[:-1]

    # 7단계
    if len(temp) <= 2:
        while (len(temp) < 3):
            temp += temp[-1]

    return temp


# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
print(solution(""))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
