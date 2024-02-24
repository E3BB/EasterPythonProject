
import math
import random
from display import *

running = True

disp = Display()

"""def clamp(numa, maxm, minm):
    num = min(numa, maxm)
    num = max(numa, minm)
    return num"""

while running:  
    
    inp = str(input()).split()

    try:
        next_x = int(inp[0]) - 1
        next_y = int(inp[1]) - 1
    except:
        running = False
        break
    next_char = inp[2]

    """next_x = clamp(next_x,1,disp.width)
    next_y = clamp(next_y,1,disp.height)"""

    disp.wipe()
    disp.change_pixel(next_x,next_y,next_char)
    disp.flip_display()
