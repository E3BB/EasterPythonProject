width = 20
height = 10
wiped_display = []
display = []
test_display = []
for h in range(height):
        new_line = []
        wipe_line = []
        for w in range(width):
            new_line.append(".")
        print(new_line)
        wiped_display.append(new_line)
        display.append(new_line)
for h in range(height):
        new_line = []
        for w in range(width):
            new_line.append(".")
        test_display.append(new_line)
display = [x[:] for x in wiped_display]
display[8][3] = "U"
print(display)
print(wiped_display)
#print(test_display)