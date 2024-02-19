from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Dice

dice1 = Dice() # D6 dice
dice2 = Dice(10) # D10 dice

results = []
for roll_num in range(50_000):
    result = dice1.roll() + dice2.roll()
    results.append(result)

frequencies = []
max_result = dice1.num_sides + dice2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, max_result + 1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title' : 'Wynik', 'dtick' : 1}
y_axis_config = {'title' : 'Częstotliwość występowania wartości'}
my_layout = Layout(title = 'Wynik rzucania koścmi D6 i D10 pięćdziesiąt tysięcy razy', xaxis = x_axis_config, yaxis = y_axis_config)

offline.plot({'data' : data, 'layout' : my_layout}, filename = 'D6_D10.html')
