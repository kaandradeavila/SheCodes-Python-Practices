""" 
1. Display each customer from the CSV in this format:
    > “Customer #53, Patricia Goodwin, vaughanchristy@lara.biz”
"""
import csv

with open("customers_w2.csv", mode = "r") as file:
    customers_reader = csv.reader(file)

    for customer in customers_reader:
        print(f"Customer #{customer[0]}, {customer[2]} {customer[3]}, {customer[9]}")

file.close()
