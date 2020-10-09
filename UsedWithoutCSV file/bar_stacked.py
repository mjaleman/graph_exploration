# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt


N = 5
Cars = (20, 35, 30, 35, 27)
Trucks = (25, 32, 34, 20, 25)
CarsStandard = (2, 3, 4, 1, 2)
TrucksStandard = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, Cars, width, color='purple', yerr=CarsStandard)
p2 = plt.bar(ind, Trucks, width,
             bottom=Trucks, yerr=TrucksStandard)

plt.ylabel('Speed')
plt.title('Difference in Speed in 60 Seconds')
plt.xticks(ind, ('Nissan', 'Toyota', 'BMW', 'GM'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Cars', 'Trucks'))

plt.show()
