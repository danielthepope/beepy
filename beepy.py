#!/usr/bin/env python

from time import sleep
import datetime
import os

repeat = 3
fileLocation = '/home/pi/apps/beepy/alarms.txt'
alarmTimes = []
verbose = False

def beep(speed):
    if speed == 's':
        os.system('mpg321 /home/pi/apps/beepy/noise/beep5.mp3')
    elif speed == 'm':
        os.system('mpg321 /home/pi/apps/beepy/noise/beep25.mp3')
    elif speed == 'f':
        os.system('mpg321 /home/pi/apps/beepy/noise/beep125.mp3')

def speak(message):
    os.system('echo "' + message + '" | festival --tts')

def alarm(num, message):
    log("alarming")
    if num == 1:
        for i in range(repeat):
            beep('s')
            sleep(0.5)
    elif num < 4:
        for i in range(repeat):
            for j in range(num):
                beep('m')
            sleep(0.5)
            
    else:
        for i in range(repeat):
            for j in range(num):
                beep('f')
            sleep(0.5)
    if len(message) > 0:
        speak(message)
        
def loadAlarms():
    global alarmTimes
    alarmList = open(fileLocation, 'r').read().split('\n')
    alarmTimes = []
    for l in alarmList:
        if len(l) > 0:
            log(l)
            #Take one line and split it by a space
            # day/month/year hour:min channel
            date = l.split(' ')[0]
            #log(date)
            time = l.split(' ')[1]
            #log(time)
            channel = int(l.split(' ')[2])
            #log(channel)
            day = int(date.split('/')[0])
            #log(day)
            month = int(date.split('/')[1])
            #log(month)
            year = int(date.split('/')[2])
            #log(year)
            hour = int(time.split(':')[0])
            #log(hour)
            minute = int(time.split(':')[1])
            #log(minute)
            message = ""
            try:
                message = l.split(' ', 3)[3]
            except:
                message = ""
            alarmTimes.append((year, month, day, hour, minute,
                               channel, message))
    log("Alarms:\n" + str(alarmTimes) + "\n")

def log(message):
    if verbose:
        print message

if __name__ == '__main__':
    log("Beepy has started.")
    while (True):
        loadAlarms()
        for a in alarmTimes:
            #Match a[0] with year, a[1] with month, a[2] with day etc.
            now = datetime.datetime.now()
            if (a[0] == now.year and a[1] == now.month and a[2] == now.day
                and a[3] == now.hour and a[4] == now.minute):
                alarm(a[5], a[6])
            else:
                log(str(now) + " is not " + str(a))
                continue
        sleep(5)
