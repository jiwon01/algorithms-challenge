from datetime import datetime
import math

def get_time(in_time, out_time):
    t_format = "%H:%M"
    in_t = datetime.strptime(in_time, t_format)
    out_t = datetime.strptime(out_time, t_format)
    
    return abs(int((in_t - out_t).total_seconds() / 60))
    
def get_calc(fees, time):
    price = fees[1]
    
    if time > fees[0]:
        excluded = time - fees[0]
        price += math.ceil(excluded / fees[2]) * fees[3]

    return price

def solution(fees, records):
    answer = []
    car_time = {}  # 각 차량별 총 시간 저장
    in_dict = {}
    
    for i, v in enumerate(records):
        time = v[:5]
        plate = v[6:10]
        act = v[11:]
        
        if act == "IN":
            in_dict[plate] = time
        else:
            if plate in car_time:
                car_time[plate] += get_time(in_dict[plate], time)
            else:
                car_time[plate] = get_time(in_dict[plate], time)
            del in_dict[plate]
    
    # 출차 처리가 안된 애들 처리
    tasks = list(in_dict)
    for v in tasks:
        if v in car_time:
            car_time[v] += get_time(in_dict[v], "23:59")
        else:
            car_time[v] = get_time(in_dict[v], "23:59")
    
    # 정렬하여 순서대로 처리하게하고, 가격 일괄 계산
    sorted_ = sorted(car_time.keys())
    
    for vv in sorted_:
        result = get_calc(fees, car_time[vv])
        answer.append(result)
    
    return answer
