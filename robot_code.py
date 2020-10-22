"""
Setup for Robot Mk. 1 (Cardboard Bot)

Servos:
 - There are two servos that stick out of the front of the robot and wiggle
   Left Servo: Power(2), Control(3/GPIO2), Ground(9)
   Right Servo: Power(4), Control(5/GPIO3), Ground(39)
   
Motors:
 - Red and white wires from each motor connect to each pair of out ports on the HBridge
 - Red Wire from battery goes to 12v+ and Black Wire goes to ground on HBridge
 - Additional wire from HBridge ground to RPi Ground(6)
 - Seems to be an issue with this setup that burns out the Raspberry Pi --> Proceed with caution
   Left Motor:
    ENA ---> 22/GPIO25
    IN1 ---> 18/GPIO24
    IN2 ---> 16/GPIO23
   Right Motor:
    ENB ---> 12/GPIO18
    IN3 ---> 8/GPIO14
    IN4 ---> 10/GPIO15

Camera:
 - Used to stream video from robot to browser - Can be used for remote controlling of robot
 - Plug in camera to camera port
 
 Fan:
 - Red goes to any power, Black goes to any ground
"""

from motors.motor import Robot, Motor
from time import sleep
import camera.cam_server as cs
import servos.servo_wiggle as se
from multiprocessing import Process
import subprocess
import curses


def controlled_drive():
    robot = Robot(l_ports=(23, 24, 25), r_ports=(14, 15, 18))

    actions = {curses.KEY_UP    : robot.forward,
               curses.KEY_DOWN  : robot.backward,
               curses.KEY_LEFT  : robot.left,
               curses.KEY_RIGHT : robot.right}

def drive_controlled(window):
    robot = Robot(l_ports=(23, 24, 25), r_ports=(14, 15, 18))

    key = 0
    while True:
        key = window.getch()
        if key == 258: #UP
            robot.drive(-.2, -.2)
        elif key == 259: #DOWN
            robot.drive(.2, .2)
        elif key == 260: #LEFT
            robot.drive(.2, -.2)
        elif key == 261: #RIGHT
            robot.drive(-.2, .2)
        elif key == 36:
            robot.stop()
        sleep(0.01)

def drive_robot():
    robot = Robot(l_ports=(23, 24, 25), r_ports=(14, 15, 18))
    
    #robot.drive_timed(1, 1, 4)
    #sleep(1)
    #robot.drive_timed(-0.5, 0.5, 1.5)
    #sleep(1)
    #robot.drive_timed(0.7, 0.7, 4)
    #sleep(3)
    #robot.drive_timed(0.8, -0.8, 4)
    #sleep(3)
    #robot.drive_timed(0.5, -1, 3)
    #sleep(1)
    #robot.drive_timed(1, .5, 3)
    #robot.drive_timed(-.5, .5, 5)
    #robot.drive_timed(-.7, -.7, 4)
    #robot.drive_timed(.3, .3, 3)
    for i in range(30):
        robot.drive_timed(.7, .7, 3)
        sleep(1)
        robot.drive_timed(-0.5, 0.5, 1)
        sleep(1)

def main():
    processes = []

    #p_drive = Process(target=drive_robot)
    p_drive = Process(target=curses.wrapper, args=(drive_controlled,))
    p_cam = Process(target=cs.start_server)
    p_servo = Process(target=se.wiggle_servos, args=((2,3), 120, 10))

    p_drive.start()
    p_cam.start()
    #p_servo.start()

    processes.append(p_drive)
    processes.append(p_cam)
    #processes.append(p_servo)

    for p in processes:
        p.join()

if __name__ == "__main__":
    print("RPi IP Address: {}".format(subprocess.getoutput('hostname -I').split(" ")[0]))
    main()
