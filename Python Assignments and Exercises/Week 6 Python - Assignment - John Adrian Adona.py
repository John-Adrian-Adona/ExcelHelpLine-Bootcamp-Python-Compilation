##### ASSIGNMENT

import pandas as pd
import numpy as np

customers = pd.read_csv('Customers.csv')
orders = pd.read_csv('Orders.csv')

print(customers)
print(orders)

# 1. Clean the data on both csv file using python.

customers.loc[5, 'Customer_ID'] = 6
customers['Points'].fillna(customers['Points'].mean(), inplace=True)

orders.dropna(inplace=True)
orders['Order_Date'] = orders['Order_Date'].apply(lambda x: '/'.join(x.split('/')[:2] + [str(2024)]))
orders[['Order_Date', 'Shipping_Date']] = orders[['Order_Date', 'Shipping_Date']].apply(pd.to_datetime)
orders.loc[13, 'Order_Total'] = 7392.68 # fixing extra letter in value

# 2. Customers and orders table has a relationship.
# (Customer_ID on orders csv file)

conso_df = pd.merge(customers, orders, on='Customer_ID')
print(conso_df)

conso_df.loc[4, 'State'] = conso_df['State'].mode().values # MODE IMPUTATION: only did this as part of assignment


# Answer the following using python code:

# What is the average shipping in terms of days?

print(conso_df)
conso_df['Order_To_Shipping'] = (conso_df['Shipping_Date'] - conso_df['Order_Date']).dt.days
conso_df.dtypes
average_shipping_duration = conso_df['Order_To_Shipping'].mean()
print(average_shipping_duration)

# Top 3 customer in terms of points

unique_top_3 = conso_df.sort_values(by='Points', ascending=False).nlargest(3, 'Points')
print(unique_top_3) # retrieve unique rows of top three

top_3 = conso_df[conso_df['Points'].isin(unique_top_3['Points'])].sort_values(by='Points', ascending=False)
print(top_3)

# Top 3 customer(Customer Name) in terms of Revenue(Order_total)

conso_df.dtypes
conso_df['Order_Total'] = pd.to_numeric(conso_df['Order_Total'])
sorted_order_total = conso_df.sort_values(by='Order_Total', ascending=False)
print(sorted_order_total.nlargest(3, 'Order_Total'))

# Top 5 state in terms of Revenue

conso_df.dtypes
conso_df['State'] = conso_df['State'].astype(str)
grouped_by_state = conso_df.groupby('State')['Order_Total'].sum().reset_index()
print(grouped_by_state.nlargest(5, 'Order_Total'))

# Total Sum of Order_total for June

print(conso_df)
conso_df['Order_Total'].sum()

# Create a bar chart -- Plot the Revenue by State

import matplotlib.pyplot as plt
plt.figure(figsize=(9, 5))
bar_graph = grouped_by_state.plot(kind='bar', color='pink')
bar_graph.set_xticks(range(len(grouped_by_state)))
bar_graph.set_xticklabels(grouped_by_state['State'].tolist(), rotation=45)
#plt.xticks(ticks=x, labels=grouped_by_state['State'].tolist(), rotation=45)
plt.title('Total Revenue per US State')
plt.xlabel('US State')
plt.ylabel('Total Revenue')
plt.show()


# Create a Line chart. Plot the daily trend of order total based on Order Date.

grouped_by_trend = conso_df.groupby('Order_Date')['Order_Total'].sum().reset_index()
print(grouped_by_trend)

plt.figure(figsize=(12,6))
line_chart = grouped_by_trend['Order_Total'].plot(kind='line', color='pink')
line_chart.set_xticks(range(len(grouped_by_trend)))
line_chart.set_xticklabels(grouped_by_trend['Order_Date'].tolist(), rotation=45)
#plt.plot(grouped_by_trend.index, grouped_by_trend['Order_Total'], label="Total Order Amount", color='purple')
plt.title('Daily Order Amount in June 2024')
plt.xlabel('Date')
plt.ylabel('Daily Order Amount')
plt.legend()
plt.grid(True)
plt.show()


### PYTHON EXAM

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']
}

df = pd.DataFrame(data)
print(df)

#1.	Write code to calculate the average age of the individuals in the DataFrame.
#python

average_age = df['Age'].mean()
print(average_age)

#2.	Write code to find the name of the individual who is from the city of Chicago.
#python

from_chicago = df[df['City'] == 'Chicago']
print(from_chicago['Name'])

#3.	Write code to count how many individuals are listed in the DataFrame.
#python

how_many_people = df['Name'].count()
print(how_many_people)

#4.	Write code to retrieve the city of residence for the individual named 'Bob'.
#python

where_bob_lives = df[df['Name'] == 'Bob']
print(where_bob_lives['City'])

#5.	Write code to find the name of the youngest individual in the DataFrame.
#python

the_youngest = df[df['Age'] == df['Age'].min()]
print(the_youngest['Name'])