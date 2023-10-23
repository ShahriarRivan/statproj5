#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:58:56 2023

@author: shahriarrivan
"""
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
iris_df = pd.read_csv("/path/to/iris.csv")

# Subset the data
setosa_subset = iris_df[iris_df["species"] == "setosa"].sample(30)
versicolor_subset = iris_df[iris_df["species"] == "versicolor"].sample(20)
virginica_subset = iris_df[iris_df["species"] == "virginica"].sample(40)
subset_df = pd.concat([setosa_subset, versicolor_subset, virginica_subset])

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle("Iris Dataset Visualization Dashboard (Subset)", fontsize=16)

# Scatter Plot: Sepal Width vs. Sepal Length with red dots
axs[0, 0].scatter(subset_df["sepal_length"], subset_df["sepal_width"], color='red')
axs[0, 0].set_title("Scatter Plot: Sepal Width vs. Sepal Length")
axs[0, 0].set_xlabel("Sepal Length")
axs[0, 0].set_ylabel("Sepal Width")
axs[0, 0].grid(True)

# Bar Chart: Species Distribution
species_counts_subset = subset_df["species"].value_counts()
axs[0, 1].bar(species_counts_subset.index, species_counts_subset.values, color=['blue', 'green', 'red'])
axs[0, 1].set_title("Bar Chart: Species Distribution")
axs[0, 1].set_xlabel("Species")
axs[0, 1].set_ylabel("Count")
axs[0, 1].grid(axis='y')

# Pie Chart: Species Distribution as a percentage
colors = ['blue', 'red', 'green']
axs[1, 0].pie(species_counts_subset, labels=species_counts_subset.index, colors=colors, autopct='%1.1f%%')
axs[1, 0].set_title("Pie Chart: Species Distribution as a percentage")

# 3D Scatter Plot: 3D visualization of sepal length, sepal width, and petal length
ax_3d = fig.add_subplot(2, 2, 4, projection='3d')
colors_3d = subset_df["species"].map({'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'})
ax_3d.scatter(subset_df["sepal_length"], subset_df["sepal_width"], subset_df["petal_length"], c=colors_3d)
ax_3d.set_xlabel("Sepal Length")
ax_3d.set_ylabel("Sepal Width")
ax_3d.set_zlabel("Petal Length")
ax_3d.set_title("3D Scatter Plot: Sepal Length, Sepal Width, and Petal Length")

# Adjust layout and display the plots
plt.tight_layout()
plt.subplots_adjust(top=0.90)
plt.show()

