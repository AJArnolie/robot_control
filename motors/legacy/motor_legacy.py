import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

class Motor:
    def __init__(self, a, b, enable):
        self.motor_a = a
        self.motor_b = b
        self.enable = enable
        GPIO.setup(a,GPIO.OUT)
        GPIO.setup(b,GPIO.OUT)
        GPIO.setup(enable,GPIO.OUT)
        self.pwm = GPIO.PWM(enable, 100) # configuring Enable pin means GPIO-04 for PWM
        self.pwm.start(100) # starting it with 100% dutycycle


    def run_motor_time(self, seconds):
        self.run_motor()
        sleep(seconds)
        self.stop_motor()

    def run_motor_time_speed(self, seconds, speed):
        self.run_motor_speed(speed)
        sleep(seconds)
        self.stop_motor()

    def run_motor(self):
        GPIO.output(self.motor_a,GPIO.HIGH) # to run motor in clockwise direction
        GPIO.output(self.motor_b,GPIO.LOW) # put it high to rotate motor in anti-clockwise direction
        GPIO.output(self.enable,GPIO.HIGH) # Should be always high to start motor
    
    def run_motor_speed(self, speed):
        self.pwm.ChangeDutyCycle(speed)
        GPIO.output(self.motor_a,GPIO.HIGH)
        GPIO.output(self.motor_b,GPIO.LOW)
        GPIO.output(self.enable,GPIO.HIGH)
        self.pwm.ChangeDutyCycle(100)

    def stop_motor(self):
        GPIO.output(self.motor_a,GPIO.LOW)
        GPIO.output(self.motor_b,GPIO.LOW)
        GPIO.output(self.enable,GPIO.LOW) # to stop the motor

    def end_run(self):
        self.pwm.stop()

class Robot:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def drive_timed(self, seconds):
        self.left.run_motor()
        self.right.run_motor()
        sleep(seconds)
        self.left.stop_motor()
        self.right.stop_motor()
    
    def drive_timed_speed(self, speed, seconds):
        self.left.run_motor_speed(speed)
        self.right.run_motor_speed(speed)
        sleep(seconds)
        self.left.stop_motor()
        self.right.stop_motor()
    
    def end_run(self):
        self.left.end_run()
        self.right.end_run()
