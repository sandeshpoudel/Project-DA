import pandas as pd

# Example DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, None, 35]  # One missing value
}

df = pd.DataFrame(data)

# Calculate median of 'age' column, ignoring missing values
median_age = df['age'].median()

print("Median age:", median_age)
