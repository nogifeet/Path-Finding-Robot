import RPi.GPIO as gpio
from time import sleep

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(4,gpio.OUT)
    gpio.setup(17,gpio.OUT)
    gpio.setup(27,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    #gpio.setup(24,gpio.OUT)
    #gpio.setup(25,gpio.OUT)
    
def forward(tf):
    init()
    gpio.output(4,False)
    gpio.output(17,True)
    gpio.output(27,True)
    gpio.output(22,False)
    sleep(tf)
    gpio.cleanup()
    
def reverse(tf):
    init()
    gpio.output(4,True)
    gpio.output(17,False)
    gpio.output(27,False)
    gpio.output(22,True)
    sleep(tf)
    gpio.cleanup()
    
def pivot_l(tf):
    init()
    gpio.output(4,False)
    gpio.output(17,True)
    gpio.output(27,False)
    gpio.output(22,True)
    sleep(tf)
    gpio.cleanup()
    
    
def pivot_r(tf):
    init()
    gpio.output(4,True)
    gpio.output(17,False)
    gpio.output(27,True)
    gpio.output(22,False)
    sleep(tf)
    gpio.cleanup()
