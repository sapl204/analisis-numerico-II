import numpy as np

def F(x1, x2):
    return np.array([4*x1**2-20*x1+x2**2/4 + 8, 
                    (x1*x2**2)/2+2*x1 - 5*x2 + 8])
def J(x1, x2):
    return np.matrix([[8*x1-20, x2/2], [x2**2/2 + 2, x1*x2 -5]])

x0 = np.zeros(2)
iter = 10
i = 0
x = x0
while i < iter :
    jac = J(*x)
    print("matriz jacobiana: \n", jac)
    fun = F(*x)
    s = np.linalg.solve(jac, (-1)*fun)
    x0 = np.copy(x)
    x = x + s
    if np.max(np.abs(x-x0)) < 1e-10:
        break 
    print(x)
    i += 1
