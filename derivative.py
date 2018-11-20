import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import sin, linspace

def f(x):
    return sin(x)


x = linspace(0, 7 , 71)
y = sin(x)

delta_x=x[1]- x[0]

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Funkcija $Sin(x)$")
plt.plot(x, y , color = "#FF0000")
#plt.legend(["$sin(x)S"])
#plt.show()

y_first_derivative = (sin(x+delta_x) - sin(x)) / delta_x
plt.plot(x, y_first_derivative , color = "#00FF00")
#plt.legend(["$Sin(x)$" , "$sin \"(x)$"])
#plt.show()

N = len(x)
y_first_derivative_build_from_array = []
for i in range(N-1):
    temp = ( y[1+i] - y[i] ) /(delta_x)
    y_first_derivative_build_from_array.append(temp)
    #print(i,x[i], x[1+i] , y[i],y[1+i],temp,y_first_derivative_build_from_array)
    
plt.plot(x[0:N-1] , y_first_derivative_build_from_array, color = "#FFD700")
plt.legend(["$sin(x)$" , "$sin(x)\ (x)$" , "$sin\"(x)- build from array$"])
plt.show()


