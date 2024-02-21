import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = '/home/emanuelg/DataGeneration/CSV/data/seattle-weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        high = int(float(row[2]))
        low = int(float(row[3]))
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

fig, ax = plt.subplots()
ax.plot(dates, highs, c = 'red', alpha = 0.5)
ax.plot(dates, lows, c = 'blue', alpha = 0.5)
ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

ax.set_title("Najwyższa i najnizsza temperatura w Seattle na przestrzeni lat", fontsize = 15)
ax.set_xlabel('', fontsize = 10)
fig.autofmt_xdate()
ax.set_ylabel('Temperatura(C)', fontsize = 10)
ax.tick_params(axis = 'both', which = 'major', labelsize = 10)

plt.show()


