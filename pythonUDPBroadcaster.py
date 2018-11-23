from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.clear()

while True:
    bg = (0,0,0)
    temp = sense.get_temperature()
    sense.show_message(str(temp), scroll_speed=0.05, back_colour=bg)
    sleep(1000)
