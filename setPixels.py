from sense_hat import SenseHat

sense = SenseHat()

# Define some colours
g = (0, 255, 0) # Green
b = (0, 0, 0) # Black
o = (0, 0, 255) # Blue
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