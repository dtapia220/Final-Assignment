import pandas as pd
import matplotlib.pyplot as plt
import requests
import io

# Importing Data
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
response = requests.get(URL)
text = io.StringIO(response.text)

df = pd.read_csv(text)
print('Data downloaded and read into a dataframe!')

# Ensure 'Year' is converted to datetime
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df.set_index('Year', inplace=True)

# Group data by 'Year' and calculate the mean of 'Automobile_Sales'
df_line = df.groupby(df.index.year)['Automobile_Sales'].mean()

# Create the plot
plt.figure(figsize=(10, 6))
df_line.plot(kind='line')

# Customize the plot
plt.xticks(list(range(1980, 2024)), rotation=75)
plt.xlabel('Year')
plt.ylabel('Average Automobile Sales')
plt.title('Automobile Sales during Recession')

# Add annotations for specific years of recession
plt.text(1981, df_line.loc[1981] + 100, '1981-82 Recession', fontsize=10)
plt.text(2008, df_line.loc[2008] + 100, '2008 Recession', fontsize=10)

plt.legend(['Automobile Sales'])
plt.savefig("Line_Plot_1.png")
plt.show()
