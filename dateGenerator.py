#temp delete asap

import random

def randomDateGenerator():
    extraDay = [1,0,1,0,1,0,1,1,0,1,0,1]
    month = random.randint(1,12)
    if(extraDay[month-1]==1):
        day = random.randint(1,31)
    else:
        day = random.randint(1,30)
    if month == 2:
        day = random.randint(1,28)
    year = random.randint(17,19)
    if len(str(month)) == 1:
        month = "0" + str(month)
    else:
        month = str(month)
    if len(str(day)) == 1:
        day = "0" + str(day)
    else:
        day = str(day)
    return month + "/" + day + "/" + str(year)

def randomTimeGenerator():
    hour = random.randint(1,23)
    min = random.randint(1,59)
    sec = random.randint(1,59)
    if len(str(hour)) == 1:
        hour = "0" + str(hour)
    if len(str(min)) == 1:
        min = "0" + str(min)
    if len(str(sec)) == 1:
        sec = "0" + str(sec)
    return str(hour) + ":" + str(min) + ":" + str(sec)

print(randomDateGenerator())
print(randomTimeGenerator())





