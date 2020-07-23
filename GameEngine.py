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


image_frame = tk.Frame(root, padx=3, pady=3, width=600, height = 400)
image_frame.grid(row=0, column=0, columnspan = 5)
image_frame.grid_propagate(False)

text_box_frame = tk.Frame(root, padx = 1, pady=1, width = 600, height = 150)
text_box_frame.grid(row=1,column=0, columnspan = 5)
text_box_frame.grid_propagate(False)
text_box = tk.Text(text_box_frame)
text_box.configure(state="disabled")
text_box.grid(sticky="nsew")

#====================STATS BOX=======================================#

stats_box_frame = tk.Frame(root, padx = 1, pady=1, width = 100, height = 570)
stats_box_frame.grid(row=0,column=5, rowspan = 4)
stats_box_frame.grid_propagate(False)
stats_box = tk.Text(stats_box_frame)
stats_box.configure(state="disabled")
stats_box.grid(sticky="nsew", rowspan = 1)

#==============================IMAGES============================#

image_list = []

image_list.append(ImageTk.PhotoImage(Image.open("images/title.png")))
image_list.append(ImageTk.PhotoImage(Image.open("images/image2.jpg")))


#============================IMAGE WINDOW=============================#

main_img_label = tk.Label(image_frame, image = image_list[0])
main_img_label.grid(row=0, column=0, sticky="nsew",
                    columnspan = 6, rowspan = 3)


#======================DETECT CLICKS=======================#


def detect_Click(button_pressed, queue, input_accepted):
    queue.put(button_pressed)
    print(queue.get())
    input_accepted.get().set()

#================================BUTTONS=============================#

button1 = tk.Button(root, text="1", padx=25,pady=1,
                            command=lambda : detect_Click(1, queue, input_accepted))
button1.grid(row=4,column=0)

button2 = tk.Button(root, text="2", padx=25,pady=1,
                            command=lambda : detect_Click(2, queue, input_accepted))
button2.grid(row=4,column=1)

button3 = tk.Button(root, text="3", padx=25,pady=1,
                            command=lambda : detect_Click(3, queue, input_accepted))
button3.grid(row=4,column=2)

button4 = tk.Button(root, text="4", padx=25,pady=1,
                            command=lambda : detect_Click(4, queue, input_accepted))
button4.grid(row=4,column=3)

button5 = tk.Button(root, text="5", padx=25,pady=1,
                            command=lambda : detect_Click(5, queue, input_accepted))
button5.grid(row=4,column=4)


start_button = tk.Button(root, text="Start Game", padx=3,pady=1,
                            command=lambda : startGame(text_box, main_img_label,
                                                       image_frame, image_list, start_button, queue, input_accepted))
start_button.grid(row=4,column=5)



root.mainloop()

