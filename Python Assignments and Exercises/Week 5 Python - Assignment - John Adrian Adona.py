
##### ASSIGNMENT

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


## INSTRUCTOR WAY: using dictionary or if function.
# Dictionary Way
discount_rates = {
    'China': 0.65,
    'US': 0.45,
    'Malaysia': 0.30,
    'India': 0.25
}
### discount rates 
grouped_df['Discount'] = grouped_df['Country'].apply(lambda x: discount_rates.get(x, 0.15))

grouped_df['Discount'] = grouped_df['Country'].apply(lambda x: 
            0.65 if x == 'China' else
            0.45 if x == 'US' else
            0.30 if x == 'Malaysia' else
            0.25 if x == 'India' else
            0.15                                                     
)
print(grouped_df)

### calculation
grouped_df['Discounted Sales'] = grouped_df['Sales'] - (grouped_df['Sales'] * grouped_df['Discount'])

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

# INSTRUCTOR WAY
import pandas as pd
#1st approach
#File path
current_inventory_file = 'Current_Inventory.csv'
incoming_product_file = 'Incoming_Product.csv'
#Read the current inventory and incoming product csv file.
current_inventory_df = pd.read_csv(current_inventory_file)
incoming_products_df = pd.read_csv(incoming_product_file)
#Find SKU on incoming products file that are not in current inventory
missing_products_df = incoming_products_df[~incoming_products_df['SKU'].isin(current_inventory_df['SKU'])]

print(missing_products_df)


current_inventory_file = 'Current_Inventory.csv'
incoming_product_file = 'Incoming_Product.csv'
#Read the current inventory and incoming product csv file.
current_inventory_df = pd.read_csv(current_inventory_file)
incoming_products_df = pd.read_csv(incoming_product_file)
#Merge the incoming products with the current inventory
merge_df = incoming_products_df.merge(current_inventory_df,on='SKU',how='left',indicator=True)
#Filter the sku's that are not in current inventory
missing_products_df = merge_df[merge_df['_merge'] == 'left_only' ]
missing_products_df.drop(columns=['_merge'],inplace=True)
print(missing_products_df)

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

# INSTRUCTOR WAY
import pandas as pd
#File path
current_inventory_file = 'Current_Inventory.csv'
#Read the current Inventory
current_inventory_df = pd.read_csv(current_inventory_file)

#Create a new column called 'Discount'
#If active column is NO, set discount to 0.65
#If yes = Discount is zero
current_inventory_df['Discount'] = current_inventory_df['Active'].apply(lambda x: 0.65 if x == 'No' else 0)

print(current_inventory_df)