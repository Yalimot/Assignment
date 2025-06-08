1.2 Load the Dataset Using pandas
python
Copy
import pandas as pd

# Load the dataset
df = pd.read_csv('iris.csv')

# Display the first few rows
print(df.head())
1.3 Explore the Structure
python
Copy
# Check data types and missing values
print(df.info())

# Check for missing values
print(df.isnull().sum())
1.4 Clean the Dataset
If there are missing values, you can handle them by either filling or dropping them.

python
Copy
# Fill missing values with the mean of each column
df.fillna(df.mean(), inplace=True)

# Alternatively, drop rows with missing values
# df.dropna(inplace=True)
📊 Task 2: Basic Data Analysis
2.1 Compute Basic Statistics
python
Copy
# Get basic statistics for numerical columns
print(df.describe())
2.2 Group by a Categorical Column and Compute Mean
Assuming the dataset has a 'Species' column:
reddit.com

python
Copy
# Group by 'Species' and compute the mean of numerical columns
grouped = df.groupby('Species').mean()
print(grouped)
This will provide the mean of each numerical column for each species.

📈 Task 3: Data Visualization
3.1 Import Necessary Libraries
python
Copy
import matplotlib.pyplot as plt
import seaborn as sns
3.2 Line Chart: Trends Over Time
If your dataset includes a time-related column, you can plot trends over time.

python
Copy
# Example: Plotting a line chart for a time-related column
# df['Year'] = pd.to_datetime(df['Year'])
# plt.plot(df['Year'], df['Value'])
# plt.title('Trends Over Time')
# plt.xlabel('Year')
# plt.ylabel('Value')
# plt.show()
3.3 Bar Chart: Comparison Across Categories
python
Copy
# Create a bar chart comparing the mean sepal length across species
df.groupby('Species')['SepalLengthCm'].mean().plot(kind='bar')
plt.title('Average Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Length')
plt.show()
3.4 Histogram: Distribution of a Numerical Column
python
Copy
# Create a histogram for the 'SepalLengthCm' column
df['SepalLengthCm'].plot(kind='hist', bins=20, edgecolor='black')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()
3.5 Scatter Plot: Relationship Between Two Numerical Columns
python
Copy
# Create a scatter plot for Sepal Length vs Sepal Width
plt.scatter(df['SepalLengthCm'], df['SepalWidthCm'])
plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.show()
