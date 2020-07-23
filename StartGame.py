import tkinter as tk
import threading
from queue import Queue
input_accepted = Queue()
input_accepted.put(threading.Event())
player_input = 0

def replace_image(main_img_label, image_frame, current_img):
    main_img_label.grid_forget()
    main_img_label = tk.Label(image_frame, image=current_img)
    main_img_label.grid(sticky="nsew")

def startGame(text_box,main_img_label, image_frame, image_list, start_button, queue, input_accepted):
    global player_input
    start_button.configure(state="disabled")
    game_thread = threading.Thread(target = printHello, args=(text_box,
                                                              main_img_label, image_frame, image_list, queue, input_accepted,))
    game_thread.start()

def printHello(text_box, main_img_label, image_frame, image_list, queue, input_accepted):    
    text_box.configure(state="normal")
    text_box.insert(tk.INSERT, "Welcome to...\n")
    text_box.configure(state="disabled")
    input_accepted.get().wait()
    input_accepted.get().clear() # reset event
    text_box.configure(state="normal")
    text_box.insert(tk.INSERT, "{}".format(queue.get()))
    text_box.configure(state="disabled")
