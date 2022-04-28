import tkinter as tk
import random
from tkinter import messagebox 

SIZE = 30       
moveX = 4      
moveY = 0      
type = random.randint(0, 6)        

timer = 800     
score = 0      

color = ["magenta", "blue", "cyan", "yellow", "orange", "red", "green", "black", "white"]


tetroT = [-1, 0, 0, 0, 1, 0, 0, 1]
tetroJ = [-1, 0, 0, 0, 1, 0, 1, 1]
tetroI = [-1, 0, 0, 0, 1, 0, 2, 0]
tetroO = [ 0, 0, 1, 0, 0, 1, 1, 1]
tetroL = [-1, 0, 0, 0, 1, 0,-1, 1]
tetroZ = [-1,-1, 0,-1, 0, 0, 1, 0]
tetroS = [ 0, 0, 1, 0, 0, 1,-1, 1]
tetro = [tetroT, tetroJ, tetroI, tetroO, tetroL, tetroZ, tetroS]


field = []
for y in range(22):
    sub = []
    for x in range(12):
        if x==0 or x==11 or y==21 :
            sub.append(8)
        else :
            sub.append(7)
    field.append(sub)


def drawTetris():
    for i in range(4):
        x = (tetro[type][i*2]+moveX)*SIZE
        y = (tetro[type][i*2+1]+moveY)*SIZE
        can. create_rectangle(x, y, x+SIZE, y+SIZE, fill=color[type])


def drawField():
    for i in range(21):
        for j in range(12):
            outLine=0 if color[field[i+1][j]]=="white" else 1   
            can.create_rectangle(j*SIZE, i*SIZE, (j+1)*SIZE, (i+1)*SIZE, fill=color[field[i+1][j]], width=outLine)


def keyPress(event):   
    global moveX, moveY
    afterX = moveX
    afterY = moveY
    afterTetro = []
    afterTetro.extend(tetro[type])
    if event.keysym=="Right" :     
        afterX += 1
    elif event.keysym=="Left" :     
        afterX -= 1
    elif event.keysym=="Down" :     
        afterY += 1
    elif event.keysym=="space" :    
        afterTetro.clear()
        for i in range(4):
            afterTetro.append(tetro[type][i*2+1]*(-1))
            afterTetro.append(tetro[type][i*2])
    judge(afterX, afterY, afterTetro)   

def judge(afterX, afterY, afterTetro):  
    global moveX, moveY
    result = True
    for i in range(4):
        x = afterTetro[i*2]+afterX
        y = afterTetro[i*2+1]+afterY
        if field[y+1][x]!=7 :
            result = False
    if result==True :
        moveX = afterX
        moveY = afterY
        tetro[type].clear()
        tetro[type].extend(afterTetro)
    return result

def dropTetris():
    global moveX, moveY, type, timer
    afterTetro = []
    afterTetro.extend(tetro[type])
    result = judge(moveX, moveY+1, afterTetro)
    if result==False :
        for i in range(4):
            x = tetro[type][i*2]+moveX
            y = tetro[type][i*2+1]+moveY
            field[y+1][x] = type
        deleteLine()
        type = random.randint(0, 6)
        moveX = 4
        moveY = 0
    can.after(timer, dropTetris)
    timer -= 2                          
    if timer<140 :
        timer = 180

def deleteLine():
    global score
    for i in range(1, 21):
        if 7 not in field[i]:
            for j in range(i):
                for k in range(12):
                    field[i-j][k] = field[i-j-1][k]
            score += 800-timer
    for i in range(1, 11):
        if 7 != field[1][i]:
            messagebox.showinfo("information", "GAME OVER !")
            exit()

  
win = tk.Tk()
win.geometry("340x630")
win.title("Rough TETRIS")
can = tk.Canvas(win, width=12*SIZE, height=21*SIZE)
can.place(x=-10, y=0)
var = tk.StringVar()
lab = tk.Label(win, textvariable=var, fg="blue", bg="white", font=("", "20"))   
lab.place(x=50, y=600)

win.bind("<Any-KeyPress>", keyPress)    

def gameLoop():
    can.delete("all")
    var.set(score)
    drawField()
    drawTetris()
    can.after(50, gameLoop)

gameLoop()
dropTetris()

win.mainloop()