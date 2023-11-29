from tkinter import *
import time

f = open("input01.txt","r")
commands = f.read().split(sep = ", ")
commands = [c.strip() for c in commands]
print(commands)
f.close()

distances = [int(c[1:]) for c in commands]
print(sum(distances))
rotation_left_dict = {
    'N': 'W',
    'W': 'S',
    'S': 'E',
    'E': 'N'
}
rotation_right_dict = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N'
}

def get_dir(dir, rot):
    if rot == 'L':
        return rotation_left_dict.get(dir) 
    else:
        return rotation_right_dict.get(dir)

        
def next_pixel():
    global commands, current_dir    
    if len(commands) > 0:
        command = commands[0]
        deltas = (-1,0)
        if current_dir == 'N':
            deltas = (0,-1)
        elif current_dir == 'E':
            deltas = (1,0)
        elif current_dir == 'S':
            deltas = (0,1)
        # import pdb; pdb.set_trace()
        step = int(command[1:])-1
        if step == 0:
            commands = commands[1:]
            if len(commands) > 0:
                current_dir=get_dir(current_dir, commands[0][0:1])
        else:
            commands[0] = command[0:1] + str(step) 
        return deltas
    else:
        return None



root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas_width = 2000
canvas_height = 1000
border_color = "grey"

canvas = Canvas(root, width=canvas_width, height=canvas_height, bg=border_color)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

# Define the size of each pixel
pixel_size = 3

# Function to draw pixels with a delay
def draw_pixel(x, y):
    canvas.create_rectangle(
        x, y, x + pixel_size, y + pixel_size,
        fill="black", outline=border_color
    )

# Function to initiate the drawing of pixels
def draw_pixels():
    global current_x, current_y
    deltas = next_pixel()
    if deltas != None:
        delta_x, delta_y = deltas
        current_x += pixel_size * delta_x
        current_y += pixel_size * delta_y
        draw_pixel(current_x, current_y)
        root.after(10, draw_pixels)
    else:
        print("Finished drawing.")

# Initialize starting coordinates
current_x = canvas_width // 4
current_y = canvas_height // 2
current_dir=get_dir('N', commands[0][0:1])
# Start the drawing process
draw_pixels()

root.mainloop()

