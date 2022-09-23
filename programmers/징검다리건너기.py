def solution(stones, k):
    start = 1
    end = max(stones)
    answer = 0
    while start <= end:
        mid = (start+end)//2  # 인원 수

        cnt = 0
        flag = True

        # 없어진 돌의 개수 세기
        for i in stones:
            if i-mid < 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                flag = False
                break

        if flag:
            start = mid+1
            answer = mid  # 정답 저장
        else:
            end = mid-1
    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
