def chenge_to_second(string):  # 시간 초로 변환하기
    h, m, s = string.split(":")
    return (int(h)*60*60)+(int(m)*60)+int(s)


def change_to_str(second):  # 초 -> 시간 문자열로 변환하기
    res = ""
    h = second//3600
    second %= 3600
    m = second // 60
    s = second % 60

    if h < 10:
        res += "0"+str(h)+":"
    else:
        res += str(h)+":"

    if m < 10:
        res += "0"+str(m)+":"
    else:
        res += str(m)+":"

    if s < 10:
        res += "0"+str(s)
    else:
        res += str(s)
    return res


def solution(play_time, adv_time, logs):
    TOTAL_TIME = chenge_to_second(play_time)+1
    log_list = [0]*TOTAL_TIME
    log_sum = [0]*(TOTAL_TIME+1)
    for log in logs:
        start, end = log.split("-")
        log_list[chenge_to_second(start)] += 1  # 영상 보기 시작한 시간
        log_list[chenge_to_second(end)] -= 1  # 영상 보기 끝난 시간

    for i in range(1, TOTAL_TIME):
        log_list[i] += log_list[i-1]

    for i in range(1, TOTAL_TIME+1):
        log_sum[i] = log_sum[i-1]+log_list[i-1]

    length = chenge_to_second(adv_time)

    answer_time = 0
    answer_val = 0
    for i in range(length, TOTAL_TIME+1):
        val = log_sum[i]-log_sum[i-length]
        if val > answer_val:
            answer_val = val
            answer_time = i-length
    return change_to_str(answer_time)


print(solution("02:03:55", "00:14:15", [
      "01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00", [
      "69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", [
      "15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
