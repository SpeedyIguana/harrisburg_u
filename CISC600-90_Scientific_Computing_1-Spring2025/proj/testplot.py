import plot
import math
import matplotlib.pyplot as plt


def f(x):
    return math.sin(2 * math.pi * x)


def g(x):
    return math.cos(20 * x) / x


def h(x):
    return -((x - 5) ** 2) / 10 + 1.25


plot.graph(f, show=False)  # plot f(x) but don't show it yet
plot.graph(g, xl=0.5, show=False)  # plot g(x) starting at lower subinterval x = 0.5
plot.graph(h, show=False)  # plot h(x) but don't show it yet
plt.title("3 functions")  # set graph title
plt.show()  # now show the plot of all functions graphed


# redefine h(x)
def h(x):
    return f(x) * g(x)


# plot h(x) (it will show only after the previous one is closed)
# we can also set upper x interval, x label, y label, title, and image file on disk...
plot.graph(
    fn=h,
    xl=0.5,
    xu=5,
    label_x="time (s)",
    label_y="voltage (v)",
    title="Sinusoidals",
    fig="waves.png",
)
