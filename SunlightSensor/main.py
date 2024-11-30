from microbit import *

# Custom image map
image_data_level = [
    [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ],
    [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ],
    [
        [0,0,0,0,0],
        [0,1,0,1,0],
        [0,0,1,0,0],
        [0,1,0,1,0],
        [0,0,0,0,0]
    ],
    [
        [0,0,0,0,0],
        [0,1,1,1,0],
        [0,1,1,1,0],
        [0,1,1,1,0],
        [0,0,0,0,0]
    ],
    [
        [1,0,1,0,1],
        [0,1,1,1,0],
        [1,1,1,1,1],
        [0,1,1,1,0],
        [1,0,1,0,1]
    ],
    [
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1]
    ]
]

def adjust_brightness(brightness):
    image_string = ""

    grade = int(brightness / int(255 / 6))
    if grade > 5:
        grade = 5

    image = image_data_level[5 - grade]
    
    for row in image:
        row_string = "".join(str(val * (9 - grade)) for val in row)
        image_string += row_string + ":"
    return Image(image_string[:-1])


while True:
    display.show(adjust_brightness(display.read_light_level()))
    sleep(100)