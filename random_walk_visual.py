import matplotlib.pyplot as plt
from randomwalk import RandomWalk

rw = RandomWalk(5_000)
rw.fill_walk()

fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth = 2)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()