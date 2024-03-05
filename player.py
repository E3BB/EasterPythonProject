# Player stuff class

class Player():

    valid_dir_inputs = ("w","a","s","d","stop")

    def __init__(s,x:int=5,y:int=5):
        s.x = x
        s.y = y
        s.stop = False
        s.inp = ""
        s.cont = True
    
    def tick(s):
        input_valid = False
        while input_valid == False:
            s.inp = input("New direction (w: Up, s: Down, a: Left, d: Right, stop: Stop) ")
            print()
            if s.inp in s.valid_dir_inputs:
                input_valid = True
        
        if s.inp == "stop": s.cont = False
        elif s.inp == "w": s.y -= 1
        elif s.inp == "a": s.x -= 1
        elif s.inp == "s": s.y += 1
        elif s.inp == "d": s.x += 1
            
        return (s.x,s.y)
    
    def grab_egg(s,egg_arr):
        for egg in egg_arr:
            if egg.x == s.x and egg.y == s.y:
                egg.delete()
