import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a pandas DataFrame
df = pd.read_csv("data.csv")

# Convert the price column to numeric values (handle commas and NaNs)
df['price'] = pd.to_numeric(df['price'].str.replace(',', ''), errors='coerce')

# Drop rows where price is NaN
df = df.dropna(subset=['price'])

# Replace NaN values in the title column with a placeholder
df['title'] = df['title'].fillna('No Title')

# Sort the DataFrame by price in descending order
df_sorted = df.sort_values(by='price', ascending=False)

# Limit the data to the top N products if necessary
top_n = df_sorted.head(10)  # Adjust the number if needed

# Plot a bar graph
plt.figure(figsize=(10, 6))
plt.barh(top_n['title'], top_n['price'], color='skyblue')
plt.xlabel('Price (INR)')
plt.ylabel('Product Title')
plt.title('Top 10 Most Expensive Products')
plt.gca().invert_yaxis()  # Invert y-axis to show highest price at the top
plt.tight_layout()

# Save the plot as an image
plt.savefig('price_comparison_chart.png')

# Display the plot
plt.show()
