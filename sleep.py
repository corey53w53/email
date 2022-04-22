import time
init=time.time()

inc_in_mins=1
total_time_in_mins=30

total_time_limit=total_time_in_mins*60
increment=inc_in_mins*60

interval=time.time()+increment
while time.time()-init<total_time_limit:
    time_to_go=interval-time.time()
    time.sleep(time_to_go)
    print(f'{round((time.time()-init)/60)} minutes')
    interval+=increment
