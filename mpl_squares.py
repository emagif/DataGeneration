import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth = 3)
ax.scatter(input_values, squares, s = 20)

ax.set_title("Kwadraty liczb", fontsize = 15)
ax.set_xlabel("Wartość", fontsize = 8)
ax.set_ylabel("Kwadraty wartości", fontsize = 8)

ax.tick_params(axis = 'both', which = 'major', labelsize = 10)


plt.show()