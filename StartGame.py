import tkinter as tk
import time
import threading
from queue import Queue
from pygame import mixer
mixer.init()

input_accepted = threading.Event()
player_input = 0

def writeToScreen(text_box, writing_text, delete):
    text_box.configure(state="normal")
    if delete == 'y':
        text_box.delete(1.0, tk.END)
    text_box.insert(tk.INSERT, writing_text)
    text_box.configure(state="disabled")

def displayStats(stats_box, writing_text):
    text_box.configure(state="normal")
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.INSERT, writing_text)
    text_box.configure(state="disabled")

def replace_image(main_img_label, image_frame, current_img):
    main_img_label.grid_forget()
    main_img_label = tk.Label(image_frame, image=current_img)
    main_img_label.grid(sticky="nsew")

def startGame(text_box,main_img_label, image_frame, image_list, start_button, queue, stats_box):
    global player_input
    global input_accepted
    start_button.configure(state="disabled")
    game_thread = threading.Thread(target = printHello, args=(text_box,
                                                              main_img_label, image_frame, image_list, queue, stats_box,))
    game_thread.start()

def printHello(text_box, main_img_label, image_frame, image_list, queue, stats_box):
    mixer.music.load('audio/174_Wizards_Tower.mp3')
    global input_accepted
    writeToScreen(text_box, "Welcome to.....\n", 'n')
    time.sleep(2)
    writeToScreen(text_box, "Game", 'n')
    mixer.music.play()
    while True:
        writeToScreen(text_box, "\n         MAIN MENU\n", 'n')
        writeToScreen(text_box, "1. New Game\n", 'n')
        writeToScreen(text_box, "2. Load Game\n", 'n')
        writeToScreen(text_box, "3. Exit\n", 'n')
        input_accepted.wait()
        input_accepted.clear() # reset event
        number = str(queue.get())
        writeToScreen(text_box, "You chose: ", 'y')
        writeToScreen(text_box, number, 'n')
        #queue.queue.clear() # clear queue
