import numpy as np
import matplotlib.pyplot as plt
import pdb

pi = np.pi

data = np.loadtxt("laserscan.dat")
angles = np.linspace(-pi / 2, pi / 2, data.shape[0], endpoint=True)

x = data * np.cos(angles)
y = data * np.sin(angles)

plt.plot(x, y, ".k", markersize=3)
plt.gca().set_aspect("equal")
plt.savefig("Robot Frame.jpeg")
plt.show()



g_T_r = np.array(
    [
        [np.cos(pi / 4), -np.sin(pi / 4), 1],
        [np.sin(pi / 4), np.cos(pi / 4), 0.5],
        [0, 0, 1],
    ]
)

r_T_l = np.array(
    [
        [np.cos(pi), -np.sin(pi), 0.2],
        [np.sin(pi), np.cos(pi), 0],
        [0, 0, 1],
    ]
)

g_T_l = np.matmul(g_T_r, r_T_l)

w = np.ones(len(x))
data_mat = np.array([x, y, w])

data_global = np.matmul(g_T_l, data_mat)

plt.plot(data_global[0,:], data_global[1,:], ".k", markersize=3)
plt.plot(g_T_r[0,2], g_T_r[1,2], '+b')
plt.plot(g_T_l[0,2], g_T_l[1,2], '+r')

plt.gca().set_aspect("equal")
plt.savefig("Global Frame.jpeg")
plt.show()


