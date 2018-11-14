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
g = pick_random_colour() # Green
b = (0, 0, 0) # Black
o = pick_random_colour() # Blue
while True:
# Set up where each colour will display
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

# Display these colours on the LED matrix
  sense.set_pixels(creeper_pixels)

  while True:
    sleep(1)
    sense.flip_h()