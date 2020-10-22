"""
Board Setup:
 - Need: 3 Micro Servos, Jumper Wires
 
 Servo 1: Power(2), Ground(6), Control(3/GPIO2)
 Servo 2: Power(4), Ground(9), Control(5/GPIO3)
 Servo 3: Power(1), Ground(14), Control(7/GPIO4)
"""
import math
import numpy as np
from gpiozero import Servo
from time import sleep

#vel = 10
correction = 0.45
maxPW = (2.0 + correction) / 1000
minPW = (1.0 - correction) / 1000

# Difference in position of motors (higher value means higher frequency wave)
# diff = 120

def wiggle_servos(GPIOs, diff, vel):
    val = 0
    servos = [Servo(i, min_pulse_width=minPW, max_pulse_width=maxPW) for i in GPIOs]
    while True:
        val += vel
        for i in range(len(servos)):
            v = np.sin((i * diff + val) / 100.0) / 1.2
            servos[i].value = v
        sleep(0.05)

if __name__ == "__main__":
    wiggle_servos([2], 120, 10)
