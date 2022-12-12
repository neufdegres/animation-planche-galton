import os
import cv2
from PIL import Image
from random import choice

trajectoire = ["left", "right"] 

cases = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

bille = Image.open("./pics/bille.png")
top = Image.open("./pics/top.png")

pos_0 = (246,15)
pos_1 = (246,56)
prev_pos = (246,56)

counter = 0

def create_folder():
    if os.path.exists("./tmp") :
        delete_folder()
    
    os.mkdir("./tmp")

def delete_folder():
    global counter
    files = os.listdir("./tmp")
    for pic in files:
        os.remove("./tmp/%s" % pic)
    os.rmdir("./tmp")

def reset_counter():
    global counter, cases
    counter = 0
    cases = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

def get_xy(direction):
    prev_x, prev_y = prev_pos
    if direction == "left":
        return (prev_x-25,prev_y+43)
    else:
        return (prev_x+25,prev_y+43)

def get_last_xy(direction):
    prev_x, prev_y = prev_pos
    if direction == "left":
        case = ((prev_x-25) // 50)
    else:
        case = ((prev_x+25) // 50)
    new_x = 12 + (case * 50)
    if cases[case] % 2 == 1 : new_x += 19
    floor = cases[case] // 2
    # new_y = (h total image) - h "sol" - h bille - (h billes déja empilées)
    new_y = 723 - 10 - 19 - (19 * floor) 
    cases[case] += 1
    return (new_x, new_y)

def creer_image(template, pos_x, pos_y):
    res = template.copy()
    res.paste(bille, (pos_x, pos_y), mask=bille)
    res.paste(top, (0,0), mask=top)
    filename = "./tmp/%s.png" % counter
    res.save(filename, "PNG")
    
def creer_video(fps):
    frameSize = (511,723)

    out = cv2.VideoWriter('video.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, frameSize)

    for i in range(counter):
        filename = "./tmp/%s.png" % i
        img = cv2.imread(filename)
        out.write(img)
    
    out.release()

def get_fps(billes):
    if billes < 30 : return 15
    if billes < 60 : return 30
    return 45


def creer_anim(billes):
    global counter, prev_pos
    
    create_folder()
    
    for i in range(billes):
        prev_pos = (246,56)
        if i == 0 :
            template = Image.new("RGB",(top.width, top.height),color=(185,191,196))
        else:
            template = Image.open("./tmp/%s.png" % (counter-1))
        for j in range(11):
            if j == 0:
                creer_image(template, *pos_0)
            elif j == 1:
                creer_image(template, *pos_1)
            elif j == 10:
                direction = choice(trajectoire)
                creer_image(template, *get_last_xy(direction))
            else:
                direction = choice(trajectoire)
                xy = get_xy(direction)
                creer_image(template, *xy)
                prev_pos = xy
                
            counter += 1
            
    fps = get_fps(billes)
    for k in range(fps): # "pause" de 1s sur la dernière image de l'anim
        last = Image.open("./tmp/%s.png" % (counter-1))
        filename = "./tmp/%s.png" % counter
        last.save(filename, "PNG")
        counter += 1
        
    creer_video(fps)
    
    delete_folder()
    reset_counter()