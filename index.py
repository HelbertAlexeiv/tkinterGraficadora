import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np 

root = tk.Tk()
root.resizable(False, False)
#--------Funtion Frame
checkFnConstante = tk.BooleanVar()
checkFnLineal = tk.BooleanVar()
checkFnCuadratica = tk.BooleanVar()
checkFnCubica = tk.BooleanVar()
checkFnRacional = tk.BooleanVar()
checkFnExponencial = tk.BooleanVar()
checkFnLogaritmica = tk.BooleanVar()
checkFnSeno = tk.BooleanVar()
checkFnCoseno = tk.BooleanVar()
checkFnTangente = tk.BooleanVar()

fxFrame = tk.Frame(root)
titleLabel = tk.Label(fxFrame,text="FUNCIONES", font=("Times New Roman", 13))

fnConstante = tk.Checkbutton(fxFrame, text="Funcion Constante", variable=checkFnConstante)
fnLineal = tk.Checkbutton(fxFrame, text="Funcion Lineal", variable=checkFnLineal)
fnCuadratica = tk.Checkbutton(fxFrame, text="Funcion Cuadratica", variable=checkFnCuadratica)
fnCubica = tk.Checkbutton(fxFrame, text="Funcion Cubica", variable=checkFnCubica)
fnRacional = tk.Checkbutton(fxFrame, text="Funcion Racional", variable=checkFnRacional)
fnExponencial= tk.Checkbutton(fxFrame, text="Funcion Exponencial", variable=checkFnExponencial)
fnLogaritmica = tk.Checkbutton(fxFrame, text="Funcion Logaritmica", variable=checkFnLogaritmica)
fnSeno = tk.Checkbutton(fxFrame, text="Funcion Seno", variable=checkFnSeno)
fnCoseno = tk.Checkbutton(fxFrame, text="Funcion Coseno", variable=checkFnCoseno)
fnTangente = tk.Checkbutton(fxFrame, text="Funcion Tangente", variable=checkFnTangente)

titleLabel.grid(row=0, column=0)
fnConstante.grid(row=1, column=0, sticky='W')
fnLineal.grid(row=2, column=0, sticky='W')
fnCuadratica.grid(row=3, column=0, sticky='W')
fnCubica.grid(row=4, column=0, sticky='W')
fnRacional.grid(row=5, column=0, sticky='W')
fnExponencial.grid(row=6, column=0, sticky='W')
fnLogaritmica.grid(row=7, column=0, sticky='W')
fnSeno.grid(row=8, column=0, sticky='W')
fnCoseno.grid(row=9, column=0, sticky='W')
fnTangente.grid(row=10, column=0, sticky='W')

#---------Graphic Frame
grFrame = tk.Frame()
image = tk.PhotoImage(file='seno.png')
graphic = tk.Label(grFrame, image=image)

graphic.grid(row=0, column=0, sticky='S')
#--------Frames
fxFrame.grid(row=1, column=0)
grFrame.grid(row=1, column=1)
root.mainloop()
