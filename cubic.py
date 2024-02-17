import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, s = 10)

ax.set_title("Cubic", fontsize = 14)
ax.set_xlabel("Values", fontsize = 8)
ax.set_ylabel("Cubic values", fontsize = 8)

ax.tick_params(axis = 'both', which = 'major', labelsize = 14)

ax.axis([1, 30, 1, 900])
plt.show()