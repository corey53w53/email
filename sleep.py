import time
init=time.time()
fifteen=time.time()+15
while True:
    time_to_go=fifteen-time.time()
    time.sleep(time_to_go)
    fifteen+=15
    time_passed=time.time()-init
    print(time_passed)
    print("end loop")
