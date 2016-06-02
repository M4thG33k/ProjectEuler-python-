def isLeapYear(year):
    if (year%4==0):
        if (year%100==0):
            if (year%400==0):
                return True
            return False
        return True
    return False

daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = (1+365)%7 #we need to start in 1901 - not 1900
month = 0
year = 1901
numSundays = 0

while (year<2001):
    if (day==0):
        numSundays+=1
##        print(month+1,'\t',year,isLeapYear(year))
    day += daysInMonth[month]
    if month==1 and isLeapYear(year):
        day += 1
    day = day%7
    month += 1
    if month==12:
        month = 0
        year += 1

print(numSundays)
