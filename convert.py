import pandas as pd

# Load the original CSV file
df = pd.read_csv('data.csv')

# Calculate the number of rows in each output file
num_rows = len(df) // 10

# Split the dataframe into 10 smaller dataframes
dfs = [df[i*num_rows:(i+1)*num_rows] for i in range(10)]

# Save each dataframe to a separate CSV file
for i, df in enumerate(dfs):
    df.to_csv(f'small_file_{i}.csv', index=False)
