import usb_hid
import digitalio
import board
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Inicialize o teclado
keyboard = Keyboard(usb_hid.devices)

# Configure o pino do botão
button = digitalio.DigitalInOut(board.GP14)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

# Função para enviar a tecla quando o botão é pressionado
def send_key():
    keyboard.send(Keycode.H)

# Loop principal
while True:
    # Verifique se o botão está pressionado
    if button.value:
        send_key()
        # Aguarde um curto período para evitar pressionamentos de tecla repetidos
        time.sleep(0.2)

    # Aguarde um curto período entre as verificações do botão
    time.sleep(0.05)
