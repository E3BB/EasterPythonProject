
import math
import random
from display import Display
from player import Player
from misc_func import *

running = True

disp = Display()
player = Player()

while running:  
    
    disp.wipe()

    #inp = str(input()).split()

    """try:
        next_x = int(inp[0])
        next_y = int(inp[1])
    except:
        running = False
        break
    next_char = inp[2]"""
    
    new_pos = player.tick()
    disp.change_pixel(new_pos[0],new_pos[1],"P")
    disp.flip_display()
