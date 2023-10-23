#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:55:32 2023

@author: shahriarrivan
"""
import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ["Category A", "Category B", "Category C"]
values = [20, 40, 60]
colors = ["#FF5733", "#33FF57", "#3366FF"]

plt.figure(figsize=(15, 15))

# Case 1: Data Interpretation - Using color to highlight specific data points
plt.subplot(331)
plt.bar(categories, values, color=[colors[0], colors[1], colors[0]])
plt.title("Data Interpretation")
plt.xlabel("Categories")
plt.ylabel("Values")

# Case 2: Data Categorization - Using color to differentiate categories
plt.subplot(332)
plt.pie(values, labels=categories, colors=colors, autopct='%1.1f%%')
plt.title("Data Categorization")

# Case 3: Data Representation - Using a heatmap to represent data values
plt.subplot(333)
heatmap_data = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
plt.imshow(heatmap_data, cmap="coolwarm")
plt.colorbar()
plt.title("Data Representation")

# Case 4: Emphasis and Hierarchy - Using color to emphasize specific elements
plt.subplot(334)
highlighted_colors = [colors[0], colors[0], colors[2]]
plt.bar(categories, values, color=highlighted_colors)
plt.title("Emphasis and Hierarchy")

# Case 5: User Engagement - Using color for visual appeal
plt.subplot(335)
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.scatter(x, y, c=y, cmap='viridis')
plt.title("User Engagement")

# Case 6: Color Scales - Using a color scale for continuous data
plt.subplot(336)
gradient = np.linspace(0, 1, 256).reshape(1, -1)
gradient = np.vstack((gradient, gradient))
plt.imshow(gradient, aspect='auto', cmap='viridis')
plt.title("Color Scales")

# Case 7: Contrast - Using high contrast for readability
plt.subplot(337)
high_contrast_colors = ["black", "yellow", "white"]
plt.bar(categories, values, color=high_contrast_colors)
plt.title("Contrast")

# Case 8: Color Symbolism - Using colors with specific symbolism
plt.subplot(338)
symbolic_colors = ["red", "blue", "green"]
plt.bar(categories, values, color=symbolic_colors)
plt.title("Color Symbolism")

# Case 9: Consistency - Using consistent colors throughout a visualization
plt.subplot(339)
consistent_colors = [colors[1], colors[1], colors[1]]
plt.bar(categories, values, color=consistent_colors)
plt.title("Consistency")

plt.tight_layout()
plt.show()

