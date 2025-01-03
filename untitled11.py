# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1smClOGEfA7B9A5Q52ATvPVkLLDLHEUhV
"""

import pandas as pd

# Read the CSV file
file_path = "/content/WHO COVID-19 cases.csv"  # Replace with the actual file path
data = pd.read_csv(file_path)

# Display the first few rows of the data
print(data.head())

# Apply a filter (e.g., filter rows where 'Region' is 'Europe')
filtered_data = data[data['Continent'] == 'Europe']  # Replace 'Region' with your actual column name

# Display the filtered data
print(filtered_data)

# Optionally, save the filtered data to a new CSV file
filtered_data.to_csv("filtered_data.csv", index=False)