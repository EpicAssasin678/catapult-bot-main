import RPi.GPIO as GPIO          
from time import sleep

#creates movement for 4 wheels driven by l298n DC Motor Driver 
#Author: Zachery Uporsky
#Date: 4/28/21

#CLASS VARIABLES

pinConfig = [] #pin config
pinConfigA = [] #left L298N
pinConfigB = [] #right L298N



#Inits pin configuration , needs all pins configured per driver 
#Groups of 2 IN's and 1 EN pin
#Start all outputs as low

def initPinConfig (IN1, IN2, IN3, IN4, ENA, ENB):
    
    GPIO.setMode(GPIO.BCM)

    #first side of L298N
    GPIO.setup(IN1,GPIO.OUT)
    GPIO.setup(IN2,GPIO.OUT)
    GPIO.setup(ENA,GPIO.OUT)
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.LOW)
    p1=GPIO.PWM(ENA,1000)
    p1.start(25)

    #second side 
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4,GPIO.OUT)
    GPIO.setup(ENB,GPIO.OUT)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.LOW)
    p2=GPIO.PWM(ENB,1000)
    p2.start(25)

    print("Pin configurations initialized. Pins have been initialized as the following: ")
    print("IN1: " + IN1 +"\nIN2: " + IN2 + "\nENA: " + ENA + "\nIN3: " + IN3 + "\nIN4: " + IN4 + "\nENB: " + ENB)
    return [IN1, IN2, IN3, IN4, ENA, ENB]
    
    #function stubs
def calibrateMotors ():
    if not(pingConfigA == [] and pingConfigB == []):
        GPIO.output(pinConfigA[0], GPIO.HIGH)
        #then record rps with sensor
        
    pass


def forward():
    pass



def reverse():
    pass

#overload deg type, "RIGHT", "LEFT"
def forward(type):
    return True
    

def forward(degrees):
    return 1

def stop():
    pass



if __name__ == "__main__":
    GPIO.cleanup()
    
    pass