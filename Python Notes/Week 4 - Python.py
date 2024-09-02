# Week 16 / Week Python 4 

# Webscrapping

# BeautifulSoup4
# requests
# pandas

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.worldometers.info/world-population/population-by-country/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# find the table with specific ID
table = soup.find('table', id='example2')
print(table)

# check if the table is found
if table:
    # find the table body -- tbody
    tbody = table.find('tbody')

    if tbody:
        #find all rows within the table body
        rows = tbody.find_all('tr')
        #print(rows)
        #initialized empty list to store data
        data = []
        #find column name / column header
        header_row = table.find('thead')
        header_cells = header_row.find_all('th')
        #print(header_cells)
        column_names = [cell.text.strip() for cell in header_cells]
        print(column_names)
        #Append the column names to data
        data.append(column_names)
        for row in rows:
            cells = row.find_all('td')
            #extract the text from each cell and add it to the data list
            row_data = [cell.text.strip() for cell in cells]
            data.append(row_data)
            print(row_data)

        # convert the data to data frame
        df = pd.DataFrame(data[1:], columns=data[0])
        print(df)

        # save data frame to csv file
        #file_path = "D:\John Adrian Files\Files\Other Files\For Learning\ExcelHelpLine\Week 13 - onwards - Python\scraped_file.csv"
        #df.to_csv(file_path)
        #print("Scraped file saved! ",file_path)

#  file_path = r"C:\Users\Ryzen\Desktop\Python\Week4\file.xlsx"
#        df.to_excel(file_path,index=False)
#        print("Scraped file saved! ",file_path)

#file_path = r"C:\Users\Zemo\Documents\Python Tutorial\Python tutorial 6-8-24\Week 4\scraped_file.xlsx"


url_2 = "https://www.worldometers.info/world-population/philippines-population/"
page_2 = requests.get(url_2)
soup_2 = BeautifulSoup(page_2.content, 'html.parser')

# find the table with specific ID
table_2 = soup_2.find('table', class_='table table-hover table-condensed table-list')
print(table_2)

# check if the table is found
if table_2:
    # find the table body -- tbody
    tbody_2 = table_2.find('tbody')

    if tbody_2:
        #find all rows within the table body
        rows = tbody_2.find_all('tr')
        #print(rows)
        #initialized empty list to store data
        data = []
        #find column name / column header
        header_row = table_2.find('thead')
        header_cells = header_row.find_all('th')
        #print(header_cells)
        column_names = [cell.text.strip() for cell in header_cells]
        print(column_names)
        #Append the column names to data
        data.append(column_names)
        for row in rows:
            cells = row.find_all('td')
            #extract the text from each cell and add it to the data list
            row_data = [cell.text.strip() for cell in cells]
            data.append(row_data)
            print(row_data)

        # convert the data to data frame
        df = pd.DataFrame(data[1:], columns=data[0])
        print(df)



# Assignment: 3 csv files from website
   