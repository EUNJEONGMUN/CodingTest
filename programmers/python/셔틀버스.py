from bisect import bisect_left, bisect_right


def convert_to_minute(time):
    h, m = time.split(":")
    return int(h)*60+int(m)


def convert_to_time(m):
    return str(m//60).zfill(2)+":"+str(m % 60).zfill(2)


def solution(n, t, m, timetable):
    END_TIME = convert_to_minute("23:59")
    # n번, t분 간격, m명까지
    for idx in range(len(timetable)):  # 시간 -> 분으로 바꾸기
        timetable[idx] = convert_to_minute(timetable[idx])
    timetable.sort()
    answer = 0
    for i in range(n):
        time = 9*60 + (i*t)
        cnt = bisect_right(timetable, time)  # 셔틀버스가 온 시간까지 도착한 사람 수

        if i == n-1 or time >= END_TIME:  # 마지막 경우의 수
            if cnt < m:  # 인원을 다 태울 수 있을 때
                answer = time  # 마지막에 오면 됨
            else:  # 다 태울 수 없다면

                answer = timetable[m-1]-1
        else:
            if cnt < m:
                timetable = timetable[cnt:]
            else:
                timetable = timetable[m:]

    return convert_to_time(answer)


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
      "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))

print(solution(10, 25, 1, ["09:00", "09:10", "09:20", "09:30", "09:40",
      "09:50", "10:00", "10:10", "10:20", "10:30", "10:40", "10:50"]))  # 10:29
