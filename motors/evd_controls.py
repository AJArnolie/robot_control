import evdev
import time

device = evdev.InputDevice('/dev/input/event1')
print(device)
#device /dev/input/event1, name "USB Keyboard", phys "usb-0000:00:12.1-2/input0"

for event in device.read_loop():
     if event.type == evdev.ecodes.EV_KEY:
         print(evdev.categorize(event))
time.sleep(.4)
