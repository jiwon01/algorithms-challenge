from datetime import datetime
import math

def get_time(in_time, out_time):
    # 가져온 시간 변수(HH:MM)을 파이썬 datetime 형식으로 변환.
    t_format = "%H:%M"
    in_t = datetime.strptime(in_time, t_format)
    out_t = datetime.strptime(out_time, t_format)
    
    # 시간 차이를 초단위로 -> 분 단위를 알기 위해 나눔 -> int, abs
    return abs(int((in_t - out_t).total_seconds() / 60))
    
def get_calc(fees, time):
    # 기본 요금데스~
    price = fees[1]
    
    # 추가 요금 부과?
    if time > fees[0]:
        excluded = time - fees[0]  # 기본 요금 시간을 제외
        price += math.ceil(excluded / fees[2]) * fees[3]  # 추가 요금 계산

    return price

def solution(fees, records):
    answer = []    # 정답 반환할 변수
    car_time = {}  # 각 차량별 총 시간 기록
    in_dict = {}   # 입차 시간 기록
    
    for v in records:
        time = v[:5]     # 시간
        plate = v[6:10]  # 번호
        act = v[11:]     # IN / OUT
        
        if act == "IN":  # 입차?
            in_dict[plate] = time
        else:            # 출차?
            if plate in car_time:  # 입출차했던 기록이 있는가? -> 기존에 +
                car_time[plate] += get_time(in_dict[plate], time)
            else:                  # 처음 입차 후 출차인가? -> 새로 car_time에 기록
                car_time[plate] = get_time(in_dict[plate], time)
            del in_dict[plate]     # 입차 기록에서 지우기~
    
    # 입차는 하였지만 출차 처리가 안된 애들 처리
    tasks = list(in_dict)  # 입차 기록에서 key를 tasks에 저장
    for v in tasks:        # 굴림
        if v in car_time:  # 위에서 했던 것과 동일. 출차 시간만 23:59로 지정
            car_time[v] += get_time(in_dict[v], "23:59")
        else:
            car_time[v] = get_time(in_dict[v], "23:59")
    
    # 정렬하여 순서대로 처리하게하고, 가격 일괄 계산
    sorted_ = sorted(car_time.keys())
    
    for vv in sorted_:
        result = get_calc(fees, car_time[vv])
        answer.append(result)
    return answer