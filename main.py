import RPi.GPIO as gpio
import time
from motor_control import forward,reverse,pivot_l,pivot_r


gpio.setwarnings(False)
gpio.setmode(gpio.BCM)


def calculate_time(distance):
    '''
    Car travels 60 cms(approx) in 0.56 seconds
    velocity of the car is 107.14 cm / second
    subtract 0.1 seconds as approximation error
    '''
    if distance>100:
        t = distance/107.14285714
        return t-0.5
        
    if distance>50:
        t = distance/107.14285714
        return t-0.2
    
    elif distance>20:
        t = distance/107.14285714
        return t-0.1
    
    elif distance<=20:
        t = distance/107.14285714
        return t-0.05
    
    
    
    
    
def pwm_init():
    '''
    PWM GPIO Initialization
    '''
    #pwm_output
    gpio.setup(24,gpio.OUT)

def run_servo(angle):
    '''
    Servo Motor Control Function
    '''
    pwm_init()
    pwm = gpio.PWM(24,50) #servos like 50hz frequency
    pwm.start(5)
    duty = 1./20.*(angle)+2
    print("Turning motor at angle {}".format(angle))
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    pwm.stop()
    
def calculate_distance():
    gpio.setmode(gpio.BCM)
    echo=19 #trigger GPIO-ECHO pin
    trig=26 #trigger GPIO-TRIG pin
    gpio.setup(trig,gpio.OUT)
    gpio.setup(echo,gpio.IN)
    
    gpio.output(trig,True)
    time.sleep(0.0001)
    gpio.output(trig,False)

    while gpio.input(echo)==False:
        start = time.time()
        
    while gpio.input(echo)==True:
        end = time.time()
        
    sig_time = end-start
    distance = sig_time/0.000058
    return round(distance,0)


'''
0.25 seconds to pivot car 90 degrees
'''

while True:
    
    dist = calculate_distance()
    time.sleep(2)
    print("Distance is {} cm".format(round(dist,2)))
    if dist>10.00 and dist<400.00:
        print("Moving Forward")
        forward(calculate_time(dist))
        time.sleep(calculate_time(dist))
    
    elif dist>500.00:
        continue
    
    else:
        run_servo(90)
        dist = calculate_distance()
        time.sleep(2)
        print("Distance is {} cm".format(round(dist,2)))
        run_servo(0)
        pivot_l(0.25)
        time.sleep(1)
        dist = calculate_distance()
        time.sleep(2)
        print("Distance is {} cm".format(round(dist,2)))
        if dist>10.00 and dist<400.00:
            print("Moving in the Left Direction")
            forward(calculate_time(dist))
            time.sleep(calculate_time(dist))

            
        elif dist>500.00:
            continue
            
        else:
            pivot_r(0.5)
            dist = calculate_distance()
            time.sleep(2)
            print("Distance is {} cm".format(round(dist,2)))
            if dist>10.00 and dist<400.00:
                print("Moving in the Right Direction")
                forward(calculate_time(dist))
                time.sleep(calculate_time(dist))

            
            elif dist>500.00:
                continue
            
            else:
                run_servo(90)
                dist = calculate_distance()
                time.sleep(2)
                run_servo(0)
                print("Distance is {} cm".format(round(dist,2)))
                if dist>10.00 and dist<400.00:
                    pivot_r(0.25)
                    print("Moving in the Reverse Direction")
                    forward(calculate_time(dist))
                    time.sleep(calculate_time(dist))
                    
                elif dist>500.00:
                    continue
                           
gpio.cleanup()
