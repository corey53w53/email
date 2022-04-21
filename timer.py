import time
s=time.time()
while True:
    print("\n"*30)
    time_passed=round(time.time()-s)
    hours, minutes = divmod(time_passed,3600)
    minutes, seconds = divmod(minutes, 60)
    hours, minutes, seconds = str(hours), str(minutes), str(seconds)
    if len(minutes)==1:
        minutes="0"+minutes
    if len(seconds)==1:
        seconds="0"+seconds
    i=input(f'{hours}:{minutes}:{seconds}\n')
    if i=="done":
        print("\n"*30)
        print(f'final time: {hours}:{minutes}:{seconds}\n')
        break