"""
* 원본 배열 정렬 필수
1. 작업이 없다면 더 낮은 시점에 시작되는 프로그램을 실행
2. 이 프로그램이 돌아가는 동안 실행되는 프로그램을 힙에다가 넣음 [구동시간, 실행시간]
3. 힙에서 꺼내서 돌림.
* 프로그램이 실행되고 종료까지 걸리는 시간은 반드시 answer 변수에 더해야함. 마지막에 총 개수로 나누면 문제 해결.
"""
from heapq import *

def solution(jobs):
    answer, progress = 0, 0  # 정답 변수, 현재 어디 ms를 처리 중인가?
    len_ = len(jobs)  # 길이를 저장
    i = 0  # 현재 처리한 progress(작업)의 개수
    heap = []  # 프로그램들이 들어갈 힙
    jobs.sort(key=lambda x: (x[0], x[1]))  # jobs 정렬
    
    while i != len_:
        while jobs and progress >= jobs[0][0]:  # 현재 ms보다 작거나 같은 작업
            poped = jobs.pop(0)  # 뽑
            heappush(heap, (poped[1], poped[0]))  # jobs[x][y]를 [y][x]로 바꿔 push... ms 단위가 앞으로 와야함. (정렬 이유)
        
        if jobs and not heap:  # jobs는 있으나 heap엔 없음... (=현재 처리할 작업이 없다.)
            poped = jobs.pop(0)  # 그냥 첫번째(제일 우선)을 뽑
            progress = poped[0]  # 현재 ms를 뽑은걸로 맞춤
            heappush(heap, (poped[1], poped[0]))  # 위와 마찬가지로 반전하여 heap에 push
        
        running_time, start_time = heappop(heap)  # heappop. 제일 우선된 작업을 pop
        progress += running_time  # 현재 ms를 running_time을 더한 값으로 저장
        
        answer += (progress) - start_time  # 현재 ms에 현재 작업을 시작한 타이밍을 빼면 요청부터 종료까지의 시간이 나옴.
        i += 1  # 작업 +1
            
    return answer // len_  # 총 개수를 나눠 평균을 구해 리턴




"""
너무 화나는 내 소스

from heapq import *

def solution(jobs):
    answer, process = 0, 0  # 정답 변수, 현재 어디 ms를 처리 중인가?
    len_jobs = len(jobs)
    heap = []  # 힙
    jobs.sort(key=lambda x: (x[0], x[1]))  # jobs 리스트 x: x[0] 기준 정렬
    print("jobs:", jobs)
    
    while jobs:
        ### 아무것도 돌아가는게 없어 시작하는 첫 타이밍 구간 ###
        # timing = 실행시간 / time_run = 구동시간
        timing, time_run = jobs.pop(0)  # 맨 먼저 실행될 친구
        running_time = time_run + timing # jobs가 실행되는 구간 (끝나는 시점 시간)
        
        #print(running_time)
        
        ### process(현재) 시간을 현재 작업이 끝나는 시간으로 변경###
        process = timing + time_run
        answer += time_run
        
        #print("process", process, "answer+", time_run)
        
        ### 현재 처리중인 작업의 시간에 할당된 작업들을 heap에 push함 ###
        while jobs:
            if jobs[0][0] < running_time:
                timing_, time_run_ = jobs.pop(0)
                heappush(heap, [time_run_, timing_])
            else:
                break
                
        ### heap 내 작업들을 처리 ###
        #print("CUR HEAP: ", heap)
        while heap:
            # task[0] = 구동시간 / task[1] = 실행시간
            task = heappop(heap)  # 힙 자료구조상 제일 실행시간이 짧은게 호출.
            while jobs:
                if jobs[0][0] < task[0]+task[1]:
                    timing_, time_run_ = jobs.pop(0)
                    heappush(heap, [time_run_, timing_])
                    #print("ADD HEAP:::", heap)
                else:
                    break
            #print("heappep:", task)
            # process 시간을 작업이 끝나는 시간으로 변경
            process += task[0]
            answer += (process - task[1])
            print("process:", process, "answer+: ", process-task[1])
    
    print("Total sum:" , answer)
    return answer // len_jobs
"""