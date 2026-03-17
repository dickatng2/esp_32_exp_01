# version 1
import machine, time
from machine import Pin, PWM, Timer
from time import sleep
import sys
import network
import urequests
import os
import json
import asyncio
#import datetime as dt
#import schedule

rtc = machine.RTC()

from ota import OTAUpdater
from wifi_config import SSID, PASSWORD

firmware_url = "https://github.com/dickatng2/ESP_32_exp_01/"
my_timer = Timer(4)

duty_cycle_on = 1000
duty_cycle_off = 0

relais_1 = Pin(26, Pin.OUT)
relais_2 = Pin(33, Pin.OUT)
pir_pin = Pin(14, machine.Pin.IN)
buzzer = PWM(16, freq=500, duty_u16 = duty_cycle_off)

#buzzer.freq = 512

relais = tuple([relais_1,relais_2])
start_1 = False
start_2 = False
            
def job():
    print ('bezig')

async def monitor_pir():
    print ("pi started")
    while True:
        if pir_pin.value() == 1:       
            print ('motion detected')
            buzz_pulse(0.2, 500)
            await asyncio.sleep(1)
        await asyncio.sleep_ms(100)
            
def buzz_pulse(sec, sterkte):
    duty_cycle_on = sterkte
    buzzer.duty_u16(duty_cycle_on)
    time.sleep(sec)
    buzzer.duty_u16(duty_cycle_off)
    
            
def timer_test(a):
    ota_updater.download_and_install_update_if_available()
    print("callback")

def tijd():    
    print ("tijd")
    my_timer.init(mode=Timer.PERIODIC, period=60000, callback=timer_test) 

def uit(start,relais_num):    
    if start == True:    
        relais[relais_num].value(1)          
    else:                             
        relais[relais_num].value(0)
    print(relais_num, '  ', start)
    
async def io_task(rel_1, delay):
    await asyncio.sleep(delay)
        
ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
tijd()

# schedule.every(2).seconds.do(job)

while True:
    ymdhms = rtc.datetime()
    if ymdhms[6] % 10 == 0: 
        start_1 = True
        #buzz_pulse(0.2, 500)
    if ymdhms[6] % 13 == 0:
        start_1 = False
        #buzz_pulse(0, 500)
    if ymdhms[6] % 3 == 0: 
        start_2 = True
    if ymdhms[6] % 13 == 0:
        start_2 = False
 
    uit(start_1,0)
    uit(start_2,1)
    #buzzer.duty_u16(duty_cycle_on)
    #buzz_pulse(0.2, 500)




    
    
