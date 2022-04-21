import time
s=time.time()

def calc_hms(time_passed):
    hours, minutes = divmod(time_passed,3600)
    minutes, seconds = divmod(minutes, 60)
    hours, minutes, seconds = str(hours), str(minutes), str(seconds)
    if len(minutes)==1:
        minutes="0"+minutes
    if len(seconds)==1:
        seconds="0"+seconds
    return f'{hours}:{minutes}:{seconds}\n'
while True:
    print("\n"*30)
    i=input(calc_hms(round(time.time()-s)))
    if i=="done":
        print("\n"*30)
        print("final time: " + calc_hms(round(time.time()-s)) + "\n")
        break