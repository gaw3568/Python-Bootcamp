# time 모듈 예제

import time

current_time = time.time()
print(f"Current time : {current_time}")

# GMT 기준 시간
gmt_time = time.gmtime()
print(f"GMT time : {gmt_time}")

# 현지 시간대 기준 시간
local_time = time.localtime()
print("현재 : ", end='')
print(f"{local_time.tm_year}년", end =' ')
print(f"{local_time.tm_mon}월", end = ' ')
print(f"{local_time.tm_mday}일", end = ' ')
print(f"{abs(local_time.tm_hour-12)}시", end = ' ')
print(f"{local_time.tm_min}분", end = ' ')
print(f"{local_time.tm_sec}초")

