import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(0,180)
# y = np.cos(x * np.pi / 180.0)
#
# plt.plot(x,y)
# plt.show()
#
# x = np.arange(0, 3 * np.pi, 0.1)
# y_sin = np.sin(x)
# plt.plot(x, y_sin)
# plt.show()


def hw1():
    x = np.arange(0, 3 * np.pi, 0.1)
    y_cos = np.cos(x)

    plt.plot(x, y_cos)

    plt.show()

def hw2():
    n = 1024
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)

    T = np.arctan2(Y, X)
    plt.scatter(X, Y, s=75, c=T, alpha=.5)

    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)

    plt.show()

hw2()