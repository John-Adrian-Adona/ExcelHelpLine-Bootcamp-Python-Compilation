# Assignment

'''
Webscrape from this website: https://www.worldometers.info/world-population/philippines-population/
Produce threee CSV files from the three tables

'''
from bs4 import BeautifulSoup
import requests
import pandas as pd

def webscrape_table_class(url_site, class_name):
    page = requests.get(url_site)
    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find('table', class_=class_name)
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

# Population of the Philippines (2024 and historical)
url = "https://www.worldometers.info/world-population/philippines-population/"
class_name = "table table-striped table-bordered table-hover table-condensed table-list"
phil_pop = webscrape_table_class(url, class_name)
print(phil_pop)
file_name = 'Population of the Philippines (2024 and historical).csv'
phil_pop.to_csv(file_name, index=False)

# Main Cities by Population in the Philippines
url = "https://www.worldometers.info/world-population/philippines-population/"
class_name = "table table-hover table-condensed table-list"
test = webscrape_table_class(url, class_name)
print(test)
file_name = 'Main Philippine Cities by Population.csv'
test.to_csv(file_name, index=False)

# Philippines Population Forecast
# My created function does not work in webscrapping this table
# I decided to do a separate python code for this, using div class

url = "https://www.worldometers.info/world-population/philippines-population/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

divs = soup.find('div', attrs={"class": "table-responsive",
                                "style": "clear:both "})
if divs:
    table = divs.find('table', class_="table table-striped table-bordered table-hover table-condensed table-list")
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
                print(row_data)

df = pd.DataFrame(data[1:], columns=data[0])
print(df)

file_name = 'Philippines Population Forecast.csv'
df.to_csv(file_name, index=False)

# use indexing (alternative)
# find_all code -> table[2] -> proceed as normal
