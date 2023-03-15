def solution(surveies, choices):
    kakao = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0, }
    for survey, choice in zip(surveies, choices):
        if choice == 1:
            kakao[survey[0]] += 3
        elif choice == 2:
            kakao[survey[0]] += 2
        elif choice == 3:
            kakao[survey[0]] += 1
        elif choice == 5:
            kakao[survey[1]] += 1
        elif choice == 6:
            kakao[survey[1]] += 2
        elif choice == 7:
            kakao[survey[1]] += 3
    answer = ''

    for a, b in ["RT", "CF", "JM", "AN"]:
        if kakao[a] >= kakao[b]:
            answer += a
        else:
            answer += b
    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], 	[7, 1, 3]))
