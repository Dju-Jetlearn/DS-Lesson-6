import matplotlib.pyplot as matpat

# Histograms

age = [22, 55, 36, 45, 21, 67, 45, 23, 89, 11, 33, 67, 88, 67, 89, 12, 6, 9, 48, 68, 18]
# bins are the ranges of vlaues grouped together to make bars in graphs
bin = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#hist is the function used for histograms
matpat.hist(age, bin, histtype = 'bar', rwidth = 0.8)
matpat.xlabel("X-axis")
matpat.ylabel("Y-axis")
matpat.title("Histogram")
matpat.show()

# Scatter plots

x = [1,2,3,4,5,6,7,8,9,10]
y = [0,1,0,1,0,1,0,1,0,1]

matpat.scatter(x,y, label = "Scatter plot", color = "red", marker = 'o', s = 50)
matpat.xlabel("X-axis")
matpat.ylabel("Y-axis")
matpat.title("Scatter plot")
matpat.show()

# Pie Chart

activities = ["sleeping", "school", "clubs", "eating", "relaxing", "homework", "playing"]
hours = [7, 6, 2, 2, 2, 3, 2]
clr = ['c', 'm', 'r', 'y', 'g']

matpat.pie(hours, labels = activities, colors = clr, startangle = 90, shadow = True)
matpat.title("Pie Chart")
matpat.show()

# Stackgraphs

days = [1,2,3,4,5]
eating = [7,8,4,3,2]
sleeping = [7,8,6,11,7]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

matpat.plot([], [], color = 'm', label = "Eating", linewidth = 5)
matpat.plot([], [], color = 'c', label = "Sleeping", linewidth = 5)
matpat.plot([], [], color = 'r', label = "Working", linewidth = 5)
matpat.plot([], [], color = 'k', label = "Playing", linewidth = 5)

matpat.stackplot(days, eating, sleeping, working, playing, colors = ['m', 'c', 'r', 'b'])

matpat.xlabel("x")
matpat.ylabel("y")
matpat.title("Stack Plot")
matpat.legend()
matpat.show()

# Multiple graphs at once

import numpy as np

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0, 5, 0.1)
matpat.figure()
matpat.subplot(221)
matpat.plot(t1, f(t1), 'bo')

t2 = np.arange(0, 5, 0.02)
matpat.subplot(224)
matpat.plot(t2, np.cos(2*np.pi*t2))

matpat.show()