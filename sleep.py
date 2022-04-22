import time
init=time.time()
#print every 15 seconds
total_time_limit=30
increment=5
fifteen=time.time()+increment
while time.time()-init<total_time_limit:
    time_to_go=fifteen-time.time()
    time.sleep(time_to_go)
    print(round(time.time()-init))
    fifteen+=increment
