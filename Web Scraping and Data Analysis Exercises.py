##### ExcelHelpLine Bootcamp: Web Scraping and Data Analysis Exercises

### Web Scraping Activity 
'''
Webscrape from this website: https://www.worldometers.info/world-population/philippines-population/
Produce threee CSV files from the three tables

'''
from bs4 import BeautifulSoup
import requests
import pandas as pd

def webscrape_table_class(url_site, class_name, n):
    page = requests.get(url_site)
    soup = BeautifulSoup(page.content, 'html.parser')

    table_list = soup.find_all('table', class_=class_name)
    table = table_list[n - 1]
    if table:
        tbody = table.find('tbody')
        if tbody:
            rows = tbody.find_all('tr')
            data = []
            header_row = table.find('thead')
            header_cells = header_row.find_all('th')
            column_names = [cell.text.strip() for cell in header_cells]
            data.append(column_names)
            for row in rows:
                cells = row.find_all('td')
                row_data = [cell.text.strip() for cell in cells]
                data.append(row_data)
            df = pd.DataFrame(data[1:], columns=data[0])
            return df

## Initiate Web Scraping 
url = "https://www.worldometers.info/world-population/philippines-population/"

class_name_pop = "table table-striped table-bordered table-hover table-condensed table-list"
class_name_city = "table table-hover table-condensed table-list"

# Population of the Philippines (2024 and historical)
phil_pop = webscrape_table_class(url, class_name_pop, 1)
print(phil_pop)
file_name = 'Population of the Philippines (2024 and historical).csv'
phil_pop.to_csv(file_name, index=False)

# Philippines Population Forecast
phil_forecast = webscrape_table_class(url, class_name_pop, 2)
print(phil_forecast)
file_name = 'Philippines Population Forecast.csv'
phil_pop.to_csv(file_name, index=False)

# Main Cities by Population in the Philippines
main_city = webscrape_table_class(url, class_name_city, 1)
print(main_city)
file_name = 'Main Philippine Cities by Population.csv'
main_city.to_csv(file_name, index=False)


### Data Analysis Exercises
'''
Perform the following tasks on the Customers and Orders CSV dataset

'''

# 1. Data Cleaning and Preprocessing Task: Clean both of the CSV files in Python.

import pandas as pd
import numpy as np

customers = pd.read_csv('Customers.csv')
orders = pd.read_csv('Orders.csv')

print(customers)
print(orders)

customers.loc[5, 'Customer_ID'] = 6
customers['Points'].fillna(customers['Points'].mean(), inplace=True)

orders.dropna(inplace=True)
orders['Order_Date'] = orders['Order_Date'].apply(lambda x: '/'.join(x.split('/')[:2] + [str(2024)]))
orders[['Order_Date', 'Shipping_Date']] = orders[['Order_Date', 'Shipping_Date']].apply(pd.to_datetime)
orders.loc[13, 'Order_Total'] = 7392.68 # fixing extra letter in value

# 2. Calculate Average Shipping Duration: What is the average shipping in terms of days?

conso_df = pd.merge(customers, orders, on='Customer_ID')
print(conso_df)

conso_df.loc[4, 'State'] = conso_df['State'].mode().values # MODE IMPUTATION: only did this as part of assignment

print(conso_df)
conso_df['Order_To_Shipping'] = (conso_df['Shipping_Date'] - conso_df['Order_Date']).dt.days
conso_df.dtypes
average_shipping_duration = conso_df['Order_To_Shipping'].mean()
print(average_shipping_duration)

# 3. Identify Top Customers by Points and Revenue: Top 3 Customers in terms of Points and Revenue.

# Top 3 customer in terms of points

unique_top_3 = conso_df.sort_values(by='Points', ascending=False).nlargest(3, 'Points')
print(unique_top_3) # retrieve unique rows of top three

top_3 = conso_df[conso_df['Points'].isin(unique_top_3['Points'])].sort_values(by='Points', ascending=False)
print(top_3)

# Top 3 customer (Customer Name) in terms of Revenue(Order_total)

conso_df.dtypes
conso_df['Order_Total'] = pd.to_numeric(conso_df['Order_Total'])
sorted_order_total = conso_df.sort_values(by='Order_Total', ascending=False)
unique_customers = sorted_order_total.drop_duplicates(subset='Customer Name', keep='first')
print(unique_customers.nlargest(3, 'Order_Total'))

# 4. State Revenue Aggregation: Top 5 state in terms of Revenue.

conso_df.dtypes
conso_df['State'] = conso_df['State'].astype(str)
grouped_by_state = conso_df.groupby('State')['Order_Total'].sum().reset_index()
print(grouped_by_state.nlargest(5, 'Order_Total'))

# Total Sum of Order_total for June

print(conso_df)
conso_df['Order_Total'].sum()

# 5. Visualizing Data with Bar and Line Charts: Create a bar chart (Revenue by State) and line chart.

# Create a bar chart -- Plot the Revenue by State

import matplotlib.pyplot as plt
plt.figure(figsize=(9, 5))
bar_graph = grouped_by_state.plot(kind='bar', color='pink')
bar_graph.set_xticks(range(len(grouped_by_state)))
bar_graph.set_xticklabels(grouped_by_state['State'].tolist(), rotation=45)
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
plt.title('Daily Order Amount in June 2024')
plt.xlabel('Date')
plt.ylabel('Daily Order Amount')
plt.legend()
plt.grid(True)
plt.show()