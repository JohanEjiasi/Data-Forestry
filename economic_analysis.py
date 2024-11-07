import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
file_path = r"C:\Users\Johan\OneDrive\Desktop\Trump\downloaded_files\Key_Economic_Indicators.csv"
data = pd.read_csv(file_path)

# Check the columns in the dataset
print("Columns in the dataset:", data.columns)

# Clean the column names by stripping any leading or trailing spaces
data.columns = data.columns.str.strip()

# Check the first few rows of the data
print("First few rows of the dataset:")
print(data.head())

# Check for missing values in the dataset
print("\nMissing values in the dataset:")
print(data.isnull().sum())

# Clean the data: Dropping rows where all values are missing
data_cleaned = data.dropna(how="all")

# Alternatively, you can forward-fill missing values
# data_filled = data.fillna(method='ffill')

# Perform some basic statistical analysis on numeric columns
print("\nSummary statistics of numeric columns:")
print(data.describe())

# Filter only numeric columns for correlation calculation
numeric_data = data.select_dtypes(include='number')

# Calculate the correlation between numeric columns
correlations = numeric_data.corr()
print("\nCorrelation matrix:")
print(correlations)

# Data Visualization: Plot Consumer Confidence in Texas over time
plt.figure(figsize=(10, 6))
plt.plot(data['Year'], data['Consumer Confidence Index TX'], label='Consumer Confidence TX', color='b')
plt.xlabel('Year')
plt.ylabel('Consumer Confidence Index TX')
plt.title('Consumer Confidence Index in Texas Over Time')
plt.legend()
plt.grid(True)
plt.show()

# Data Visualization: Plot Unemployment Rate in Texas over time
plt.figure(figsize=(10, 6))
plt.plot(data['Year'], data['Unemployment TX'], label='Unemployment TX', color='r')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate TX')
plt.title('Unemployment Rate in Texas Over Time')
plt.legend()
plt.grid(True)
plt.show()

# Plot a heatmap of the correlations
plt.figure(figsize=(12, 8))
sns.heatmap(correlations, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Economic Indicators')
plt.show()

# Example: Calculate the percentage change in Consumer Confidence Index in Texas
data['Consumer Confidence Growth TX'] = data['Consumer Confidence Index TX'].pct_change() * 100

# Display the year-over-year growth in Consumer Confidence Index
print("\nConsumer Confidence Growth TX:")
print(data[['Year', 'Consumer Confidence Index TX', 'Consumer Confidence Growth TX']].dropna())
