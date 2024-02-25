
import math
from random import randint
from display import Display
from player import Player
from egg import Egg
from misc_func import *

running = True
init_refresh = True

disp = Display()
player = Player()

for i in range(5):
    Egg(randint(1,disp.width),randint(1,disp.height))

while running and player.cont and Egg.cont:  

    disp.wipe()
    
    if init_refresh == False:
        new_pos = player.tick()
    else: 
        new_pos = (player.x,player.y)
        init_refresh = False
    
    player.grab_egg(Egg.eggs)
    
    for i in Egg.eggs:
        disp.change_pixel(i.x,i.y,"E")
    
    disp.change_pixel(new_pos[0],new_pos[1],"P")
    disp.flip_display()

print("Game has stopped. Your score was:", str(Egg.score) + ". GGs")
print()
