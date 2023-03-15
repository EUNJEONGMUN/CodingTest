distance = [[1, 7, 6, 7, 5, 4, 5, 3, 2, 3], [7, 1, 2, 4, 2, 3, 5, 4, 5, 6], [6, 2, 1, 2, 3, 2, 3, 5, 4, 5], [7, 4, 2, 1, 5, 3, 2, 6, 5, 4], [5, 2, 3, 5, 1, 2, 4, 2, 3, 5], [
    4, 3, 2, 3, 2, 1, 2, 3, 2, 3], [5, 5, 3, 2, 4, 2, 1, 5, 3, 2], [3, 4, 5, 6, 2, 3, 5, 1, 2, 4], [2, 5, 4, 5, 3, 2, 3, 2, 1, 2], [3, 6, 5, 4, 5, 3, 2, 4, 2, 1]]


def solution(numbers):
    now_weight = 0
    all_dict = {}
    finger = (4, 6)
    all_dict[finger] = now_weight

    for str_num in numbers:
        num = int(str_num)
        curr_dict = {}
        for finger, weight in all_dict.items():
            left, right = finger
            if right == num or left == num:  # 만약 오른쪽or 왼쪽이 해당 숫자라면,
                if not (left, right) in curr_dict.keys() or curr_dict[(left, right)] > weight + 1:
                    curr_dict[(left, right)] = weight + 1  # weight 1증가
            else:
                # 오른쪽 손 움직이는 경우
                if not (left, num) in curr_dict.keys() or curr_dict[(left, num)] > weight + distance[right][num]:
                    curr_dict[(left, num)] = weight + distance[right][num]
                # 왼쪽 손 움직이는 경우
                if not (num, right) in curr_dict.keys() or curr_dict[(num, right)] > weight + distance[left][num]:
                    curr_dict[(num, right)] = weight + distance[left][num]
        all_dict = curr_dict

    return min(list(all_dict.values()))


print(solution("1756"))
