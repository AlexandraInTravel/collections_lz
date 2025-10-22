import numpy as np 
import matplotlib.pyplot as plt
def f(x): #создание функции
    return x**3+3*x**2-4*x+1 #сама функция
x = np.arange(2, 22, 1) #координаты x точек, по которым будет строиться график
y = f(x) #значения y
plt.plot(x,y, color='red', marker='o', ) #создание графика
plt.show() #показ графика