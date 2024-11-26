import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

#Tabla de Iteraciones
head = ["n", "yn"]
tableData = []

#Solución EDO
sol = lambda t: np.exp(-t)

#Grafica de Solución
x = np.linspace(0,1, 100)
l = sol(x)

#Datos
f = lambda t, y: -2*y + np.exp(-t)
y0 = 1
y1 = 0.8187
h = 0.2
a = 0
b = 1
t = np.linspace(0, 1, round((b-a)/h) + 1)
y = np.zeros(len(t))

#Añadimos datos iniciales a el array y
y[0] = y0
y[1] = y1

#Añadimos primeros datos a la tabla
tableData.append([0, y[0]])
tableData.append([1, y[1]])

#Iteramos con la formula del metodo
for i in range(2, len(t)):
    y[i] = y[i-2] + 2*h*f(t[i-1], y[i-1])
    tableData.append([i, y[i]])

#Imprimimos la tabla
print(tabulate(tableData, headers = head, tablefmt= "grid"))

#Imprimimos las gráficas
plt.plot(x, l, label = "Solución EDO")
plt.plot(t, y, "o", label = "Aproximaciones")
plt.legend(loc = "best")
plt.show()
