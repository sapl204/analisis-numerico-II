import numpy as np
from tabulate import tabulate
heads = ["t_k", "y_k"]
h = float(input("Ingrese el paso: "))
b = float(input("Introduzca el extremo izquierdo: "))
a = float(input("Introduzca el extremo derecho: "))
func = eval(input("Ingrese la función f: "))
y0 = float(input("Ingrese el valor inicial: "))
net = np.linspace(b, a, int((a-b)/h) + 1)
y = np.empty(int((a-b)/h) + 2)
h = net[1]-net[0]
y[0] = y0
for i in range(len(net)):
    yk = y0 + h*func(net[i], y[i])
    y0 = yk
    y[i+1] = yk
tableData = zip(net, y[1:])
print(tabulate(tableData, headers = heads, tablefmt="grid"))
