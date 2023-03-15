from collections import defaultdict


def solution(str1, str2):
    dic = defaultdict(int)
    inter = 0
    union = 0

    for elem in [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]:
        dic[elem] += 1
        union += 1

    for elem in [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]:
        if elem in dic:  # str1에 있으면
            inter += 1  # 교집합 1 증가
            dic[elem] -= 1  # dic 요소 1감소

            if dic[elem] <= 0:  # dic이 0이하라면, delete
                del dic[elem]
        else:  # str1에 없으면
            union += 1  # union 1 증가

    return 65536 if union == 0 else int((inter/union)*65536)


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "	AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))
