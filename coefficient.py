import numpy as np

def maximumNorm(matrix):
    return np.max(np.sum(np.abs(matrix), 1))

def norm1(matrix):
    return np.max(np.sum(np.abs(matrix), 0))

def requestData():
    size = int(input("Ingrese el tamaño de la matriz: "))
    matrix = np.empty((size, size))
    for i in range(size):
        row = input(f"Ingrese la {i+1} fila de la matriz separada por comas :  ")
        matrix[i] = [ float(x) for x in row.split(",")]
    return matrix

while True:
    print("Ingrese la norma a utilizar: \n 1) Infinito \n 2) Norma 1 \n 3) Salir")
    option = int(input("---> "))
    if option == 1:
        matrix = requestData()
        inverse = np.linalg.inv(matrix)
        print(maximumNorm(matrix)*maximumNorm(inverse))
    elif option == 2:
        matrix = requestData()
        inverse = np.linalg.inv(matrix)
        print(norm1(matrix)*norm1(inverse))

    else: 
        break
        
        
