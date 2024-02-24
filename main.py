
import math
import random
from display import *

running = True

disp = Display()

while running:  
    
    inp = str(input())
    
    try:
        int(inp[0])
        int(inp[2])
        str(inp[4])
    except:
        running = False
        break

    next_x = int(inp[0])
    next_y = int(inp[2])
    next_char = inp[4]

    disp.wipe()
    disp.change_pixel(next_x,next_y,next_char)
    disp.flip_display()
