import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from time import sleep

root = tk.Tk()
root.resizable(False, False)
#--------Comands
fnlist = list()
def clickAddButton():
    fnlist.append(funtionEntry.get())
    fnListLabel.config(text="")
    funtions = ""
    
    for i in fnlist:
        funtions += "\n*"+i+"\n"
    fnListLabel.config(text=funtions)

def clickGraphButton():
    image = tk.PhotoImage(file='seno.png')
    graphic.create_image(320,240, image=image)
    x = np.linspace(-10, 10, 300)
    for i in fnlist:
        y = eval(i)
        plt.plot(x, y)
    plt.savefig('seno.png')
    plt.show()
    plt.close(fig='seno.png')
#--------Funtion Frame
fxFrame = tk.Frame(root)
funtionEntry = tk.Entry(fxFrame)
fnTitleLabel = tk.Label(fxFrame,text="FUNCIONES", font=("Times New Roman", 13))
fnListLabel = tk.Label(fxFrame)
addButton = tk.Button(fxFrame,text="Agregar", command=clickAddButton)
graphicButton = tk.Button(fxFrame,text="Gráficar", command=clickGraphButton)

funtionEntry.grid(row=0, column=0)
fnTitleLabel.grid(row=1, column=0)
fnListLabel.grid(row=2, column=0)
addButton.grid(row=3, column=0)
graphicButton.grid(row=4, column=0)
#---------Graphic Frame
grFrame = tk.Frame()
image = tk.PhotoImage(file='seno.png')
graphic = tk.Canvas(grFrame, width=640, height=480, bg="black")

graphic.grid(row=0, column=0)
#--------Frames
fxFrame.grid(row=1, column=0)
grFrame.grid(row=1, column=1)


root.mainloop()
