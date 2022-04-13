def add_time(start, duration,curr_day=None):
    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    present=0
    day = 0
    duration=[int(d) for d in duration.split(':')]
    add =duration[0]*60 +duration[1]
    current = start.split()
    current_time = current[0].split(':')
    hours = int(current_time[0])
    minutes = int(current_time[1])
    if current[1]=="AM":
        present+=hours*60+minutes
    else:
        present+=(hours+12)*60 + minutes
    present+=add

    day+=present//1440
    present = present%1440
    present_hour=present//60
    present_min = present%60
    if present_min//10==0:
        present_min= '0'+str(present_min)
    if present_hour>=12:
        present_hour=present_hour%12
        time = f"{present_hour if present_hour!=0 else 12}:{present_min} PM"
    else:
        time = f"{present_hour if present_hour!=0 else 12}:{present_min} AM"

    if curr_day != None:
        day_out= day+days.index(curr_day.title())
        if day>0:
            if day == 1:
                output = time+f", {days[day_out%7]} (next day)"
            else:
                output = time + f", {days[day_out % 7]} ({day} days later)"
        else:
            output = time + f", {days[day_out % 7]}"
    else:
        if day>0:
            if day==1:
                output = time + f" (next day)"
            else:
                output = time + f" ({day} days later)"
        else:
            output = time

    return output




