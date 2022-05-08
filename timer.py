#prints time whenever use types anything

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
    return f'{hours}:{minutes}:{seconds}\n'

start_time=time.time()
while True:
    print("\n"*30)
    i=input(calc_hms(round(time.time()-start_time)))
    if i=="done":
        print("\n"*30)
        print("final time: " + calc_hms(round(time.time()-start_time)) + "\n")
        break