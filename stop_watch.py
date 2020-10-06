import time,os
count = 66600
stop_time = input("Set timer : ")
stop_timer = stop_time.lower()
stop_timer = stop_timer.split(' ')
stop_time_hour = 0
stop_time_min = 0
stop_time_sec = 0
repeat = True
for x in stop_timer:
    if 'h' in x:
        try:
            index = x.index('h')
            stop_time_hour += int(x[:index])
        except ValueError:
            if x == 'hour':
                stop_time_hour+=1
    elif 'm' in x:
        try:
            index = x.index('m')
            stop_time_min += int(x[:index])
        except ValueError:
            if 'minute' in x:
                stop_time_min +=1
    else:
        try:        
            index = x.index('s')
            stop_time_sec += int(x[:index])+count
        except ValueError:
            try:
                stop_time_sec += int(x)+count
                stop_time+=" seconds"
            except ValueError:
                if 'sec'in x:
                    stop_time_sec += 1
#stop_timer = str(stop_time_hour)+":"+str(stop_time_min)+":"+str(stop_time_sec-count)
timer = (stop_time_hour*3600)+(stop_time_min*60)+stop_time_sec
if timer==0:
    print('Timer not set')
    repeat=False
if repeat:
    repeat = input("Repeat : ")
    try:
        repeat = int(repeat)
        print('You will be notified for every ',stop_time,' only ',repeat,' times')
    except ValueError:
        if 'y' in repeat:
            repeat = True
            print('You will be notified for every : ',stop_time)
        else:
            repeat = 1
            print('You will be notified at : ',stop_time)
'''



        if len(stop_time)>1:
            index = stop_time[1].index('m')
            stop_time_min = int(stop_time[1][:index])  
    except ValueError:
        stop_time_min = 0
    timer = stop_time*3600+count
    d_time = time.ctime(timer)
    d_time = d_time.split(" ")
    print("You will be notified at : ",d_time[4])
    repeat = True
elif 'm' in stop_time:
    index = stop_time.index('m')
    stop_time = int(stop_time[:index])
    timer = stop_time*60+count
    d_time = time.ctime(timer)
    d_time = d_time.split(" ")
    print("You will be notified at : ",d_time[4])
    repeat = True
else:
    try:        
        index = stop_time.index('s')
        timer = int(stop_time[:index])+count
        d_time = time.ctime(timer)
        d_time = d_time.split(" ")
        print("You will be notified at : ",d_time[4])
        repeat = True
    except ValueError:
        try:
            timer = int(stop_time)+count
            repeat_time=stop_time+" seconds"
            d_time = time.ctime(timer)
            d_time = d_time.split(" ")
            print("You will be notified at : ",d_time[4])
            repeat = True
        except ValueError:
            print("Timer not set.")
            repeat = False
if repeat:
    repeat = input("Repeat : ")
    try:
        repeat = int(repeat)
        print('You will be notified for every ',stop_time,' only ',repeat,' times')
    except ValueError:
        if 'y' in repeat:
            repeat = True
            print('You will be notified for every : ',stop_time)
        else:
            repeat = False'''
            #print('No Repeat')
print('\n\n\n',end='')
x_timer = timer
repeat_count = 0
x_repeat = repeat
while True:
    realtime = time.ctime(count)
    realtime = realtime.split(" ")
    watch = realtime[4]
    if repeat>1:
        watch = "\t\t\t\t"+watch+"\t\t\t\t"+str(repeat_count)+"/"+str(x_repeat)
    else:
        watch = "\t\t\t\t"+watch+"\t\t\t\t"+str(repeat_count)
    print(watch,end = '\r')
    #print(stop_time)
    if count==timer:
        repeat_count+=1
        os.system('play -nq -t alsa synth {} sine {}'.format(1,5000))
        if str(repeat)=='True':
            timer+=x_timer-66600
        elif repeat>1:
            timer+=x_timer-66600
            repeat-=1
            #print(timer,count)
    else:
        time.sleep(1)
    count+=1
