# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:53:45 2023

@author: baniyaghoubm
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd


# Load the Iris dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris_data = pd.read_csv(url)

# Scatter Plot: Sepal Width vs. Sepal Length
plt.figure(figsize=(8, 6))
plt.scatter(iris_data["sepal_length"], iris_data["sepal_width"])
plt.title("Scatter Plot: Sepal Width vs. Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.grid(True)
plt.show()

# Line Chart: Petal Length over Species ID
plt.figure(figsize=(8, 6))
species_ids = range(len(iris_data))
plt.plot(species_ids, iris_data["petal_length"])
plt.title("Line Chart: Petal Length over Species ID")
plt.xlabel("Species ID")
plt.ylabel("Petal Length")
plt.grid(True)
plt.show()

# Bar Chart: Species Distribution
species_counts = iris_data["species"].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(species_counts.index, species_counts.values)
plt.title("Bar Chart: Species Distribution")
plt.xlabel("Species")
plt.ylabel("Count")
plt.grid(axis='y')
plt.show()

# Pie Chart: Species Distribution as a percentage
plt.figure(figsize=(8, 6))
plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%')
plt.title("Pie Chart: Species Distribution as a percentage")
plt.show()

# 3D Scatter Plot: 3D visualization of sepal length, sepal width, and petal length
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(iris_data["sepal_length"], iris_data["sepal_width"], iris_data["petal_length"])
ax.set_xlabel("Sepal Length")
ax.set_ylabel("Sepal Width")
ax.set_zlabel("Petal Length")
ax.set_title("3D Scatter Plot: Sepal Length, Sepal Width, and Petal Length")
plt.show()

fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Scatter Plot", "Bar Chart", "Pie Chart", "3D Scatter Plot"),
    specs=[[{"type": "scatter"}, {"type": "bar"}],
           [{"type": "pie"}, {"type": "scatter3d"}]]
)

fig.add_trace(
    go.Scatter(x=iris_data["sepal_length"], y=iris_data["sepal_width"], mode='markers'),
    row=1, col=1
)
species_counts = iris_data["species"].value_counts()
fig.add_trace(
    go.Bar(x=species_counts.index, y=species_counts.values),
    row=1, col=2
)
fig.add_trace(
    go.Pie(labels=species_counts.index, values=species_counts.values),
    row=2, col=1
)
fig.add_trace(
    go.Scatter3d(
        x=iris_data["sepal_length"], 
        y=iris_data["sepal_width"], 
        z=iris_data["petal_length"], 
        mode='markers'
    ),
    row=2, col=2
)
fig.update_layout(title_text="Iris Dataset Visualization Dashboard")
fig.show()


