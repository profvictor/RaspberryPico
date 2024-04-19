import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time

mouse = Mouse(usb_hid. devices)
keyboard = Keyboard(usb_hid.devices)
 
#MOUSE JIGGLER
while True:
    mouse.move (x=200)
    time. sleep(1)
    mouse.move(x=-200)
    time.sleep(1)
    
