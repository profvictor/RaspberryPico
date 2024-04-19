import board
import usb_hid
import digitalio
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

btn1_pin = board.GP16
btn2_pin = board.GP17
btn3_pin = board.GP18

keyboard = Keyboard(usb_hid.devices)

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

while True:
    if btn1.value:
        print("button 1 pressed")
        #keyboard.send(Keycode.COMMAND, Keycode.A)
        #keyboard.send(Keycode.COMMAND, Keycode.C) 
        time.sleep(0.5)
        
    if btn2.value:
        print("button 2 pressed")
        #keyboard.send(Keycode.COMMAND, Keycode.V)  
        time.sleep(0.5)
        
    if btn3.value:
        print("button 3 pressed")
        #keyboard.send(Keycode.COMMAND, Keycode.V)  
        time.sleep(0.5)
