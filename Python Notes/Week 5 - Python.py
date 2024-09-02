# Week 17 / Week 5 Python

# Pandas
import pandas as pd

# Data Frame

# Reading from CSV file
df = pd.read_csv('Current_Inventory.csv')
print(df)

# Display 1st 5 rows
print(df.head())

# Display last 5 rows
print(df.tail())

# Display columns
print(df.columns)

# Access specific / single column
print(df['SKU'])

# Access specific multiple column
print(df[['SKU', 'Quantity']])

# Display values
print(df.values)

# Describe -- quick statistics / summary of data
print(df.describe)

# Sum of the prices
total_price = df['Price'].sum()
total_quantity = df['Quantity'].sum()

print("Total:", total_price)
print("Total:", total_quantity)

# Getting count of values
total_count = df['Product Name'].count()
print("Total Count:", total_count)

# Getting distinct count of values
unique_count = df['Product Name'].nunique()
print("Total Distinct Count:", unique_count)

unique_count = df['SKU'].nunique()
print("Total Distinct Count:", unique_count)

# Writing to a CSV file
#df.to_csv()

# Reading from an Excel file
#df = pd.read_excel('', sheet_name='')

# Writing to an Excel file
#df.to_excel('', sheet_name='')


##### 1st Activity 
##### SUM PRICE AND QUANTITY, COUNT PRODUCT, SAVE IT AS A CSV FILE

test = pd.DataFrame([total_price, total_quantity, total_count])

test.to_csv('Total And Counts.csv', index=False)


# Get All inactive products and active products on current inventory and save it on CSV file
inactive_products = df[df['Active'] == 'No']
inactive_products.to_csv('Inactive Products.csv', index=False)

active_products = df[df['Active'] == 'Yes']
active_products.to_csv('Active Products.csv', index=False)

# Sum all inactive and active products on Current Inventory
total_active_products = active_products['Price'].sum()
print("Total Active Price:", total_active_products)

total_inactive_products = inactive_products['Price'].sum()
print("Total Active Price:", total_inactive_products)


# VLOOKUP
df = pd.read_csv('Current_Inventory.csv')
df_products = pd.read_csv('Products.csv')

merge_df = pd.merge(df, df_products, on=('SKU'), how='left')

merge_df.to_csv('Merge File - Final.csv')


# GROUP BY
df = pd.read_csv('Sales Sample.csv')
grouped_df = df.groupby('Country')['Sales'].sum().reset_index()
print(grouped_df)

# What if we want to add new column?
grouped_df['Discount'] = .45
print(grouped_df)

# Calculation by Columns
# Multiply Sales and Discount to create new column - Discounted Sales
grouped_df['Discounted Sales'] = grouped_df['Sales'] - (grouped_df['Sales'] * grouped_df['Discount'])
print(grouped_df)
grouped_df.to_csv('Grouped Data.csv')



##### 1st Activity 
##### SUM PRICE AND QUANTITY, COUNT PRODUCT, SAVE IT AS A CSV FILE -- use current inventory
df = pd.read_csv('Current_Inventory.csv')
print(df)

# Sum of the prices and quantity
total_price = df['Price'].sum()
total_quantity = df['Quantity'].sum()

print("Total:", total_price)
print("Total:", total_quantity)

# Getting count of values
total_count = df['Product Name'].count()
print("Total Count:", total_count)

# Getting distinct count of values
unique_count = df['Product Name'].nunique()
print("Total Distinct Count:", unique_count)

unique_count = df['SKU'].nunique()
print("Total Distinct Count:", unique_count)

new_df = pd.DataFrame([[total_price, total_quantity, total_count]], columns=['Total Price', 'Total Quantity', 'Total Count'])
new_df.to_csv('Week 5 Python - Activity 1.csv')

##### 2ND Activity
##### Using Sales Sample new code (Save it as CSV file)
# China .65
# USA .45
# Malaysia .30
# India .25
# the rest .15
df = pd.read_csv('Sales Sample.csv')
grouped_df = df.groupby('Country')['Sales'].sum().reset_index()
print(grouped_df)

# What if we want to add new column?
list = []
for index, country in enumerate(grouped_df['Country']):
    if country == "China":
        list.append(.65)
    elif country == "US":
        list.append(.45)
    elif country == "Malaysia":
        list.append(.30)
    elif country == "India":
        list.append(.25)
    else:
        list.append(.15)

print(list)
grouped_df['Discount'] = list
print(grouped_df)
grouped_df.to_csv('Week 5 Python - Activity 2.csv')


##### 3rd Activity 
##### Compare incoming product and current inventory
##### SKU, product name, price and inventory na wala sa inventory
##### Using current inventory csv, find all the products that are not in current inventory
##### Print price and total quantity of those products not in inventory
df = pd.read_csv('Current_Inventory.csv')
df_incoming = pd.read_csv('Incoming_Product.csv')

# checking products not in current inventory
merge_df = pd.merge(df, df_incoming, on='SKU', how='right')
print(merge_df)

# get products not in inventory
#not_in_inventory = df_incoming[~df_incoming['SKU'].isin(df['SKU'])]
inventory_sku = df['SKU'].tolist()
not_in_inventory = df_incoming[[sku not in inventory_sku for sku in df_incoming['SKU']]]
print(not_in_inventory)

total_price = not_in_inventory['Price'].sum()
total_quantity = not_in_inventory['Quantity'].sum()
print("Total:", total_price)
print("Total:", total_quantity)

not_in_inventory.to_csv('Week 5 Python - Activity 3.csv')

##### 4th Activity
##### using current inventory, create new column called Discount
##### if the product is Active = No -> discount is .65 
##### if the product is not Active -> no discount
df = pd.read_csv('Current_Inventory.csv')
print(df)

list = []
for index, status in enumerate(df['Active']):
    if status == "No":
        list.append(.65)
    else:
        list.append(0)
print(list)

df['Discount'] = list
print(df)

df['New Price'] = df['Price'] - (df['Price'] * df['Discount'])
print(df)

df.to_csv('Week 5 Python - Activity 4.csv')

#Activity
#1st Activity
#Sum Price and Quantity, COUNT Product save it as csv file. -- Use Current Inventory

#Activity
#2nd Activity
#Using Sales Sample new code(Save it as csv file)
#China .65
#US .45
#Malaysia .30
#India .25
#The rest is .15

#2nd activity
#Change the discount based on above data.
#3rd Activity
#Using Current Inventory and Incoming Products csv
#Find all the Products that are not in Current Inventory
#Print The Price and the Total Quantity of those products
#that are not in Current Inventory
#4th Activity
#Using Current Inventory
#Create a new column called Discount
#If the product is Active = No
#the value to the discount column will be 65%
#if Active = Yes
#Discount column will be 0
#Create a new column called New Price
#New Price = Price - (Price * Discount)


