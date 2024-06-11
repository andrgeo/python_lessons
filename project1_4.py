import csv
import pandas

rows = []
with open('orderdata_sample.csv', "a", encoding="utf-8") as fh:
    reader = pandas.read_csv('orderdata_sample.csv')
    Quantity = reader['OrderID']
    reader = reader.assign(total = reader['Quantity'] * reader['Price'] + reader['Freight'])
    reader.to_csv('new_orderdate.csv')