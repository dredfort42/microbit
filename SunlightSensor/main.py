from microbit import *

# Custom image map
image_data = [
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1],
]

def adjust_brightness(image_data, brightness):
    image_string = ""
    for row in image_data:
        row_string = "".join(str(val * brightness) for val in row)
        image_string += row_string + ":"
    return Image(image_string[:-1])

brightness = 5  # Set brightness (0-9)

while True:
    display.show(adjust_brightness(image_data, int(display.read_light_level() / 255 * 9)))
    sleep(100)