
import math
import random

class Display():
    width = 20
    height = 10
    wiped_display = []
    display = []

    def __init__(s):
        for h in range(s.height):
            new_line = []
            for w in range(s.width):
                new_line.append(".")
            s.wiped_display.append(new_line)
        s.display = s.wiped_display

    def wipe(s):
        s.display = []

    def change_pixel(s,x:int,y:int,letter:str):
        if x > 0 and x <= s.width and y > 0 and y <= s.height:
            s.display[y][x] = letter

    def flip_display(s):
        for h in range(s.height):
            new_line = ""
            for w in range(s.width):
                new_line += " " + s.display[h][w]
            print(new_line)

    def tick(s):
        s.update_display()

disp = Display()
disp.change_pixel(7,3,"P")
disp.flip_display()
