def solution(dartResult):
    res = []
    idx = 0
    while idx < len(dartResult):
        if dartResult[idx+1].isalpha():
            num = int(dartResult[idx])
        else:
            num = 10
            idx += 1
        if dartResult[idx+1] == "D":
            num = num**2
        elif dartResult[idx+1] == "T":
            num = num**3

        if idx+2 < len(dartResult) and dartResult[idx+2] in ["*", "#"]:
            if dartResult[idx+2] == "*":
                if res:
                    temp = res.pop()
                    res.append(temp*2)
                res.append(num*2)
            elif dartResult[idx+2] == "#":
                res.append(-num)
            idx += 3
        else:
            res.append(num)
            idx += 2
    answer = 0
    for r in res:
        answer += r
    return answer


print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))
