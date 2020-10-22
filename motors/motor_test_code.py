from time import sleep
import motor as m

test_motor = m.Motor(23, 24, 25)

test_motor.run_motor_time(.5, 2)
sleep(3)
test_motor.run_motor_time(-.5, 2)
