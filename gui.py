import sys
import threading
from time import sleep
from tkinter import *
from PIL import Image
from tkVideoPlayer import TkinterVideo

try:
    from video import *
except:
    print("Erreur: veuillez vous placer dans le dossier contenant \"gui.py\" et \"video.py\"")
    sys.exit(1)

pause_pushed = False

#-----------------------action boutons + autres fonctions

def thread_loop():
    while(True):
        if video == None: break
        if not pause_pushed and video.is_paused():
            video.play()
        else:
            sleep(1)   

def delete_video():
    if os.path.exists("./video.avi"):
        os.remove("./video.avi")

def play():
    global video, pause_pushed, loop
    state = {
        "play" : play_button['state'],
        "pause" : pause_button['state'],
        "stop" : stop_button['state']
        }
    
    if state["play"] == 'disabled' : return
    
    play_button.config(state='disabled')
    
    if state["pause"] == 'disabled' and state["stop"] == 'disabled': # play
        message_label.config(text="Chargement en cours...")
        root.update()
        nbr_billes = int(spinbox.get())
        creer_anim(nbr_billes) 
        message_label.config(text="")
        root.update()
        # création du widget de l'animation
        video = TkinterVideo(master=canvas_frame, scaled=True)
        video.place(x=0, y=0, anchor="nw", relwidth=1.0, relheight=1.0)
        video.load(r"video.avi")
        video.play()
        loop = threading.Thread(target=thread_loop)
        loop.start()
        
    elif state["pause"] == 'disabled': # resume
        pause_pushed = False
        video.play()
    
    pause_button.config(state='normal')
    stop_button.config(state='normal')
        
def pause():
    global pause_pushed
    if pause_button['state'] != 'disabled' :
        play_button.config(state='normal')
        pause_button.config(state='disabled')
        pause_pushed = True
        video.pause()
        
def stop():
    global loop, video
    if stop_button['state'] != 'disabled' :
        play_button.config(state='normal')
        pause_button.config(state='disabled')
        stop_button.config(state='disabled')
        video.destroy()
        video = None
        loop.join()
        loop = None
        delete_video()
        
def on_closing():
    global video
    if video != None:
        video.destroy()
        video = None
        loop.join()
        delete_video()
    fenetre.destroy()
    
#-----------------------création fenêtre

fenetre=Tk()

fenetre.title('Planche de Galton')
fenetre.geometry('400x650')
fenetre.minsize(400,620)
fenetre.maxsize(400,620)
fenetre.config(bg="#b9bfc4")

root = Frame(fenetre, bg="#b9bfc4")

#-----------------------title

title = Label(root, text='Planche de Galton\nAnimation', bg="#b9bfc4", fg="black", font=('UbuntuMono-R.ttf', '18'))
title.pack(side=TOP)

#-----------------------animation

pic = Image.open("./pics/top.png")
new_width, new_height = pic.width//2, pic.height//2
pic.close()

canvas_frame = Frame(root, bg="#b9bfc4")

video = None
loop = None

image = PhotoImage(file="./pics/resized_top.png")
canvas = Canvas(canvas_frame, width=new_width+10, height=new_height, bg="#b9bfc4")
canvas.create_image((new_width//2)+5, new_height//2, anchor=CENTER, image=image)

canvas.pack()

canvas_frame.pack(expand=YES, pady=(30,30))

#-----------------------nombre billes

spinbox_frame = Frame(root, bg="#b9bfc4")

spinbox_label = Label(spinbox_frame, text="Nombre de billes : ", bg="#b9bfc4", fg="black", font=('UbuntuMono-R.ttf', '12'))
spinbox_label.pack(side=LEFT)

spinbox = Spinbox(spinbox_frame, from_=20, to=70, increment=5, state='readonly', bg="#b9bfc4", width=10)
spinbox.pack()

spinbox_frame.pack()

#-----------------------message de chargement

message_label = Label(root, text="", bg="#b9bfc4", fg="red", font=('UbuntuMono-R.ttf', '10'))
message_label.pack()

#-----------------------boutons

buttons_frame = Frame(root, bg="#b9bfc4")

play_button = Button(buttons_frame, height=2, width=10, bg="#b9bfc4", text='▶', command=play)
pause_button = Button(buttons_frame, height=2, width=10, bg="#b9bfc4", text='||', state='disabled', command=pause)
stop_button = Button(buttons_frame, height=2, width=10, bg="#b9bfc4", text='■', state='disabled', command=stop)

buttons_frame.columnconfigure(1, weight=1)

play_button.grid(row=0, column=0)
pause_button.grid(row=0, column=1)
stop_button.grid(row=0, column=2)

buttons_frame.pack(side=BOTTOM)


root.pack(expand=YES)

fenetre.protocol("WM_DELETE_WINDOW", on_closing)

fenetre.mainloop()