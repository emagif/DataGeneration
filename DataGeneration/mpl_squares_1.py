import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, s = 5)

ax.set_title("Kwadraty liczb", fontsize = 15)
ax.set_xlabel("Wartość", fontsize = 8)
ax.set_ylabel("Kwadraty wartości", fontsize = 8)

ax.tick_params(axis = 'both', which = 'major', labelsize = 10)

ax.axis([0, 1100, 0, 1100000])

plt.show()