import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time
 
mouse = Mouse(usb_hid. devices)
keyboard = Keyboard(usb_hid.devices)

#esse codigo e para fazer o mouse ficar movendo para direita e esquerda
#while True:
#    mouse.move (x=200)
#    time. sleep(1)
#    mouse.move(x=-200)
#    time.sleep(1)
    
while True:
    time.sleep(5)
    keyboard.send(Keycode.H)
    keyboard.send(Keycode.E)
    keyboard.send(Keycode.L)
    keyboard.send(Keycode.L)
    keyboard.send(Keycode.O)
    
    time.sleep(1)
    keyboard.send(Keycode.SPACE)
    time.sleep(1)

    keyboard.send(Keycode.W)
    keyboard.send(Keycode.O)
    keyboard.send(Keycode.R)
    keyboard.send(Keycode.L)
    keyboard.send(Keycode.D)
    keyboard.send(Keycode.SPACE)
    keyboard.send(Keycode.SHIFT, Keycode.ONE)
    keyboard.send(Keycode.ENTER)

    time.sleep(1)