def convert_to_sec(time):
    h = int(time[:2])*60*60*1000
    m = int(time[3:5])*60*1000
    s = int(time[6:8])*1000
    f = int(time[-3:])
    return h+m+s+f


def solution(lines):
    start_time = []
    end_time = []
    answer = 0
    for line in lines:
        date, time, sec = line.split()
        end = convert_to_sec(time)
        start = end - (float(sec[:-1])*1000) + 1
        start_time.append(start)
        end_time.append(end)

    for i in range(len(lines)):
        cnt = 0
        cur_end_time = end_time[i]
        # i번째 이전은 작업이 끝났을 것이므로 탐색 하지 않아도 됨.
        for j in range(i, len(lines)):
            if start_time[j] < cur_end_time+1000:  # j의 시작시간이 i의 끝나는 시간으로부터 1초 내에 있다면
                cnt += 1
        answer = max(answer, cnt)
    return answer


# print(solution([
#     "2016-09-15 01:00:04.001 2.0s",
#     "2016-09-15 01:00:07.000 2s"
# ]))
# print(solution(["2016-09-15 01:00:04.002 2.0s",
#                "2016-09-15 01:00:07.000 2s"]))
print(solution([
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]))
