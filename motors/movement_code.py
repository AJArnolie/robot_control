from motor import Robot
from time import sleep
from camera import cam_server

robot = Robot(l_ports=(23, 24, 25), r_ports=(14, 15, 18))

robot.drive_timed(1, 1, 6)
sleep(1)
robot.drive_timed(-0.5, 0.5, 1.5)
sleep(1)
robot.drive_timed(0.7, 0.7, 4)
sleep(3)
robot.drive_timed(0.8, -0.8, 4)
sleep(3)
robot.drive_timed(0.5, -1, 3)
