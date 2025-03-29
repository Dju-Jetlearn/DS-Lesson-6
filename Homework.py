import matplotlib.pyplot as mp

number = [423, 234, 453, 786, 231, 312, 352, 175, 707, 573, 648, 825, 735, 198, 425, 135, 846, 986, 846, 636, 735]
bin = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

mp.hist(number, bin, histtype = 'bar', rwidth = 0.5)
mp.xlabel("X-axis")
mp.ylabel("Y-axis")
mp.title("Histogram")
mp.show()

x = [14,21,35,49,54,65,77,83,92,101]
y = [0.5,1,0.2,0.7,0.3,1,0.9,0.1,0,1]

mp.scatter(x,y, label = "Scatter plot", color = "blue", marker = '^', s = 25)
mp.xlabel("X-axis")
mp.ylabel("Y-axis")
mp.title("Scatter plot")
mp.show()

activities = ["sleeping", "tennis", "homework", "class", "gaming", "socialising", "homework"]
hours = [8, 1, 1, 1, 4, 5, 4]
clr = ['c', 'm', 'r', 'y', 'r', 'g', 'b']

mp.pie(hours, labels = activities, colors = clr, startangle = 90, shadow = False)
mp.title("Pie Chart")
mp.show()