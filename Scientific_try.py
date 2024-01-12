import numpy as nu
import matplotlib.pyplot as plt
import pandas as pd

file_path = 'center_sternum.txt'
data = pd.read_csv(file_path, delim_whitespace=True)
data = data.iloc[:,2:10]
new_column_names = ['LogFreq', 'Timestamp', 'AccX', 'AccY', 'AccZ', 'GyroX', 'GyroY', 'GyroZ']
data.columns = new_column_names
print(data.head())

#Loading datda
df = pd.read_csv('path/to/your/logfile.txt', sep='\t')

#Eliminating the first three columns from the statistics
sensor_columns = df.columns[3:] 

#This function finds the percentiles
stats_df = df[sensor_columns].describe().transpose()  # Basic statistical descriptors
stats_df['Variance'] = df[sensor_columns].var()  #Variance 

print(stats_df)

# Calculating 25th and 75th percentiles
percentiles = df.describe(percentiles=[.25, .75])
percentiles_25_75 = percentiles.loc[['25%', '75%']]

print("25th and 75th Percentiles:")
print(percentiles_25_75)

# Calculating correlation coefficients
correlation = df.corr()
print("\nCorrelation Coefficients:")
print(correlation)

# Correlation Matrix
corr_matrix = df[sensor_columns].corr()
print("\nCorrelation Matrix:\n", corr_matrix)
