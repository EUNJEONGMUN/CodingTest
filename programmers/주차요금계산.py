import math
from collections import defaultdict


def convert_time(start, end):
    s_h, s_m = start.split(":")
    e_h, e_m = end.split(":")
    start_time = int(s_h)*60+int(s_m)
    end_time = int(e_h)*60+int(e_m)

    return end_time-start_time


def solution(fees, records):
    cars = dict()  # 자동차 입출차 내역 저장
    time_dict = defaultdict(int)  # 자동차별 누적 시간

    for record in records:
        time, car_num, status = record.split()

        if status == "IN":
            cars[car_num] = time
        else:
            t = convert_time(cars[car_num], time)
            time_dict[car_num] += t
            del cars[car_num]

    # 출차 내역이 없는 차량 처리
    if cars:
        for car_num in cars:
            t = convert_time(cars[car_num], "23:59")
            time_dict[car_num] += t

    fee_list = sorted(time_dict.items(), key=lambda x: x[0])  # 자동차 번호 순으로 정렬

    res = []

    for key, value in fee_list:
        fee = fees[1]
        if value > fees[0]:
            fee += math.ceil((value-fees[0])/fees[2])*fees[3]
        res.append(fee)
    return res


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
      "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
