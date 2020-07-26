import tkinter as tk
import time
import threading
from queue import Queue
from pygame import mixer


#========================================================UTILITY FUNCTIONS=====================================================#

def writeToScreen(text_box, writing_text, delete): # Write to the main text widget, delete function clears text box
    text_box.configure(state="normal")
    if delete == 'y':
        text_box.delete(1.0, tk.END)
    text_box.insert(tk.INSERT, writing_text)
    text_box.configure(state="disabled")

def displayStats(stats_box, writing_text): # Write to the side text widget
    text_box.configure(state="normal")
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.INSERT, writing_text)
    text_box.configure(state="disabled")

def replace_image(img_canvas, image_frame, current_img, main_img): # Replace the Main Background Image
    img_canvas.itemconfig(main_img, image=current_img)

def replace_sprite(img_canvas, image_frame, sprite_img, sprite_img2, sprite_img3, player_img): # Replace the Main Background Image
    img_canvas.itemconfig(sprite_img, image=current_sprite)
    img_canvas.itemconfig(sprite_img2, image=current_sprite2)
    img_canvas.itemconfig(sprite_img3, image=current_sprite3)
    img_canvas.itemconfig(player_img, image=player_img)
    
def startGame(text_box, image_frame, image_list, start_button, queue, stats_box, sprite_img, sprite_img2, sprite_img3, player_img, img_canvas, current_img, main_img):
    global player_input
    global input_accepted
    start_button.configure(state="disabled")
    game_thread = threading.Thread(target = mainMenu, args=(text_box, image_frame, image_list, queue, stats_box, sprite_img, sprite_img2, sprite_img3, player_img, img_canvas, current_img, main_img,))
    game_thread.start()


#===============================================MAIN MENU=====================================================================================================#
def mainMenu(text_box, image_frame, image_list, queue, stats_box, sprite_img, sprite_img2, sprite_img3, player_img, img_canvas,current_img, main_img):
    global input_accepted
    writeToScreen(text_box, "Welcome to.....\n", 'n')
    time.sleep(2)
    writeToScreen(text_box, "Game!", 'n')
    while True:
        writeToScreen(text_box, "\n         MAIN MENU\n", 'n')
        writeToScreen(text_box, "1. New Game\n2. Load Game\n3. Credits\n4. Exit\n", 'n')
        input_accepted.wait()
        input_accepted.clear() # reset event
        number = str(queue.get())
        writeToScreen(text_box, "You chose: ", 'y')
        writeToScreen(text_box, number, 'n')
        #queue.queue.clear() # clear queue
