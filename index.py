import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from time import sleep

root = tk.Tk()
root.resizable(False, False)
#--------Comands
fnlist = list()

def machineDiagram(fx, minX = -10.0, maxX = 10.0, ran = 20):
    x = np.linspace(minX, maxX)
    y = eval(fx)
    fn.plot(x, y)
    canvasFn.draw()


def clickAddButton():
    fnlist.append(funtionEntry.get())
    fnListLabel.config(text="")
    funtions = ""
    
    for i in fnlist:
        funtions += "\n➤ "+i+"\n"
    fnListLabel.config(text=funtions)

def clickEraseButton():
    plt.cla()
    canvasFn.draw()
    fnlist.clear()
    fnListLabel.config(text="")

def clickGraphButton():
    plt.cla()
    otherFn = False
    for f in fnlist:
        if "log" in f:
            base = f[f.index("g")+1:f.index("(")]
            arg = f[f.index("(")+1:len(f)-1]
            machineDiagram(f"np.log({arg})/np.log({base})", minX=0.1)
            
        else:
            machineDiagram(f)



#--------Funtion Frame
fxFrame = tk.Frame(root)
funtionEntry = tk.Entry(fxFrame)
fnTitleLabel = tk.Label(fxFrame,text="FUNCIONES", font=("Times New Roman", 13))
fnListLabel = tk.Label(fxFrame)
addButton = tk.Button(fxFrame,text="Agregar", command=clickAddButton, width=7)
eraseButton = tk.Button(fxFrame, text="Borrar", command=clickEraseButton, width=7)
graphicButton = tk.Button(fxFrame,text="Gráficar", command=clickGraphButton, width=7)

funtionEntry.grid(row=0, column=0)
fnTitleLabel.grid(row=1, column=0)
fnListLabel.grid(row=2, column=0)
addButton.grid(row=3, column=0)
eraseButton.grid(row=4, column=0)
graphicButton.grid(row=5, column=0)
#---------Graphic Frame
grFrame = tk.Frame()
fig, fn = plt.subplots(dpi=100, figsize=(5, 5), sharey=True, facecolor="#FFFFFF")
canvasFn = FigureCanvasTkAgg(fig, master=grFrame)
canvasFn.get_tk_widget().grid(row=0, column=0)
canvasFn.draw()
#--------Frames
fxFrame.grid(row=1, column=0)
grFrame.grid(row=1, column=1)


root.mainloop()
