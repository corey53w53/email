import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(type(current_time))
print(current_time)

