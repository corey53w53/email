import time

def calc_hms(time_passed):
    '''
    Calculates the hours, minutes, and seconds given the number of seconds.
    
    time_passed should be an integer

    Returns string in a readable format hh:mm:ss
    '''
    hours, minutes = divmod(time_passed,3600)
    minutes, seconds = divmod(minutes, 60)
    hours, minutes, seconds = str(hours), str(minutes), str(seconds)
    if len(minutes)==1: minutes="0"+minutes
    if len(seconds)==1: seconds="0"+seconds
    return f'{hours}:{minutes}:{seconds}'

def stopwatch(time_limit_in_mins, overtime=False):
    '''
    Counts from 0.
    
    time_limit_in_mins should be an int, the number of minutes the stopwatch should count to

    the time will be printed every second
    '''
    start_time=time.time()
    time_limit_in_secs=time_limit_in_mins*60

    interval=time.time()+1
    while time.time()-start_time<time_limit_in_secs:
        print("\n"*30+f'Stopwatch for {time_limit_in_mins} minutes:'+"\n"+calc_hms(round(time.time()-start_time)))
        time.sleep(interval-time.time())
        interval+=1
    t = time.localtime()
    start_time=time.time()
    while overtime:
        print("\n"*30+f'Finished stopwatch for {time_limit_in_mins} minutes at {time.strftime("%H:%M:%S", t)}')
        print(f'Overtime:'+"\n"+calc_hms(round(time.time()-start_time)))
        time.sleep(interval-time.time())
        interval+=1

stopwatch(90, overtime=True)