from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import utime
import freesans20
import writer

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

WIDTH  = 128                                          
HEIGHT = 64                                             

i2c = I2C(0)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    t= 27 - (reading - 0.706)/0.001721
    temperatura = "{:.2f}".format(t)
    oled.fill(0)
    oled.text("TEMPERATURA",20,10)
    font_writer = writer.Writer(oled, freesans20)
    font_writer.set_textpos(30, 30)
    font_writer.printstring(temperatura)
    font_writer.set_textpos(90, 30)
    font_writer.printstring("C")
    oled.show() 
    utime.sleep(2)
    
