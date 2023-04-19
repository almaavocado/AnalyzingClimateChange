import pandas as pd
import matplotlib.pyplot as plt

# Load the climate data into a pandas DataFrame
df = pd.read_csv('ghcn_dataset.csv')

# Convert the DATE column to a datetime object
df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%d')


# select only the relevant columns
df = df[['DATE', 'NAME', 'TEMP']]

# filter out missing temperature data
df = df[df['TEMP'] != -9999]

# group by date and calculate average temperature for each day
daily_temps = df.groupby('DATE')['TEMP'].mean()

# plot the data
plt.plot(daily_temps.index, daily_temps.values, color='blue')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Average Daily Temperature')
plt.show()