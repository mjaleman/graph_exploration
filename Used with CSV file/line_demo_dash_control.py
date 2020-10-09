"""
Demo of a simple plot with a custom dashed line.

A Line object's ``set_dashes`` method allows you to specify dashes with
a series of on/off lengths (in points).
"""

import csv

import numpy as np
import matplotlib.pyplot as plt

brand_ = []
Rating = []
with open("./Cereal.csv", 'r') as csv_file:
	cereal_reader = csv.DictReader(csv_file)
	for row in cereal_reader:
		brand_.append(row["Cereal Brands"])
		Rating.append(int(row["Rating"])) 

	x = np.linspace(0, len(brand_))
	dashes = [10, 10, 10, 10]  

	fig, ax = plt.subplots()
	y = Rating
	#Plots the rating of the cereal brand as the y.
	y_pos = np.arange(len(brand_))
	plt.xticks(y_pos, brand_)
	line1, = ax.plot(y)
	line1.set_dashes(dashes)
	plt.xlabel("Brands")
	plt.ylabel("Average Customer Ratings")
	plt.title("Ratings Per Brand")
	plt.show()
