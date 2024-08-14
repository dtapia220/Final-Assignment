import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import requests

# Import Data
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
response = requests.get(URL)
text = io.StringIO(response.text)

df = pd.read_csv(text)
print('Data downloaded and read into a dataframe!')

# Optional: Inspecting the data
print(df.describe())
print(df.columns)

# Convert 'Year' to datetime if it's not already, and set it as the index
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df.set_index('Year', inplace=True)

# Group data by 'Year' and calculate the mean of 'Automobile_Sales'
df_line = df.groupby(df.index.year)['Automobile_Sales'].mean()

# Create the plot
plt.figure(figsize=(10, 6))
df_line.plot(kind='line', marker='o')
plt.xlabel('Year')
plt.ylabel('Average Automobile Sales')
plt.title('Automobile Sales during Recession')

# Add annotations for specific recession years
recession_years = [2008, 2020]  # Example years
for year in recession_years:
    if year in df_line.index:
        plt.annotate(
            'Recession',
            xy=(year, df_line.loc[year]), 
            xytext=(year, df_line.max() * 0.9),  # Adjust text position
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10
        )

# Save the plot as "Line_Plot_1.png"
plt.savefig("Line_Plot_1.png")

# Show the plot
plt.show()

# Optional: Further inspection of the data
print(df.describe())
print(df.columns)
