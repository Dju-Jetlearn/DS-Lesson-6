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

days = [1, 2, 3, 4, 5, 6, 7]
sleeping = [9, 9, 9, 9, 9, 8, 7]
eating = [3, 3, 3, 3, 3, 4, 4]
working = [10, 9, 11, 10, 7, 2, 2]
sport = [1, 2, 0, 0, 1, 1, 1]
relaxing = [1, 1, 1, 1, 1, 9, 10]

mp.plot([], [], color = 'g', label = "Sleeping", linewidth = 5)
mp.plot([], [], color = 'y', label = "Eating", linewidth = 5)
mp.plot([],[], color = 'b', label = "Working", linewidth = 5)
mp.plot([], [], color = 'c', label = "Sport", linewidth = 5)
mp.plot([], [], color = 'r', label = "Relaxing", linewidth = 5)

mp.stackplot(days, sleeping, eating, working, sport, relaxing, colors = ['g', 'y', 'b', 'c', 'r'])

mp.xlabel("X")
mp.ylabel("Y")
mp.title("Stackplot")
mp.legend()
mp.show()