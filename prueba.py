cadena = "log a(b)"
base = cadena[cadena.index("g")+2:cadena.index("(")]
print(base)
arrayNum = cadena[cadena.index("(")+1:len(cadena)-1]
print(arrayNum)
