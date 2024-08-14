import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import io

# Importing Data
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
response = requests.get(URL)
text = io.StringIO(response.text)

df = pd.read_csv(text)
print('Data downloaded and read into a dataframe!')

# Convert 'Year' to datetime format
df['Year'] = pd.to_datetime(df['Year'], format='%Y')

# Create dataframes for recession and non-recession periods
rec_data = df[df['Recession'] == 1]
non_rec_data = df[df['Recession'] == 0]

# Create the figure
fig = plt.figure(figsize=(12, 6))

# Create subplots
ax0 = fig.add_subplot(1, 2, 1)  # First subplot
ax1 = fig.add_subplot(1, 2, 2)  # Second subplot

# Plot for recession period
sns.lineplot(x='Year', y='GDP', data=rec_data, ax=ax0)
ax0.set_xlabel('Year')
ax0.set_ylabel('GDP')
ax0.set_title('GDP Variation during Recession Period')

# Plot for non-recession period
sns.lineplot(x='Year', y='GDP', data=non_rec_data, ax=ax1)
ax1.set_xlabel('Year')
ax1.set_ylabel('GDP')
ax1.set_title('GDP Variation during Non-Recession Period')

# Adjust layout
plt.tight_layout()
plt.show()
