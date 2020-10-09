import csv
import matplotlib.pyplot as plt
import numpy as np


Brand = []
Bought = []
with open("./Cereal.csv", "r") as csv_file:
	cereal_reader = csv.DictReader(csv_file)
	for row in cereal_reader:
		Brand.append(row["Cereal Brands"])
		Bought.append(row["Purchased"])

	fig, ax = plt.subplots()
	n = 750
	ypos = np.arange(len(Bought))
	y = Bought
	scale = ('logit')
	for i in range(len(Brand)):
		value = Bought[i]
		legend_val = Brand[i]
		ax.scatter(i, value, label=legend_val)
	plt.xlabel("Cereal Brands")
	plt.ylabel("Amount Purchased")
ax.legend()
ax.grid(True)

plt.show()
