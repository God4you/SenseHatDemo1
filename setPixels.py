from sense_hat import SenseHat
from time import sleep
from random import randint

from sense_hat import SenseHat

sense = SenseHat()

# Generate a random colour
def pick_random_colour():
  random_b = randint(0, 255)
  random_g = randint(0, 255)
  random_o = randint(0, 255)
  return (random_b, random_g, random_o)
  
# Define some colours
g = (0, 255, 0) # Green
b = (0, 0, 0) # Black
o = (0, 0, 255) # Blue
face = True

while True:
  # Set up where each colour will display
  
  if face == True:
    creeper_pixels = [
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, b, b, g, g, b, b, g,
        g, b, o, g, g, b, o, g,
        g, g, g, b, b, g, g, g,
        g, g, b, b, b, b, g, g,
        g, g, b, b, b, b, g, g,
        g, g, b, g, g, b, g, g
    ]
  else:
    creeper_pixels = [
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, b, b, g, g, b, b, g,
        g, o, b, g, g, o, b, g,
        g, g, g, b, b, g, g, g,
        g, g, b, b, b, b, g, g,
        g, g, b, b, b, b, g, g,
        g, g, b, g, g, b, g, g
    ]
  
  for event in sense.stick.get_events():
    if event.action == "pressed" and event.direction == "middle":
      g = pick_random_colour()
      o = pick_random_colour()
      

  # Display these colours on the LED matrix
  sense.set_pixels(creeper_pixels)
  
  face = True if face == False else False
  
  sleep(1)
  
