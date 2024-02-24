# Player stuff class

class Player():

    valid_dir_inputs = ("w","a","s","d")

    def __init__(s,x:int=5,y:int=5):
        s.x = x
        s.y = y
    
    def tick(s):
        input_valid = False
        inp = ""
        while input_valid == False:
            inp = input("New direction (w: Up, s: Down, a: Left, d: Right)")
            if inp in s.valid_dir_inputs:
                input_valid = True
        if inp == "w": s.y -= 1
        elif inp == "a": s.x -= 1
        elif inp == "s": s.y += 1
        elif inp == "d": s.x += 1
        print(s.x,s.y)
        return (s.x,s.y)
