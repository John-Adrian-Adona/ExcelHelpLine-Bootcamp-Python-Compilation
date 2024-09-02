# Week 18 / Week 6 Python

# Pandas
import pandas as pd

# Clean data using Pandas
# Empty Cells
# Remove the rows, Supply a value (average, average of the row before, average of succ. rows)
df = pd.read_csv('Sample Data.csv')
print(df)

# dropna <- returns a new dataframe, not deleting the original
new_df = df.dropna()
print(new_df.to_string())

# modify original file 
df.dropna(inplace=True)
print(df.to_string())

# Data in wrong format
df = pd.read_csv('Sample Data.csv')
print(df)

df['Date'] = pd.to_datetime(df['Date'], errors='coerce') # coersce - any errors returns a NaT value to it
print(df)

# Wrong data
df = pd.read_csv('Sample Data.csv')
print(df)

df.loc[7, 'Duration '] = 45
print(df)

# ------------
for x in df.index:
    if df.loc[x, 'Duration '] > 100:
        df.loc[x, 'Duration '] = 60

print(df)

for x in df.index:
    if df.loc[x, 'Duration '] > 99:
        df.drop(x, inplace=True)

# Duplicates 
df = pd.read_csv('Sample Data.csv')
print(df.duplicated())

df.drop_duplicates(inplace=True)
print(df)


# Generate Data using Pandas 

# Essential Functions with Examples:
# Sorting, Rename, Shape, Merge, Apply functions, loc, Iloc, pivot.

import pandas as pd
import numpy as np
import random

# set seed
np.random.seed(42)
random.seed(42)

# generate random data
offices_data = {
    'office_id': [1,2,3,4,5],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'state': ['NY', 'LA', 'CA', 'TX', 'AZ']
}

offices_df = pd.DataFrame(offices_data)
print(offices_df)

employee_names = [
    'John Smith', 'Jane Doe', 'Alice Johnson', 'Kleine Evasco', 'Azrael Callisto',
    'Jeffrey Stilton', 'Marget Baget', 'John Mike', 'Ayaka Flores', 'Luz Margie',
    'Goku Son', 'Elan Misk', 'Mirk Zikkerberg', 'Money Pacs', 'Lebon Jams',
    'Stephany Hawklings', 'Shiori Novel', 'Peko Navira', 'Luke Waterswimmer', 'Harry Buffer'
]

position = [
    'CEO', 'Specialist', 'Manager', 'Financial Analyst', 'Logistics Rank and File',
    'Cashier', 'Relation Specialist', 'Janitor', 'Interior Designer', 'Security Guard', 
    'Auditor'
]

department = [
    'HR', 'IT', 'Marketing', 'Legal', 'Sales', 'Support', 'Operations', 'R&D', 'Calls'
]

salaries = np.random.randint(50000,150000, size=20)
office_ids = np.random.choice([1,2,3,4,5], size=20)

employee_data = {
    'Employee_Name': employee_names,
    'Position': np.random.choice(position, size=20),
    'Department': np.random.choice(department, size=20),
    'Salaries': salaries,
    'Office_ID': office_ids
}

employee_df = pd.DataFrame(employee_data)
print(employee_df)
employee_df.to_csv('Employee.csv')
offices_df.to_csv('Office.csv')

# ---------
sorted_employee_df = employee_df.sort_values(by='Salaries', ascending=False)
print(sorted_employee_df)

# Rename Column
employee_df_renamed = employee_df.rename(columns={'Employee_Name': 'Name'})
print(employee_df_renamed)

# Shape
print(employee_df.shape)

#Merge tables
merge_df = pd.merge(employee_df,offices_df,left_on='Office_ID',right_on='office_id')
merge_df.to_csv('Sample merge.csv',index=False)

# Function 
# Create a function to categorize salary
def categorize_salary(salary):
    if salary < 60000:
        return 'Low'
    elif 60000 <= salary < 100000:
        return 'Medium'
    else:
        return 'High'

employee_df['Salary Category'] = employee_df['Salaries'].apply(categorize_salary)
print(employee_df)

# Loc nad Iloc
print(employee_df.loc[employee_df['Department'] == 'IT'])

# Pivot
pivot_df = employee_df.pivot_table(index='Department', values='Salaries', aggfunc='mean')
print(pivot_df)

# Visualizations 

# Sending Email

# project