import gpiozero as gpi
from time import sleep

class Motor:
    def __init__(self, a, b, ena):
        self.motor = gpi.Motor(a,b,enable=ena)

    def run_motor_time(self, power=1, seconds=1):
        self.run_motor(power)
        sleep(seconds)
        self.motor.stop()

    def run_motor(self, power=1):
        if power > 1 or power < -1:
            raise Exception("Invalid input for motor speed. Select value between 1 and -1.")
        if power >= 0:
            self.motor.forward(power)
        else:
            self.motor.backward(-power)


class Robot:
    def __init__(self, l_ports, r_ports):
        self.robot = gpi.Robot(left=l_ports, right=r_ports)
        self.ldir = -1
        self.rdir = -1

    def drive_timed(self, l_speed, r_speed, seconds):
        l_speed = self.ldir * l_speed
        r_speed = self.rdir * r_speed

        if l_speed > 1 or l_speed < -1:
            raise Exception("Invalid input for left motor speed. Select value between 1 and -1.")
        if l_speed >= 0:
            self.robot.left_motor.forward(l_speed)
        else:
            self.robot.left_motor.backward(-l_speed)
        
        if r_speed > 1 or r_speed < -1:
            raise Exception("Invalid input for right motor speed. Select value between 1 and -1.")
        if r_speed >= 0:
            self.robot.right_motor.forward(r_speed)
        else:
            self.robot.right_motor.backward(-r_speed)
        sleep(seconds)
        self.robot.left_motor.stop()
        self.robot.right_motor.stop()


    def drive(self, l_speed, r_speed):
        l_speed = self.ldir * l_speed
        r_speed = self.rdir * r_speed

        if l_speed > 1 or l_speed < -1:
            raise Exception("Invalid input for left motor speed. Select value between 1 and -1.")
        if l_speed >= 0:
            self.robot.left_motor.forward(l_speed)
        else:
            self.robot.left_motor.backward(-l_speed)
        
        if r_speed > 1 or r_speed < -1:
            raise Exception("Invalid input for right motor speed. Select value between 1 and -1.")
        if r_speed >= 0:
            self.robot.right_motor.forward(r_speed)
        else:
            self.robot.right_motor.backward(-r_speed)

    def stop(self):
        self.robot.left_motor.stop()
        self.robot.right_motor.stop()
