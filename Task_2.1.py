import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


U = 1 # convection velocity
dx = 0.01 # step along x
dt = 0.01 # timestep
t_final = 4.5 # simulation time
x_max = 1.5 # x range

x = np.arange(0, x_max+dx, dx)
t = np.arange(0, t_final+dt, dt)

# calculate courant number
courant = U*dt/dx

# define initial conditions
# square
def init_square(x):
    result = 0
    if x > 0.1 and x < 0.3:
        result = 1
    return result
square = np.vectorize(init_square)
# gaussian
gauss = lambda x: np.exp(-10*(4*x-1)**2)

# define and simulate the evolution of the initial condition
grid_1 = np.zeros([len(t), len(x)])
#grid_1 = grid_1.copy()
grid_1[0, :] = square(x)

for i_t in range(len(t)-1):
    for i_x in range(len(x)):
        grid_1[i_t + 1, i_x] = grid_1[i_t, i_x] - courant * (grid_1[i_t, i_x] - grid_1[i_t, i_x-1])
# plot simulation
fig, ax = plt.subplots()
line_1, = ax.plot(x, np.zeros(len(x)))
ax.set_ylim(-0.1, 1.1)


def animate(i, grid_1):
    line_1.set_ydata(grid_1[i+1, :])  # update the data.

    return line_1


ani = animation.FuncAnimation(
    fig, animate, fargs=(grid_1,), frames=len(t)-1, interval=20, blit=False)


plt.grid()
plt.show()
# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)
