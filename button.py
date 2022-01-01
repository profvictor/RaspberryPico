import machine
import utime
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        print("Botão pressionado")
        utime.sleep(0.5)