import time
init=time.time()

inc_in_mins=1
total_time_in_mins=90

total_time_limit=total_time_in_mins*60
increment=inc_in_mins*60

interval=time.time()+increment
print("\n"*30)
print(f'Starting timer for {total_time_in_mins} minutes.')
while time.time()-init<total_time_limit:
    time.sleep(interval-time.time())
    print("\n"*30)
    print(f'{round((time.time()-init)/60)} minutes')
    interval+=increment
