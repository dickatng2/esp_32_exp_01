# version 1
import machine, time
from machine import Pin, PWM, Timer
from time import sleep
import sys
import network
import urequests
import os
import json

rtc = machine.RTC()

from ota import OTAUpdater
from wifi_config import SSID, PASSWORD

firmware_url = "https://github.com/dickatng2/ESP_32_exp_01/"
my_timer = Timer(4)

relais_1 = Pin(26, Pin.OUT)
relais_2 = Pin(33, Pin.OUT)
relais = tuple([relais_1,relais_2])
start_1 = False
start_2 = False
            
def timer_test(a):
    ota_updater.download_and_install_update_if_available()
    print("callback")

def tijd():    
    print ("tijd")
    my_timer.init(mode=Timer.PERIODIC, period=6000, callback=timer_test) 

def uit(start,relais_num):    
    if start == True:    
        relais[relais_num].value(1)          
    else:                             
        relais[relais_num].value(0)
        
ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
tijd()

while True:
    ymdhms = rtc.datetime()
    if ymdhms[6] % 10 == 0: 
        start_1 = True
    if ymdhms[5] % 2 == 0:
        start_1 = False    
    if ymdhms[6] % 3 == 0: 
        start_2 = True
    if ymdhms[5] % 3 == 0:
        start_2 = False     
    
    uit(start_1,0)
    uit(start_2,1)


    
    
