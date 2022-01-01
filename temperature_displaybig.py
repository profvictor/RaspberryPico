import ssd1306big
import time

write = ssd1306big
#temperatura
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print('{:.2f}'.format(temperature))
    
    temp = str("{:.2f} ".format(temperature))
    write.clear()
    write.wrap(temp + "C")
    time.sleep(5)
