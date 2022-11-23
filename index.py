import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

root = tk.Tk()
root.resizable(False, False)
root.config(bg="#FDF6E3")
#--------Comands
fnlist = list()
grColorList = {"Background":"#FDF6E3",
               "FnBackground":"#EEE8D5",
               "Grid":"#7F7F7F"}
def planeConf():
    fn.set_facecolor(grColorList["FnBackground"])
    plt.xlim(-10, 10)
    plt.ylim(-5, 10)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')

def machineDiagram(fx, minX = -10.0, maxX = 10.0, ran = 20, divisions = 50):
    x = np.linspace(minX, maxX, divisions)
    if isinstance(fx, list):
        y = fx
        fn.plot(x, y)
        planeConf()
        canvasFn.draw()
    else:
        y = eval(fx)
        fn.plot(x, y)
        planeConf()
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
    planeConf()
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
            machineDiagram(f"np.log({arg})/np.log({base})", minX=0.00001)
        elif "sin" in f:
            arg = f[f.index("(")+1:f.index(")")]
            machineDiagram(f"np.sin({arg})")
        elif "cos" in f:
            arg = f[f.index("(")+1:f.index(")")]
            machineDiagram(f"np.cos({arg})")
        elif "tan" in f:
            arg = f[f.index("(")+1:f.index(")")]
            machineDiagram(f"np.tan({arg})", minX=-10, maxX=10, divisions=1000)
        elif "x" in f:
            machineDiagram(f)
        else:
            fnConst = []
            for i in range(50):
                fnConst.append(float(f))
            machineDiagram(fnConst)
    fn.grid()
    canvasFn.draw()


def clickSaveButton():
    plt.savefig('gráfica.png')
    messagebox.showinfo("Save", "Se ha guardado el esquema como gráfica.png")

#--------Funtion Frame
fxFrame = tk.Frame(root, bg=grColorList["FnBackground"])
funtionEntry = tk.Entry(fxFrame, bg=grColorList["Background"])
fnTitleLabel = tk.Label(fxFrame,text="FUNCIONES", bg=grColorList["FnBackground"], font=("Times New Roman", 13))
fnListLabel = tk.Label(fxFrame, bg=grColorList["FnBackground"])
addButton = tk.Button(fxFrame,text="Agregar", command=clickAddButton, width=7, bg=grColorList["Background"])
eraseButton = tk.Button(fxFrame, text="Borrar", command=clickEraseButton, width=7, bg=grColorList["Background"])
graphicButton = tk.Button(fxFrame,text="Gráficar", command=clickGraphButton, width=7, bg=grColorList["Background"])
saveButton = tk.Button(fxFrame,text="Guardar", command=clickSaveButton, width=7, bg=grColorList["Background"])

funtionEntry.grid(row=0, column=0, padx=4, pady=1)
fnTitleLabel.grid(row=1, column=0, pady=1)
fnListLabel.grid(row=2, column=0, pady=1)
addButton.grid(row=3, column=0, pady=1)
eraseButton.grid(row=4, column=0, pady=1)
graphicButton.grid(row=5, column=0, pady=1)
saveButton.grid(row=6, column=0, pady=1)
#---------Graphic Frame
grFrame = tk.Frame()
fig, fn = plt.subplots(dpi=100, figsize=(5, 5), sharey=True,facecolor=grColorList["Background"])
canvasFn = FigureCanvasTkAgg(fig, master=grFrame)
canvasFn.get_tk_widget().grid(row=0, column=0)
planeConf()
fn.grid()
canvasFn.draw()
#--------Frames
fxFrame.grid(row=1, column=0, sticky='nsew')
grFrame.grid(row=1, column=1)


root.mainloop()
