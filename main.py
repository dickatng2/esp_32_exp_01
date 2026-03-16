# version 56
import machine, time
from machine import Pin, PWM, Timer
from time import sleep
import sys
import network
import urequests
import os
import json

#from us import HCSR04
#sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=30000)

from ota import OTAUpdater
from wifi_config import SSID, PASSWORD

firmware_url = "https://github.com/dickatng2/ESP32LEDS/"
my_timer = Timer(4)

pwm = [26,13,27,14,2,15,23,25,33,12,4]
len_pwm = len(pwm)
duur = 1  # 
per = 60000 # timer voor update via ota in msec

pwm[0] = machine.PWM(Pin(26, Pin.OUT)) 
pwm[1] = machine.PWM(Pin(13, Pin.OUT))
pwm[2] = machine.PWM(Pin(27, Pin.OUT))
pwm[3] = machine.PWM(Pin(14, Pin.OUT))
pwm[4] = machine.PWM(Pin(2, Pin.OUT))
pwm[5] = machine.PWM(Pin(15, Pin.OUT))
pwm[6] = machine.PWM(Pin(19, Pin.OUT))
pwm[7] = machine.PWM(Pin(25, Pin.OUT))
pwm[8] = machine.PWM(Pin(33, Pin.OUT))
pwm[9] = machine.PWM(Pin(12, Pin.OUT))
pwm[10] = machine.PWM(Pin(05, Pin.OUT))             
 
def test01(num, dt):
    pwm[num].duty(100)
    time.sleep(dt)
  
def licht03(num, dt):                                        
    for i in range (0, num, 1):    
        for j in reversed(range(0, 20, 1)):            
            pwm[i].duty(j*50)
            time.sleep(dt/5)
            print (i,j)
        time.sleep(0)

def licht04(num, dt):                                        
    for i in range (0, num, 1):    
        pwm[i].duty(1023)
        pwm[((i+5) % len_pwm)].duty(600)
        pwm[((i+4) % len_pwm)].duty(400)
        pwm[((i+3) % len_pwm)].duty(100)
        pwm[((i+2) % len_pwm)].duty(0)
        time.sleep(dt)

def licht05(num, dt):                                        
    for i in reversed(range (0, num , 1)):    
        pwm[i].duty(1023)
        pwm[((i-5) % len_pwm)].duty(600)
        pwm[((i-4) % len_pwm)].duty(400)
        pwm[((i-3) % len_pwm)].duty(100)
        pwm[((i-2) % len_pwm)].duty(0)
        time.sleep(dt) 
            
def timer_test(a):
    ota_updater.download_and_install_update_if_available()
    print("callback")

def tijd():    
    print ("tijd")
    my_timer.init(mode=Timer.PERIODIC, period=per, callback=timer_test) 

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
tijd()
while True:    
  #   for i in range (0, 10, 1):
  #       licht04(len_pwm, duur)
  #   for i in range (0, 10, 1):
  #       licht05(len_pwm, duur)
  #   for i in range (0, 10, 1):
  #       licht03(len_pwm, duur)
    pwm[4].duty(100)
    pwm[10].duty(0)
    time.sleep(2)
    pwm[4].duty(0)
    pwm[10 ].duty(100)
    time.sleep(2)
   
     


