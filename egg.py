
from random import randint

class Egg():

    eggs = []
    score = 0
    cont = True
    scr_width : int = 4
    scr_height : int = 2
    px = 1
    py = 1

    def __init__(s):
        s.x = randint(1,Egg.scr_width)
        s.y = randint(1,Egg.scr_height)
        def not_valid_space(egg):
            if egg.x == s.x and egg.y == s.y: return True
            elif egg.x == Egg.px and egg.y == Egg.py: return True
            else: return False
        while True in map(not_valid_space,Egg.eggs):
            s.x = randint(1,Egg.scr_width)
            s.y = randint(1,Egg.scr_height)
        Egg.eggs.append(s)
    
    def delete(s):
        Egg.eggs.remove(s)
        Egg.score += 1
        if Egg.eggs == []: Egg.cont = False
        Egg()
