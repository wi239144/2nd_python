#import needed suite
import pandas as pd
import openpyxl
import requests
from bs4 import BeautifulSoup

#setting website url, stock related for example
url = "https://histock.tw/stock/dividend.aspx"

#path of excel file wanted to save and load workbook
targetfile = "./example.xlsx"
workbook = openpyxl.load_workbook(targetfile)

# append new sheet
sheet = workbook.create_sheet("test1", 0)

#use get method and soup to analysis data with text format
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

#find header and loop for catching data
result = soup.find_all("table")[0]
rows = result.find_all("tr")
for row in rows:
    data = [cell.get_text(strip=True) for cell in row.find_all(["th", "td"])]
    sheet.append(data)

#save to excel file and show data saved
workbook.save(targetfile)
print("Data saved to Excel.")