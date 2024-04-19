import board
import usb_hid
import digitalio
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

#MOSTRANDO QUAL PINO É CADA BOTÃO
btn1_pin = board.GP16
btn2_pin = board.GP17
btn3_pin = board.GP18

#DEFININDO A VARIÁVEL TECLADO
keyboard = Keyboard(usb_hid.devices)

#DEFININDO O MODO DE CADA BOTÃO
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

#DEFININDO PARA COMEÇAR NO MODO 1
modo = 1  # Modo inicial

while True:
    if btn1.value:
        if modo == 1:
            print("button 1 pressed - Modo 1")
            keyboard.send(Keycode.A)
        else:
            print("button 1 pressed - Modo 2")
            keyboard.send(Keycode.C)
        
        time.sleep(0.5)
        
    if btn2.value:
        if modo == 1:
            print("button 2 pressed - Modo 1")
            keyboard.send(Keycode.B)
        else:
            print("button 2 pressed - Modo 2")
            keyboard.send(Keycode.D)
            
        time.sleep(0.5)
        
    if btn3.value:
        print("button 3 pressed - Trocando de Modo")
        modo = 2 if modo == 1 else 1  # Alternando entre os modos
        time.sleep(0.5)
