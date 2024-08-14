import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import io
import requests

# Importing Data
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
response = requests.get(URL)
text = io.StringIO(response.text)

df = pd.read_csv(text)
print('Data downloaded and read into a dataframe!')

# Optional: Inspecting the data
print(df.describe())
print(df.columns)

# Ensure that your data has a 'Year' column and a 'Automobile_Sales' or similar column
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df.set_index('Year', inplace=True)

# Create the line plot
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Automobile_Sales'], marker='o')

# Customize the plot
plt.xticks(df.index.year)  # Setting the x-axis with year ticks
plt.xlabel('Year')
plt.ylabel('Automobile Sales')
plt.title('Automobile Sales during Recession')

# Adding annotations for two recession years (for example, 2008 and 2020)
plt.annotate('Recession', xy=(2008, df.loc['2008', 'Automobile_Sales']), 
             xytext=(2008, df['Automobile_Sales'].max()), 
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.annotate('Recession', xy=(2020, df.loc['2020', 'Automobile_Sales']), 
             xytext=(2020, df['Automobile_Sales'].max()), 
             arrowprops=dict(facecolor='black', shrink=0.05))

# Save the plot as "Line_Plot_1.png"
plt.savefig("Line_Plot_1.png")

# Show the plot
plt.show()

# Optional: Further inspection of the data
print(df.describe())
print(df.columns)





















