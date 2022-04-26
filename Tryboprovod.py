import numpy as np
Ti = 293
TL = 400
TR = 293
alpha = 1.1E-4
x = [0,1]
xc = 50
dx = (1-0)/xc
rtol = 1E-4
T = [[Ti]*(xc)]
dt = (1/2)*(((dx)*(dx))/alpha)
i=1; j=1
while True:
    T.append([0]*xc)
    T[j][0] = 293
    T[j][49] = 400
    for z in range(1,49):
        T[j][z] = T[j-1][z] + ((alpha*dt)/((dx)*(dx)))*((T[j-1][z+1]) - (2*T[j-1][z]) + (T[j-1][z-1]))
        if np.max(np.array(T[-1])-np.array(T[-2]))<=rtol:
            break
    j +=1
    print(T)
    print (j)
    import numpy as np
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1)
    x = np.linspace(0,10**(-2))
    y = T[j]
    ax.plot(x,y)
    plt.title("График")
    plt.xlabel("Слева направо")
    plt.ylabel("Снизу вверх")
    plt.legend()
    plt.grid()
    plt.show()
