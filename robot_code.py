from motors.motor import Robot, Motor
from time import sleep
import camera.cam_server as cs
import servos.servo_wiggle as se
from multiprocessing import Process

def drive_robot():
    robot = Robot(l_ports=(23, 24, 25), r_ports=(14, 15, 18))
    robot.drive_timed(1, 1, 4)
    sleep(1)
    robot.drive_timed(-0.5, 0.5, 1.5)
    sleep(1)
    robot.drive_timed(0.7, 0.7, 4)
    sleep(3)
    robot.drive_timed(0.8, -0.8, 4)
    sleep(3)
    robot.drive_timed(0.5, -1, 3)
    sleep(1)
    robot.drive_timed(1, .5, 3)
    robot.drive_timed(-.5, .5, 5)
    robot.drive_timed(-.7, -.7, 4)
    robot.drive_timed(.3, .3, 3)

processes = []

p_drive = Process(target=drive_robot)
p_cam = Process(target=cs.start_server)
p_servo = Process(target=se.wiggle_servos, args=((2,3), 120, 10))

p_drive.start()
p_cam.start()
p_servo.start()

processes.append(p_drive)
processes.append(p_cam)
processes.append(p_servo)

for p in processes:
    p.join()

