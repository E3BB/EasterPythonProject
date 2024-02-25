
class Egg():

    eggs = []
    score = 0
    cont = True

    def __init__(s,x:int=1,y:int=1):
        s.x = x
        s.y = y
        Egg.eggs.append(s)
    
    def grab(s):
        Egg.eggs.remove(s)
        Egg.score += 1
        if Egg.eggs == []: Egg.cont = False

