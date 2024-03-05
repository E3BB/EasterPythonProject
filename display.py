# Text display class

from misc_func import *

class Display():
    width = 20
    height = 10
    wiped_display = []
    display = []
    for h in range(height):
            new_line = []
            for w in range(width):
                new_line.append(".")
            wiped_display.append(new_line)
            display.append(new_line)

    def __init__(s):
        pass

    def wipe(s):
        s.display = [x[:] for x in s.wiped_display]
        #print("Wiped display!")

    def raw_change_pixel(s,x:int,y:int,letter:str):
        if x >= 0 and x <= s.width - 1 and y >= 0 and y <= s.height - 1:
            s.display[y][x] = letter
    
    def change_pixel(s,x:int,y:int,letter:str):
        x -= 1; y -= 1
        x = clamp(x,0,s.width - 1)
        y = clamp(y,0,s.height - 1)
        if x >= 0 and x <= s.width - 1 and y >= 0 and y <= s.height - 1:
            s.display[y][x] = letter

    def flip_display(s):
        for i in range(3):
            print()
        print("--------------------------------------")
        
        for h in range(s.height):
            new_line = ""
            for w in range(s.width):
                new_line += " " + s.display[h][w]
            print(new_line)
