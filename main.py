import pandas as pd

# Load GHCN dataset into a Pandas DataFrame
df = pd.read_csv('ghcn_dataset.csv')
print(df.columns)

# Convert the date column to a Pandas datetime object
df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%d')

# Subset the dataset to only include temperature data
temp_df = df[(df['NAME'] == station_name) & (df['TEMP_ATTRIBUTES'] == '  H')]['TEMP']

# Group the data by year and calculate the average temperature
temp_df['year'] = temp_df['DATE'].dt.year
#temp_by_year = temp_df.groupby('year')['value'].mean()

# Plot the temperature trends over time
#temp_by_year.plot()