# Python Figure Plotter
import matplotlib.pyplot as plt
import numpy as np
import math as maths
def FunctionPlotter(f, xLower=0.0, xUpper=1.0, title="", xLab="", yLab=""):
# functionPlotter takes in a function, f, and plots it on a line graph.

# Citation: https://www.w3schools.com/python/matplotlib_plotting.asp

    increment = 0.01
    x_points = np.arange(xLower, xUpper+increment, increment, dtype = float)
    y_points = np.array(x_points)
    for i, x in enumerate(x_points):
        y_points[i] = f(x)

    print(y_points)
    plt.plot(x_points, y_points)
    plt.show()

def function(x):
    return maths.pow(x,2)

FunctionPlotter(function, -1, 1);