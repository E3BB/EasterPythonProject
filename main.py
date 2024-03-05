
import math
from display import Display
from player import Player
from egg import Egg
from misc_func import *

running = True
init_refresh = True

disp = Display()
player = Player()
Egg.scr_width = disp.width
Egg.scr_height = disp.height

def clamp(x,minn,maxn):
    if x > maxn: x = maxn
    if x < minn: x = minn
    return x

for i in range(5):
    Egg()

print()
print("To play this easter egg hunt, you should type your input,")
print("then hit enter; because I don't yet know how to continually")
print("take input. - Elliott")
print()

while running and player.cont and Egg.cont:  

    disp.wipe()

    player.tick()
    player.x = clamp(player.x,1,disp.width)
    player.y = clamp(player.y,1,disp.height)

    Egg.px,Egg.py = player.x,player.y
    
    player.grab_egg(Egg.eggs)

    for i in Egg.eggs:
        disp.change_pixel(i.x,i.y,"E")
    
    disp.change_pixel(player.x,player.y,"P")
    if running and player.cont and Egg.cont:
        disp.flip_display()

print("Game has stopped. Your score was:", str(Egg.score) + ". GGs")
print()
input("Press and enter any key to close window ")
