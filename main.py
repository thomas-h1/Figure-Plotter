# Python Figure Plotter
import matplotlib.pyplot as plt
import numpy as np
import math as maths

def FunctionPlotter(f, xLower=0.0, xUpper=1.0, title='', xLab='', yLab=''):
# functionPlotter takes in a function, f, and plots it on a line graph.

# Citation: https://www.w3schools.com/python/matplotlib_plotting.asp

    increment = 0.01
    x_points = np.arange(xLower, xUpper+increment, increment, dtype = float)
    y_points = np.array(x_points)
    for i, x in enumerate(x_points):
        y_points[i] = f(x)


    plt.rcParams['mathtext.rm'] = 'Times'
    plt.rcParams['mathtext.it'] = 'Times:italic'
    plt.rcParams['mathtext.bf'] = 'Times:bold'
    plt.rc('font', family='Times')
    plt.rc('text', usetex=True)
    font = {'fontname':'Times New Roman', 'size':14}
    plt.plot(x_points, y_points)
    plt.title(title, **font)
    plt.xlabel(xLab, **font)
    plt.ylabel(yLab, **font)
    plt.show()

def function(x):
    answer = 1 + maths.exp(-x)
    return 1/answer

FunctionPlotter(function, -10, 10, title='Plot of Logistic Function', xLab='$t$', yLab = '$\sigma(t)$');