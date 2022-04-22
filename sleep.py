import time
init=time.time()
print(time.time())
#print every 15 seconds
increment=5
fifteen=time.time()+increment
while True:
    time_to_go=fifteen-time.time()
    time.sleep(time_to_go)
    fifteen+=increment
    print(time.time()-init)
