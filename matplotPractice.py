#Program 1 to plot the line graph
import matplotlib.pyplot as plt
x = [1,2,9,4,7]
y = [10,5,8,4,2]
plt.plot(x,y)
plt.show()

#Program 2 to plot bar chart
import matplotlib.pyplot as plt
x = [1,2,9,4,7]
y = [10,5,8,4,2]
plt.bar(x,y)
plt.show()

#Program 3 to plot histogram
from matplotlib import pyplot as plt
y = [10,5,8,4,2]
plt.hist(y)
plt.show()

#Program 4 to plot scatter graph
import matplotlib.pyplot as plt
x = [1,2,9,4,7]
y = [10,5,8,4,2]
plt.scatter(x,y)
plt.show()

#Program 5
import matplotlib.pyplot as plt
y = [1,4,9,16,25,36,49,64]
x1 = [1,16,30,42,55,68,77,88]
x2 = [1,6,12,18,28,40,52,65]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
l1 = ax.plot(x1,y,'ys-')
l2 = ax.plot(x2,y,'ys-')
ax.legend(labels = ('tv','smartphone'), loc = 'lower right')
ax.set_title("Advertisement effect on sales")
ax.set_xlabel("medium")
ax.set_ylabel("sales")
plt.show()

#Program 6
import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0.01, 10.0, 0.001)
data1 = np.exp(t)
data2 = np.cos(0.4 * np.pi * t)
fig, ax1 = plt.subplots()
color = 'tab:orange'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp', color = color)
ax1.plot(t, data1, color = color)
ax1.tick_params(axis ='y', labelcolor = color)
ax2 = ax1.twinx()
color = 'tab:cyan'
ax2.set_ylabel('cos', color = color)
ax2.plot(t, data2, color = color)
ax2.tick_params(axis ='y', labelcolor = color)
fig.suptitle('matplotlib.axes.Axes.twinx()function Example\n\n', fontweight ="bold")
plt.show()


#Program 7 - stacked plots
import matplotlib.pyplot as plt
x = ['A','B','C','D']
y1 = [10, 20,10,30]
y2 = [20, 25,15,25]
plt.bar(x,y1,color='r')
plt.bar(x,y2,bottom=y1,color='b')
plt.show()

#Program 8
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels=mylabels, startangle=90, explode=myexplode, shadow=True, colors= mycolors)
#Two ways to use legend as seen below:
#plt.legend()
plt.legend(title = "Four Fruits:")
plt.show()

#Program 9
import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleep = [6,7,5,8,6]
eat =   [2,2,1,2,1]
work =  [5,7,10,8,6]
exercise=  [3,3,0,1,3]


plt.plot(color='green', label='sleep', linewidth=3)
plt.plot(color='blue', label='eat', linewidth=3)
plt.plot(color='red', label='work', linewidth=3)
plt.plot(color='black', label='play', linewidth=3)

plt.stackplot(days, sleep, eat, work, exercise, colors=['green','blue','red','black'])

plt.xlabel('days')
plt.ylabel('activities')
plt.title('5 DAY ROUTINE')
plt.legend()
plt.show()


#Program 10
import matplotlib.pyplot as plt
x = [10,20,30,40,50]
y = [20,40,60,80,100]
plt.plot(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Draw a line")
plt.show()

#Program 11
import matplotlib.pyplot as plt
x = ["Java","Python","PHP","Javascript","C#","C++"]
y = [22.2,17.6,8.8,8,7.7,6.7]
plt.bar(x,y, color='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language \n worldwide, Oct 2017 compared to a year ago")
plt.grid(True,color='red')
plt.show()


#Program 12
import matplotlib.pyplot as plt
import numpy as np
x=["mon","tue","wed","thu","fri","sat","sun"]
sleeping = np.array([8,7,9,10,8,9,7])
reading = np.array([5,6,4,5,4,5,6])
working = np.array([8,7,8,8,9,8,9])
tv = np.array([3,4,3,1,2,1,2])

plt.bar(x,sleeping,color="r")
plt.bar(x,reading,bottom=sleeping,color="b",)
plt.bar(x,working,bottom=sleeping+reading,color="k")
plt.bar(x,tv,bottom=sleeping+reading+working,color="g")
plt.xlabel("days of week")
plt.ylabel("my hours")
plt.title("my week consumption")
plt.show()