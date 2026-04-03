# version 100
import machine, time
from machine import Pin, PWM, Timer
from time import sleep
import sys
import network
import urequests
import os
import json
import ntptime


SYNC_INTERVAL = 60
rtc = machine.RTC()

from ota import OTAUpdater
from wifi_config import SSID, PASSWORD

firmware_url = "https://github.com/dickatng2/ESP32LEDS/"
my_timer = Timer(4)

rel_1 = Pin(26, Pin.OUT) 
rel_2 = Pin(33, Pin.OUT)

rel_1_sec_on = [1,5], [14, 27] # [on/off][h/m/s] alarm setpoints rel
rel_1_sec_off = [0, 5], [30, 46] # setpoints rel 1 uit
rel_2_sec_on = [1,5], [15, 28] # setpoints rel 2 aan
rel_2_sec_off = [0, 5], [30, 45] # setpoints rel 2 uit

rel_1_min_on = [1, 4], [15, 29, 31] # setpoints rel 1 aan
rel_1_min_off = [0, 4], [30, 45] # setpoints rel 1 uit
rel_2_min_on = [1, 4],[ 15, 29] # setpoints rel 2 aan
rel_2_min_off = [0, 4],[30, 45] # setpoints rel 2 uit

rel_1_hh_on = [1,3],[ 1, 2] # setpoints rel 1 aan
rel_1_hh_off = [0, 3], [2, 3] # setpoints rel 1 uit
rel_2_hh_on = [1, 3],[ 3, 4] # setpoints rel 2 aan
rel_2_hh_off = [0,3],[ 5, 6] # setpoints rel 2 uit

rel_1_sec = [rel_1_sec_on, rel_1_sec_off]
rel_1_min = [rel_1_min_on, rel_1_min_off]
rel_1_hh = [rel_1_hh_on, rel_1_hh_off]
rel_2_sec = [rel_2_sec_on, rel_2_sec_off]
rel_2_min = [rel_2_min_on, rel_2_min_off]
rel_2_hh = [rel_2_hh_on, rel_2_hh_off]

rel_1_data = [rel_1, 0, rel_1_hh, rel_1_min, rel_1_sec]
rel_2_data = [rel_2, 0, rel_2_hh, rel_2_min, rel_2_sec]

rel = [rel_1_data, rel_2_data]



# def tijd_sync():
#     try: 
#     ntptime.settime() # Synchronize with NTP server
#     print("Time set:", time.localtime(),'  \r')
#     
# except:
#    print("Error setting time")

def timer_test(a):
    ota_updater.download_and_install_update_if_available()
    print("callback")

def tijd():    
    print ("tijd")
    my_timer.init(mode=Timer.PERIODIC, period=600000, callback=timer_test) 

def rel_startstop():    
    for i in rel:   
        i[0].value(i[1])

def check_alarm_time():
    t = time.localtime()
    for i in rel:
        #print (i)
        for m in range(2,5):
            #print(i(m))
            for j in i[m]:
                for n in range(0,2):
                    #print (j[0][0], j[0][1])
                    for o in j[1]:
                        #print (i[1],j[0][0],j[0][1],o)
                        if t[5] == o:
                            if i[1] != j[0][0]:
                                print ('toggle hit', t[5], i[0], i[1], j[0][0])
                                i[1] = j[0][0]

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
tijd()
while True:
    check_alarm_time()
    rel_startstop()
    time.sleep(0.5)
