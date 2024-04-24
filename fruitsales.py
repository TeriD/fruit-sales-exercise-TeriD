# Import required modules
import os
import pandas as pd

# Get the path of the current working directory
py_file_path = os.path.dirname(os.path.abspath(__file__))
print(py_file_path)

# Create the DataFrame
# Data for the CSV file
data = {'Apples': [35, 41], 'Bananas': [21, 34], }
labels = ['2017 Sales', '2018 Sales']

# Create the DataFrame
fruit_sales = pd.DataFrame(data, index=labels)

print(fruit_sales)

# Define CSV file path
csv_file_path = os.path.join(py_file_path, 'fruit.csv')

# Write the DataFrame to the CSV file
fruit_sales.to_csv(csv_file_path)
