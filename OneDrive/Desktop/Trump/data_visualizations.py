import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Update this to the correct path of your CSV file
file_path = r'C:\Users\Johan\OneDrive\Desktop\Trump\downloaded_files\Key_Economic_Indicators.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Preview the column names and first few rows
print("Column Names: ", df.columns)
print(df.head())

# Example 1: Line plot for Consumer Confidence Index TX
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Consumer Confidence Index TX'], label='Consumer Confidence Index TX')
plt.title('Consumer Confidence Index TX Over Time')
plt.xlabel('Year')
plt.ylabel('Consumer Confidence Index TX')
plt.legend()
plt.grid(True)
plt.show()

# Example 2: Bar chart for Unemployment TX (showing unemployment rate over the years)
plt.figure(figsize=(10, 6))
plt.bar(df['Year'], df['Unemployment TX'], color='skyblue', label='Unemployment TX')
plt.title('Unemployment TX Over Time')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate (%)')
plt.legend()
plt.grid(True)
plt.show()

# Example 3: Scatter plot for Gross Value Natural Gas Production vs Year
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['Gross Value Natural Gas Production'], label='Natural Gas Production', color='orange')
plt.title('Natural Gas Production Over Time')
plt.xlabel('Year')
plt.ylabel('Gross Value Natural Gas Production')
plt.legend()
plt.grid(True)
plt.show()

# Example 4: Heatmap for correlations between economic indicators
# Ensure there are no missing values in the columns you are interested in
correlation_matrix = df.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap of Economic Indicators')
plt.show()

# Example 5: Histogram for Distribution of Consumer Price Index TX
plt.figure(figsize=(10, 6))
plt.hist(df['Consumer Price Index TX'].dropna(), bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Consumer Price Index TX')
plt.xlabel('Consumer Price Index TX')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Example 6: Line plot for Nonfarm Employment TX vs Nonfarm Employment U.S.
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Nonfarm Employment TX'], label='Nonfarm Employment TX', color='blue')
plt.plot(df['Year'], df['Nonfarm Employment U.S.'], label='Nonfarm Employment U.S.', color='green')
plt.title('Nonfarm Employment TX vs Nonfarm Employment U.S.')
plt.xlabel('Year')
plt.ylabel('Nonfarm Employment')
plt.legend()
plt.grid(True)
plt.show()

# Example 7: Bar chart for Retail Gasoline Price TX (showing gas price trends over time)
plt.figure(figsize=(10, 6))
plt.bar(df['Year'], df['Retail Gasoline Price TX'], color='red', label='Retail Gasoline Price TX')
plt.title('Retail Gasoline Price TX Over Time')
plt.xlabel('Year')
plt.ylabel('Retail Gasoline Price ($)')
plt.legend()
plt.grid(True)
plt.show()

# Example 8: Line plot for Total Sales Tax Collections TX vs Year
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Total Sales Tax Collections TX'], label='Total Sales Tax Collections TX', color='purple')
plt.title('Total Sales Tax Collections TX Over Time')
plt.xlabel('Year')
plt.ylabel('Total Sales Tax Collections TX')
plt.legend()
plt.grid(True)
plt.show()
