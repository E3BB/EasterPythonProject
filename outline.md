# Easter Python Project - outline
Premise: Collect the Easter Bunny's eggs in a text adventure style maze.

Notable parts: Display, Player, Egg

Checklist:
- Display (Done)
- Player (Done)
- Egg (Done)

---

Display handles writing display made of text to screen. Pseudocode is this:
```
width = 20
height = 20

var new_display : display

for w in width:
  for h in height:
    new_display(w,h) = "."

new_display(player.x,player.y) = "P"

for egg in eggs:
  if egg.x < 0 or egg.y < 0: break
  else: new_display(egg.x,egg.y) = "E"

for y in new_display.y.length():
  line = ""
  for x in new_display.y.length():
    line += "" + new_display(x,y)
  print(line)
```

Player handles moving player. Pseudocode is this:
```
x : int
y : int
new_keys_pressed = {}
keys_last_pressed = {}

keys_last_pressed = new_keys_pressed
new_keys_pressed.assign()
for i in new_keys_pressed:
  if keys_last_pressed{i}:
    new_keys_pressed{i}.remove

if new_keys_pressed{w}: y -= 1
if new_keys_pressed{a}: x -= 1
if new_keys_pressed{s}: y += 1
if new_keys_pressed{d}: x += 1
```

Eggs handles picking up eggs and score-keeping. Pseudocode is this:
```
eggs_arr = []
#           Self
#            \/
egg __init__(s):
  s.x : int = randint(0,display.width)
  s.y : int = randint(0,display.height)
  eggs_arr += s

if player.x == x && player.y == y:
  score += 1
  eggs_arr -= s
  
```
