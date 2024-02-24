
import math
import random
from display import Display
from misc_func import *

running = True

disp = Display()

while running:  
    
    inp = str(input()).split()

    try:
        next_x = int(inp[0])
        next_y = int(inp[1])
    except:
        running = False
        break
    next_char = inp[2]
    disp.wipe()
    disp.change_pixel(next_x,next_y,next_char)
    disp.flip_display()
