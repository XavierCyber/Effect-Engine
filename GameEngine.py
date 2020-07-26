import tkinter as tk
from PIL import Image, ImageTk
import time
import threading
from StartGame import *
from queue import Queue

queue = Queue()


root = tk.Tk()
root.title("Test")



#==============IMAGE AND MESSAGE FRAMES=================================#


image_frame = tk.Frame(root, width=600, height = 400)
image_frame.grid(row=0, column=0, columnspan = 5, rowspan = 3)
image_frame.grid_propagate(False)

img_canvas = tk.Canvas(root, width=600, height = 400)
img_canvas.grid(row=0, column=0, columnspan = 5, rowspan = 3)
img_canvas.grid_propagate(False)

text_box_frame = tk.Frame(root, padx = 1, pady=1, width = 600, height = 150)
text_box_frame.grid(row=3,column=0, columnspan = 5)
text_box_frame.grid_propagate(False)
text_box = tk.Text(text_box_frame)
text_box.configure(state="disabled")
text_box.grid(sticky="nsew")

#====================STATS BOX=======================================#

stats_box_frame = tk.Frame(root, padx = 3, pady=3, width = 100, height = 570)
stats_box_frame.grid(row=0,column=5, rowspan = 4)
stats_box_frame.grid_propagate(False)
stats_box = tk.Text(stats_box_frame)
stats_box.configure(state="disabled")
stats_box.grid(sticky="nsew", rowspan = 4)

#==============================IMAGES============================#

image_list = []

image_list.append(ImageTk.PhotoImage(Image.open("images/title.png")))

current_img = image_list[1]
sprite_img= image_list[1]
sprite_img2= image_list[1]
sprite_img3= image_list[1]
player_img= image_list[1]


#============================IMAGE WINDOW=============================#

main_img = img_canvas.create_image((0,0), image=image_list[0], anchor="nw")


#============================TEMP SPRITE SYSTEM======================#

sprite_img = img_canvas.create_image((50,50), anchor="nw")
sprite_img2 = img_canvas.create_image((100,100), anchor="nw")
sprite_img3 = img_canvas.create_image((50,150), anchor="nw")
player_img = img_canvas.create_image((500,100), anchor="nw")


#======================DETECT CLICKS=======================#


def detect_Click(button_pressed, queue):
    global input_accepted
    queue.put(button_pressed)
    input_accepted.set()

#================================BUTTONS=============================#

button1 = tk.Button(root, text="1", padx=25,pady=1,
                            command=lambda : detect_Click(1, queue))
button1.grid(row=4,column=0)

button2 = tk.Button(root, text="2", padx=25,pady=1,
                            command=lambda : detect_Click(2, queue))
button2.grid(row=4,column=1)

button3 = tk.Button(root, text="3", padx=25,pady=1,
                            command=lambda : detect_Click(3, queue))
button3.grid(row=4,column=2)

button4 = tk.Button(root, text="4", padx=25,pady=1,
                            command=lambda : detect_Click(4, queue))
button4.grid(row=4,column=3)

button5 = tk.Button(root, text="5", padx=25,pady=1,
                            command=lambda : detect_Click(5, queue))
button5.grid(row=4,column=4)


start_button = tk.Button(root, text="Start Game", padx=3,pady=1,
                            command=lambda : startGame(text_box, image_frame, image_list, start_button, queue, stats_box, sprite_img, sprite_img2, sprite_img3, player_img, img_canvas, current_img, main_img))
start_button.grid(row=4,column=5)



root.mainloop()

