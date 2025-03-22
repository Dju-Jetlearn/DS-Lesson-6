import matplotlib.pyplot as mp

# Histograms

age = [22, 55, 36, 45, 21, 67, 45, 23, 89, 11, 33, 67, 88, 67, 89, 12, 6, 9, 48, 68, 18]
# bins are the ranges of vlaues grouped together to make bars in graphs
bin = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#hist is the function used for histograms
mp.hist(age, bin, histtype = 'bar', rwidth = 0.8)
mp.xlabel("X-axis")
mp.ylabel("Y-axis")
mp.title("Histogram")
mp.show()

# Scatter plots

x = [1,2,3,4,5,6,7,8,9,10]
y = [0,1,0,1,0,1,0,1,0,1]

mp.scatter(x,y, label = "Scatter plot", color = "red", marker = 'o', s = 50)
mp.xlabel("X-axis")
mp.ylabel("Y-axis")
mp.title("Scatter plot")
mp.show()

# Pie Chart

activities = ["sleeping", "school", "clubs", "eating", "relaxing", "homework", "playing"]
hours = [7, 6, 2, 2, 2, 3, 2]
clr = ['c', 'm', 'r', 'y', 'g']

mp.pie(hours, labels = activities, colors = clr, startangle = 90, shadow = True)
mp.title("Pie Chart")
mp.show()