import math
import os

#function for checking first day of a month in a given year
def DayCheck(mm,yy):
    yy = str(yy)
    if(int(yy)%4 == 0):
        leap = True
    else:
        leap = False
    length = len(yy)
    dig = yy[length-2] + yy[length-1]
    dig1 = int(dig)
    mm = int(mm)
    yy = int(yy)
    dig1 = math.floor(dig1/4)
    dig1 +=1
    if(mm == 1 or mm == 10):
        dig1 += 1
    elif(mm == 2 or mm == 3 or mm == 11):
        dig1 += 4
    elif(mm == 4 or mm == 7):
        dig1 += 0
    elif(mm == 5):
        dig1 += 2
    elif(mm == 6):
        dig1 += 5
    elif(mm == 8):
        dig1 += 3
    elif(mm == 9 or mm == 12):
        dig1 += 6
    if(leap):
        if(mm == 1 or mm == 2):
            dig1 -=1
    if(yy >= 2000):
        dig1 += 6
    elif(yy >=1900):
        dig1 += 0
    elif(yy >= 1800):
        dig1 += 2
    elif(yy >= 1700):
        dig1 += 4
    elif(yy >= 1600):
        dig1 += 6
    elif(yy >=1500):
        dig1 += 0
    elif(yy >= 1400):
        dig1 += 2
    elif(yy >= 1300):
        dig1 += 4
    elif(yy >= 1200):
        dig1 += 6
    elif(yy >=1100):
        dig1 += 0
    elif(yy >= 1000):
        dig1 += 2
    elif(yy >= 900):
        dig1 += 4
    elif(yy >= 800):
        dig1 += 6
    elif(yy >=700):
        dig1 += 0
    elif(yy >= 600):
        dig1 += 2
    elif(yy >= 500):
        dig1 += 4
    elif(yy >= 400):
        dig1 += 6
    elif(yy >=300):
        dig1 += 0
    elif(yy >= 200):
        dig1 += 2
    elif(yy >= 100):
        dig1 += 4
    elif(yy >= 0):
        dig1 += 6
    dig1 += int(dig)
    day = dig1%7
    return day

#function displaying the calendar
def Calendar(mm = None,yy = None):
    switch = False
    switch2 = False
    if(yy == None):
        yy = input("Year : ")
    if(mm == None):
        mm = input ("Month : ")
    dayCount = 1
    nextWeekCount = 0
    weekCount = 0
    if(int(mm) == 1):
        monthName = "January"
    elif(int(mm) == 2):
        monthName = "February"
    elif(int(mm) == 3):
        monthName = "March"
    elif(int(mm) == 4):
        monthName = "April"
    elif(int(mm) == 5):
        monthName = "May"
    elif(int(mm) == 6):
        monthName = "June"
    elif(int(mm) == 7):
        monthName = "July"
    elif(int(mm) == 8):
        monthName = "August"
    elif(int(mm) == 9):
        monthName = "September"
    elif(int(mm) == 10):
        monthName = "October"
    elif(int(mm) == 11):
        monthName = "November"
    elif(int(mm) == 12):
        monthName = "December"
    if(int(yy)%4 == 0):
        leap = True
    else:
        leap = False
    length = len(str(yy)) + len(monthName)
    firstDay = DayCheck(mm,yy)
    os.system("CLS")
    for i in range(int(10-(length/2))):
        print(" ",end = '')
    print(monthName,yy)
    print("Mo Tu We Th Fr Sa Su")
    if(firstDay == 0):
        for i in range(16):
            print(" ",end = '')
        nextWeekCount = 2
    elif(firstDay == 1):
        for i in range(19):
            print(" ",end = '')
        nextWeekCount = 1
    elif(firstDay == 2):
        for i in range(1):
            print(" ",end = '')
        nextWeekCount = 7
    elif(firstDay == 3):
        for i in range(4):
            print(" ",end = '')
        nextWeekCount = 6
    elif(firstDay == 4):
        for i in range(7):
            print(" ",end = '')
        nextWeekCount = 5
    elif(firstDay == 5):
        for i in range(10):
            print(" ",end = '')
        nextWeekCount = 4
    elif(firstDay == 6):
        for i in range(13):
            print(" ",end = '')
        nextWeekCount = 3
    else:
        print("Something went wrong")
    while(True):
        mm = int(mm)
        if(mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12):
            if(dayCount == 32):
                break
        elif(mm == 4 or mm == 6 or mm == 9 or mm == 11):
            if(dayCount == 31):
                break
        else:
            if(leap):
                if(dayCount == 30):
                    break
            else:
                if(dayCount == 29):
                    break
        if(nextWeekCount == 0):
            if(switch):
                print()
            else:
                print(dayCount)
            nextWeekCount = 7
            switch2 = True
            continue
        else:
            if(switch2):
                if(dayCount<9):
                    print(" ",end ='')
                    switch2 = False
                else:
                    switch2 = False
            if(dayCount<9):
                print(dayCount," ",end='')
                dayCount+=1
                nextWeekCount-=1
                switch = True
            else:
                print(dayCount,"",end='')
                dayCount+=1
                nextWeekCount-=1
                switch = True

#main{
while(True):
    choose = input("Do you want to see a specific month or the whole year?\n1.Specific month\n2.Whole year\nNumber : ")
    if(choose == "1"):
        Calendar()
        break
    elif(choose == "2"):
        year = input("Enter a year : ")
        year = int(year)
        for i in range(1,13):
            Calendar(i,year)
            print("\n")
            x = input("Press enter to move to next month . . . ")
        break
    else:
        print("Not an option")
#}
